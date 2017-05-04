from behave import *

use_step_matcher("re")


@given("I'm registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    from django.contrib.auth.models import User
    User.objects.create(username='used_name')


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


@then("I'm redirected to my profile page")
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