import subprocess


@given(u'we use parameter {parameter}')
def step_impl(context, parameter):
    context.cli_args.append(*parameter.split(' '))


@given(u'we assume version {version}')
def step_impl(context, version):
    context.cli_args.extend(['-c', version])


@given(u'we asusume label {label}')
def step_impl(context, label):
    context.cli_args.extend(['-l', label])


@when(u'we run versionbump {level}')
def step_impl(context, level):
    args = ['versionbump']
    args.extend(context.cli_args)
    args.append(level)
    args.extend(list(context.cli_filenames))

    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               universal_newlines=True)
    context.process_output = process.communicate()[0].strip()
    context.process_exit_code = process.poll()


@then(u'the output was {text}')
def step_impl(context, text):
    assert context.process_output == text


@then(u'there was no output')
def step_impl(context):
    assert context.process_output == ''


@then(u'the exit code was {exit_code:d}')
def step_impl(context, exit_code):
    assert context.process_exit_code == exit_code
