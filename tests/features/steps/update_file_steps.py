from behave import *
from StringIO import StringIO
from versionbump import FileBump

@given(u'xa text loaded into a file')
def step_impl(context):
    context.fo = StringIO()
    context.fo.write(context.text)
    context.fo.seek(0)

@when(u'xwe parse the file assuming it contains {version}')
def step_impl(context, version):
    context.fb = FileBump(context.fo, version)

@when(u'xwe file bump {level}')
def step_impl(context, level):
    context.fb.bump(level)

@then(u'xthe file contains {version}')
def step_impl(context, version):
    context.fo.seek(0)
    assert version in context.fo.read()
