# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ahmetdal'

from setuptools import setup, find_packages

entrypoints = {}

console_scripts = entrypoints['console_scripts'] = [
    'update_version = src.bin.update_version:main',
    'current_version = src.bin.current_version:main',
]

# -*- %%% -*-

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='version-upgrader',
    version='0.2.2',
    description="Version upgrader in all spesific files like setup.py, package.json, bower.json etc.",
    author="Ahmet DAL",
    author_email="ceahmetdal@gmail.com",
    url="https://github.com/javrasya/version-updater",
    platforms=['any'],
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'repoze.lru',
    ],
    include_package_data=True,
    entry_points=entrypoints,
    long_description=long_description
)
