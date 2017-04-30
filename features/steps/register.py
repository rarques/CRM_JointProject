from behave import *

use_step_matcher("re")


@given("The user visits the register page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("I'm not registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I fill the form with valid information")
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


@then("I receive an email confirmation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I accept the confirmation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


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
