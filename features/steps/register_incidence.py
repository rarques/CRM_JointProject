from behave import *

use_step_matcher("re")


@step("There are prodcuts in the data base")
def step_impl(context):
    from CRMapp.models import Product, Category
    category = Category.objects.get(name="Keyboard")
    Product.objects.create(name="Genesis RX66", category=category, price=2)


@given("I have bought a product")
def step_impl(context):
    from CRMapp.models import Product, Category, Sale, WebUser
    from django.contrib.auth.models import User
    category = Category.objects.get(name="Keyboard")
    product = Product.objects.get(name="Genesis RX66", category=category)
    django_user = User.objects.get(id=1)
    client = WebUser.objects.get(django_user=django_user)
    Sale.objects.create(client=client, product=product)


@when("I visit my purchases page")
def step_impl(context):
    context.browser.visit(context.get_url('sales_list'))
    assert context.browser.is_text_present('PRODUCTS PURCHASED')


@when("I click the Incidence button")
def step_impl(context):
    context.browser.click_link_by_partial_href('/incidence/1')
    assert context.browser.is_text_present('Register an Incidence about the product')


@step("write and submit the incidence")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])
    browser.choose('category', 'The product arrived broken')
    form = context.browser.find_by_id('incidence-form')
    form.find_by_value('Submit').first.click()


@then("I see that the incidence is registered")
def step_impl(context):
    from CRMapp.models import Incidence
    assert context.browser.is_text_present('Incidence correctly submitted')
    incidence = Incidence.objects.get(id=1)
    assert incidence.explanation == "My thing is very broken"