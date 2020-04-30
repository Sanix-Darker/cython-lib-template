from setuptools import setup, Extension
from Cython.Distutils import build_ext

NAME = "cython-lib-template"
VERSION = "0.1"
DESCR = "A small template project that shows how to wrap C/C++ code into python using Cython"
URL = "https://github.com/sanix-darker"
REQUIRES = ['cython']

AUTHOR = "Sanix-darker"
EMAIL = "s4nixd@gmail.com"

LICENSE = "Apache 2.0"

SRC_DIR = "cython_lib"
PACKAGES = [SRC_DIR]
