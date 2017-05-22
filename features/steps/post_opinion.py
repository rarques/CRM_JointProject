from behave import *

use_step_matcher("re")


@step("I click the Opinion button")
def step_impl(context):
    context.browser.click_link_by_partial_href('/opinion/1')
    assert context.browser.is_text_present('Tell us your opinion about this product:')


@step("write and submit the opinion")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])
    form = context.browser.find_by_id('opinion-form')
    form.find_by_value('Submit').first.click()


@then("I see that the opinion is posted")
def step_impl(context):
    from CRMapp.models import Opinion
    assert context.browser.is_text_present('Opinion correctly submitted')
    opinion = Opinion.objects.get(id=1)
    assert opinion.comment == "Good customer service"
