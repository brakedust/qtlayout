from setuptools import setup
import sys

setup(
    name='qt_easy_layout',
    version = '1.0',
    description='Provides convenience functions for easier layout of PyQt and PySide widgets',
    author='brakedust',
    url='https://github.com/brakedust/qt_easy_layout',
    author_email='',

    package_dir = {'': 'qt_easy_layout'},
    packages = ['qt_easy_layout'],
    keywords = ["Qt", "PyQt", "PySide", "gui"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent"
    ]
)