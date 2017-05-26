from __future__ import print_function
from behave import *

use_step_matcher("re")


@given("I am interested in a category")
def step_impl(context):
    pass


@step("I am registered")
def step_impl(context):
    from django.contrib.auth.models import User
    from CRMapp.models import WebUser
    from CRMapp.models import CategoryPerUser
    from CRMapp.models import Category
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info = row[heading]
    user = User.objects.create(username=user_info[0], password=user_info[1])
    web_user = WebUser.objects.create(django_user=user, country="Mordor",
                                      province="Gorgoroth",
                                      city="Barad dur", zip_code=25200,
                                      street="Ramon Balcells n2", phone=288)
    CategoryPerUser.objects.create(user=web_user, category=Category.objects.create(name=user_info[2]))


@step("I log in")
def step_impl(context):
    from CRMapp.models import WebUser
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_id('login_form').first
    web_user = WebUser.objects.get(country="Mordor")
    context.browser.fill('username', web_user.django_user.username)
    context.browser.fill('password', web_user.django_user.password)
    form.find_by_value('login').first.click()


@step("There are products related with my category")
def step_impl(context):
    from CRMapp.models import Product
    from CRMapp.models import Category
    product_info = []
    for row in context.table:
        for heading in row.headings:
            product_info = row[heading]

    Product.objects.create(name=product_info[0], category=Category.objects.create(name=product_info[1]),
                           price=10)


@step("So I get a recommendation")
def step_impl(context):
    pass


@step("I go to the homepage")
def step_impl(context):
    context.browser.find_by_tag('li').find_by_tag('a').click()
