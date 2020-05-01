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

ext_1 = Extension(SRC_DIR + ".wrapped",
                  [SRC_DIR + "/lib/cfunc.c", SRC_DIR + "/wrapped.pyx"],
                  libraries=[],
                  include_dirs=[])


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )
