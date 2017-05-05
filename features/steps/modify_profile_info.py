from behave import *

use_step_matcher("re")


@given("I am registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    from CRMapp.models import WebUser, UserAsPerson, UserAsCompany
    from django.contrib.auth.models import User
    user1 = User.objects.create(username='used_name')
    user2 = User.objects.create(username='padre')
    web_user1 = WebUser.objects.create(django_user=user1, country="Spain", province="Lleida",
                                       city="Cervera", zip_code=25200,
                                       street="Ramon Balcells n2", phone=288)
    web_user2 = WebUser.objects.create(django_user=user2, country="Spain", province="Lleida",
                                       city="Cervera", zip_code=25200,
                                       street="Ramon Balcells n2", phone=288)
    UserAsPerson.objects.create(web_user=web_user1, DNI="312W")
    UserAsCompany.objects.create(web_user=web_user2, CIF="12w2")


@step("I visit the modify as person page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('modify_person'))


@when("I change the form fields that interest me")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I submit the modify person form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    form = context.browser.find_by_id('modify_person_form')
    form.find_by_value('Apply').first.click()


@then("I am redirected to my profile page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Exists a UserAsPerson with DNI = "45236834T"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    from CRMapp.models import UserAsPerson
    assert UserAsPerson.objects.filter(DNI='45236834T').exists()


@when("Fields I've tried to modify contain invalid information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I get an error telling me the invalid information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I visit the modify as company page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('modify_company'))


@step("I submit the modify company form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    form = context.browser.find_by_id('modify_company_form')
    form.find_by_value('Apply').first.click()


@step('Exists a UserAsCompany with CIF = "E43576214"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    from CRMapp.models import UserAsCompany
    assert UserAsCompany.objects.filter(CIF='E43576214').exists()


@step("I am logged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass