============
versionbump
============

Helper tool to generate version strings based on semantic versioning rules. It provides a shell command for using in bash scripts and comes with Python classes which you can integrate in your code.


Installation
============

::

    pip install versionbump


Usage
=====

::

    usage: versionbump [-h] -c CURRENT [-q] [-i]
                   {major,minor,patch} [file [file ...]]

Arguments
+++++++++
- ``-c`` / ``--current``: Assume current version. (required)
- ``-h`` / ``--help``: Print help text and exit.
- ``-q`` / ``--quiet``: Don't write anything to stdout.
- ``-i`` / ``--ignore``: Ignore invalid files

Increase version
++++++++++++++++

::

    $ versionbump -c 0.1.2 patch
    0.1.3

Replace version in file(s)
++++++++++++++++++++++++++

::

    $ cat version.txt
    Current version: 0.1.2
    $ versionbump -c 0.1.2 minor version.txt
    0.1.3
    $ cat version.txt
    Current version: 0.1.3

If you want to replace the version string in more than one file, just pass them to ``versionbump`` aswell. Example:

::

    $ versionbump -c 0.1.2 major file1.txt file2.txt file3.txt

Python library
==============

VersionBump
+++++++++++

::

    from versionbump import VersionBump
    vb = VersionBump('2.0.1')
    vb.bump()  ## default value: 'patch'
    print vb.get() ## 2.0.2
    print vb.get('patch')  ## 2

FileBump
++++++++

::

    from versionbump import FileBump
    fo = open('version.txt', 'r+')
    fb = FileBump(fo, '2.0.1')
    vb.bump()  ## default value: 'patch', writes to file
    print vb.get() ## 2.0.2
    print vb.get('patch')  ## 2
