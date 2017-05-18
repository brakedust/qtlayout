from setuptools import setup
import sys

setup(
    name='qtlayout',
    version = '1.0.1',
    description='Provides convenience functions for easier layout of PyQt and PySide widgets',
    author='Brad Campbell',
    url='https://github.com/brakedust/qtlayout',
    author_email='bradlcampbell@gmail.com',
    package_dir = {'': ''},
    packages = ['qtlayout'],
    keywords = ["Qt", "PyQt", "PySide", "gui"],
    reqruirements = ["qtpy"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License, Version 2.0",
        "Operating System :: OS Independent"
    ]
)
