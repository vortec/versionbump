from temp_file import make_temp_file, get_temp_file


@given(u'a file that contains {text}')
def step_impl(context, text):
    fp = make_temp_file(context)
    with open(fp, 'w') as fo:
        fo.write(text)


@given(u'a file named {filename} that contains {text}')
def step_impl(context, filename, text):
    fp = make_temp_file(context, filename)
    with open(fp, 'w') as fo:
        fo.write(text)


@given(u'an empty file')
def step_impl(context):
    make_temp_file(context)


@then(u'the file contains {text}')
def step_impl(context, text):
    fp = get_temp_file(context)
    with open(fp, 'r') as fo:
        content = fo.read()
    assert text in content


@then(u'the file {filename} contains {text}')
def step_impl(context, filename, text):
    fp = get_temp_file(context, filename)
    with open(fp, 'r') as fo:
        content = fo.read()
    assert text in content


@then(u'the file is empty')
def step_impl(context):
    fp = get_temp_file(context)
    with open(fp, 'r') as fo:
        content = fo.read()
    assert content == ''
