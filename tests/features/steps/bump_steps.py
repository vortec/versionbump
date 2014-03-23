from behave import *
from versionbump import VersionBump

@given('the version {version}')
def step_impl(context, version):
    context.versionbump = VersionBump(version)

@when('we bump {level}')
def step_impl(context, level):
    context.versionbump.bump(level)

@then('version is {version}')
def step_impl(context, version):
    context.versionbump.get() == version

@then('{level} is {number:d}')
def step_impl(context, level, number):
    assert context.versionbump.get(level) == number
