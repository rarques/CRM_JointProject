from behave import *

use_step_matcher("re")


@given("There are product categories in the data base")
def step_impl(context):
    from CRMapp.models import Category
    Category.objects.create(name="Keyboard")
    Category.objects.create(name="Mouse")
    Category.objects.create(name="Graphic cards")


@given("I'm not registered")
def step_impl(context):
    pass


@step("I visit the register as person page")
def step_impl(context):
    context.browser.visit(context.get_url('register_person'))


@step("I visit the register as company page")
def step_impl(context):
    context.browser.visit(context.get_url('register_company'))


@when("I fill the form's basic fields")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I fill the form's specific fields")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I select the categories I'm interested in")
def step_impl(context):
    raise NotImplementedError


@step("I submit the form")
def step_impl(context):
    form = context.browser.find_by_id('registration-form')
    form.find_by_value('Submit').first.click()


@then("I'm redirected to my profile page")
def step_impl(context):
    pass
    # raise NotImplementedError("Not implemented")


@step("Exists a UserAsPerson with DNI = 12345678A")
def step_impl(context):
    from CRMapp.models import UserAsPerson
    assert UserAsPerson.objects.filter(DNI='12345678A').exists()


@step("Exists a UserAsCompany with CIF = 98765432Z")
def step_impl(context):
    from CRMapp.models import UserAsCompany
    assert UserAsCompany.objects.filter(CIF='98765432Z').exists()


@given("I'm registered")
def step_impl(context):
    from django.contrib.auth.models import User
    User.objects.create(username='used_name')


@then("I get an error telling me I'm registered")
def step_impl(context):
    browser = context.browser
    assert len(browser.find_by_css('.errorlist')) == 1
