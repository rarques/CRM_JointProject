from behave import *

use_step_matcher("re")


@given("I'm registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I change the form fields that interest me")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I submit the form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I receive an email notification")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


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