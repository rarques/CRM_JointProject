from behave import *

use_step_matcher("re")


@given("I have bought a product")
def step_impl(context):
    pass


@when("I click the Incidence button")
def step_impl(context):
    pass


@step("write and submit the incidence")
def step_impl(context):
    pass


@then("I see that the incidence is registered")
def step_impl(context):
    pass