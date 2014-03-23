# -*- coding: utf-8 -*-
#!/usr/bin/env python

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command

setup(name='versionbump',
      version='0.0.1',
      description='Bump versions based on semantic versioning rules',
      author='Fabian Kochem',
      packages=find_packages(),
      install_requires=[
          
      ],
)
