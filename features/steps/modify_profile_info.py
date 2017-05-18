from behave import *

use_step_matcher("re")


@given("I am registered as person")
def step_impl(context):
    from CRMapp.models import WebUser, UserAsPerson
    from django.contrib.auth.models import User
    user1 = User.objects.create(username='used_name', email='used_name')
    user1.set_password('patatapatata1')
    web_user1 = WebUser.objects.create(django_user=user1, country="Spain", province="Lleida",
                                       city="Cervera", zip_code=25200,
                                       street="Ramon Balcells n2", phone=288)
    user_as_person1 = UserAsPerson.objects.create(web_user=web_user1, DNI="312W")
    user1.save()
    web_user1.save()
    user_as_person1.save()


@given("I am registered as company")
def step_impl(context):
    from CRMapp.models import WebUser, UserAsCompany
    from django.contrib.auth.models import User
    user2 = User.objects.create(username='padre', email='padre@padre.padre')
    user2.set_password('patata1')
    web_user2 = WebUser.objects.create(django_user=user2, country="Spain", province="Lleida",
                                       city="Cervera", zip_code=25200,
                                       street="Ramon Balcells n2", phone=288)
    user_as_company1 = UserAsCompany.objects.create(web_user=web_user2, CIF="12w2")
    user2.save()
    web_user2.save()
    user_as_company1.save()


@step("I visit the modify as person page")
def step_impl(context):
    context.browser.visit(context.get_url('modify_person'))


@when("I change the form fields that interest me")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I submit the modify person form")
def step_impl(context):
    form = context.browser.find_by_id('modify_person_form')
    form.find_by_value('Apply').first.click()


@then("I am redirected to my profile page")
def step_impl(context):
    pass


@step('Exists a UserAsPerson with DNI = "45236834T"')
def step_impl(context):
    from CRMapp.models import UserAsPerson
    assert UserAsPerson.objects.filter(DNI='45236834T').exists()


@when("Fields I've tried to modify contain invalid information")
def step_impl(context):
    pass


@then("I get an error telling me the invalid information")
def step_impl(context):
    pass


@step("I visit the modify as company page")
def step_impl(context):
    context.browser.visit(context.get_url('modify_company'))


@step("I submit the modify company form")
def step_impl(context):
    form = context.browser.find_by_id('modify_company_form')
    form.find_by_value('Apply').first.click()


@step('Exists a UserAsCompany with CIF = "E43576214"')
def step_impl(context):
    from CRMapp.models import UserAsCompany
    assert UserAsCompany.objects.filter(CIF='E43576214').exists()


@step("I am logged as person")
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_id('login_form').first
    f = open('log.txt', 'w+')
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
            f.write('heading :' + heading + " " + row[heading] + '\n')
    form.find_by_value('login').first.click()


@step("I am logged as company")
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_id('login_form').first
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    form.find_by_value('login').first.click()
