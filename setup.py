# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ahmetdal'

from setuptools import setup, find_packages

entrypoints = {}

console_scripts = entrypoints['console_scripts'] = [
    'update_version = src.update_version:main',
    'current_version = src.current_version:main',
]

# -*- %%% -*-

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='version-upgrader',
    version='0.1.0',
    description="Version upgrader in all spesific files like setup.py, package.json, bower.json etc.",
    author="Ahmet DAL",
    author_email="ceahmetdal@gmail.com",
    url="https://github.com/javrasya/version-upgrader",
    platforms=['any'],
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ],
    include_package_data=True,
    entry_points=entrypoints,
    long_description=long_description,
)