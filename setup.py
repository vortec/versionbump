# -*- coding: utf-8 -*-
#!/usr/bin/env python

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command


description = 'Generate version strings based on semantic versioning rules.'
long_description = str(open('README.rst', 'rb').read())

setup(name='versionbump',
      version='1.1.0',
      license='MIT',
      author='Fabian Kochem',
      url='https://github.com/vortec/versionbump',
      description=description,
      long_description=long_description,
      packages=find_packages(),
      install_requires=[

      ],
      entry_points={
          'console_scripts': [
            'versionbump = versionbump.command_line:main',
          ]
      },
      classifiers=(
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
    ),
)
