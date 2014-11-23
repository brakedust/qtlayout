from setuptools import setup
import sys

setup(
    name='qt_easy_layout',
    version = '1.0.1',
    description='Provides convenience functions for easier layout of PyQt and PySide widgets',
    author='Brad Campbell',
    url='https://github.com/brakedust/qt_easy_layout',
    author_email='blc.77@verizon.net',
    package_dir = {'': ''},
    packages = ['qt_easy_layout'],
    keywords = ["Qt", "PyQt", "PySide", "gui"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License, Version 2.0",
        "Operating System :: OS Independent"
    ]
)