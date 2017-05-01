from behave import *

use_step_matcher("re")


@given("I'm not registered")
def step_impl(context):
    pass


@step("I visit the register as person page")
def step_impl(context):
    context.browser.visit(context.get_url('register_person'))
    title = context.browser.find_by_tag("h2")
    assert title.text == 'Register as Person'


@step("I visit the register as company page")
def step_impl(context):
    context.browser.visit(context.get_url('register_company'))
    title = context.browser.find_by_tag("h2")
    assert title.text == 'Register as Company'


@when("I fill the form's basic fields")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I fill the form's specific fields")
def step_impl(context):
    pass
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I submit the form")
def step_impl(context):
    form = context.browser.find_by_id('registration-form')
    form.find_by_value('Submit').first.click()


@then("I'm redirected to my profile page")
def step_impl(context):
    raise NotImplementedError("Not implemented")


@step("I see my personal information")
def step_impl(context):
    raise NotImplementedError("Not implemented")


@given("I'm registered")
def step_impl(context):
    raise NotImplementedError("Not implemented")


@then("I get an error telling me I'm registered")
def step_impl(context):
    raise NotImplementedError("Not implemented")


@when("I fill the form with invalid information")
def step_impl(context):
    raise NotImplementedError("Not implemented")


@then("I get an error telling me the wrong information")
def step_impl(context):
    raise NotImplementedError("Not implemented")
