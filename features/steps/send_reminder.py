from behave import *

use_step_matcher("re")


@given("There are clients afk")
def step_impl(context):
    pass


@given("I am logged in")
def step_impl(context):
    from django.contrib.auth.models import User
    User.objects.create(username='jeypie', email='jeypie@pie.jey')


@step("I visit the send reminders page")
def step_impl(context):
    context.browser.visit(context.get_url('crm:client_reminder'))


@when("There is an afk client")
def step_impl(context):
    from django.contrib.auth.models import User
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info = row[heading]
    User.objects.create(username=user_info[0], password=user_info[1], email=user_info[2], last_login=user_info[3])


@step("I click the send button")
def step_impl(context):
    form = context.browser.find_by_id('Send')
    form.find_by_value('Send reminder to afk clients').first.click()


@then("I see the reminder sent page")
def step_impl(context):
    pass