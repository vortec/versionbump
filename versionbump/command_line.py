import argparse
from .filebump import FileBump
from .versionbump import VersionBump

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--current', required=True,
                    help='Assume current version. (required)')
parser.add_argument('-l', '--label', default=None,
                    help='Pre-release label.')
parser.add_argument('-q', '--quiet', default=False, action='store_true',
                    help='Don\'t write anything to stdout.')
parser.add_argument('-i', '--ignore', default=False, action='store_true',
                    help='Ignore invalid files.')
parser.add_argument('level', choices=['major', 'minor', 'patch', 'pre'])
parser.add_argument('file', nargs='*')
args = parser.parse_args()


def main():
    current_version = args.current
    level = args.level
    label = args.label

    vb = VersionBump(current_version)
    vb.bump(level, label)

    for filename in args.file:
        fo = open(filename, 'r+')
        try:
            fb = FileBump(fo, current_version)
            fb.bump(level)
        except ValueError:
            if args.ignore:
                continue
            else:
                raise

    new_version = vb.get()
    _output(new_version)
    raise SystemExit(0)


def _output(text):
    if not args.quiet:
        print(text)
