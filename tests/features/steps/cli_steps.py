import subprocess

@given(u'we assume version {version}')
def step_impl(context, version):
    context.current_version = version

@when(u'we run bump {level}')
def step_impl(context, level):
    args = [
        'versionbump',
        '-a', context.current_version,
        level
    ] + list(context.cli_filenames)

    context.exit_code = subprocess.call(args)

@then(u'the exit code was {exit_code:d}')
def step_impl(context, exit_code):
    assert context.exit_code == exit_code
