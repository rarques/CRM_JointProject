from behave import *

use_step_matcher("re")


@given("The user visits the register page")
def step_impl(context):
    context.browser.visit(context.get_url('register'))
    title = context.browser.find_by_tag("h2")
    assert title.text == 'Register as a Person or as a Company'


@given("I'm not registered")
def step_impl(context):
    pass


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


@step("I submit the form")
def step_impl(context):
    form = context.browser.find_by_id('person-registration-form')
    form.find_by_value('Submit').first.click()


@then("I'm redirected to my profile page")
def step_impl(context):
    assert context.browser.is_text_present("Profile")


@given("I'm registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I get an error telling me I'm registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I fill the form with invalid information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I get an error telling me the wrong information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
