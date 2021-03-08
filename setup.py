#!/usr/bin/env python

from setuptools import setup, find_packages

name = "pyupdi-tomaz"

setup(
    name = name,
    version = '1.0.0',
    url = 'https://github.com/avian2/pyupdi',
    entry_points = {
        'console_scripts': ['pyupdi=updi:_main'],
    },
    packages = find_packages(),
    python_requires = '>3',
    install_requires = ['intelhex', 'pyserial'],
)
