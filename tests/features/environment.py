from distutils.util import strtobool as _bool
import os
import pdb
import shutil
import tempfile


def before_scenario(context, scenario):
    context.cli_args = []
    context.cli_filenames = set()
    context.process_output = None
    context.process_exit_code = None
    context.test_data_folder = tempfile.mkdtemp()

def after_scenario(context, scenario):
    shutil.rmtree(context.test_data_folder)


debug_flag = _bool(os.environ.get("DEBUG", "no"))
def after_step(context, step):
    if debug_flag and step.status == "failed":
        pdb.post_mortem(step.exc_traceback)
