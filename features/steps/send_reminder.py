from __future__ import print_function
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
    from datetime import timedelta, datetime
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info = row[heading]
    User.objects.create(username=user_info[0], password=user_info[1], last_login=(datetime.now() - timedelta(days=15)), email=user_info[3])


@step("I click the send button")
def step_impl(context):
    context.browser.find_by_tag('form').find_by_tag('input').click()


@then("I see the reminder sent page")
def step_impl(context):
    pass
