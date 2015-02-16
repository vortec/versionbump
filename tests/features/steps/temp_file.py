"""
Not using Python's built-in "tempfile" module because it
doesn't allow custom file names.
"""

import os


def make_temp_file(context, filename=None):
    folder = context.test_data_folder
    if not filename:
        filename = 'default'
    fp = os.path.join(folder, filename)
    open(fp, 'a').close()
    context.cli_filenames.add(fp)
    return fp


def get_temp_file(context, filename=None):
    folder = context.test_data_folder
    if not filename:
        filename = 'default'
    return os.path.join(folder, filename)
