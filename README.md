cython-lib-template
=======================

A small template that wrap C code into python using [cython](http://cython.org/), and integrate the extensions into an installable module. Developed around python 3.x.

[A cython pyx file](cython_lib/wrapped.pyx) is included that implements a few C functions which can accept
and return standard
python data types and numpy ndarrays. These are compiled, wrapped, and
integrated into the module using a standard [setup.py](setup.py) script.

In addition to concrete examples of cython syntax, this repo also illustrates
a working project structure with a working setup.py configuration (using setuptools)
for Python projects with C extension modules, along with basic unit tests
(together with a working Travis-CI config).

## Build the lib

First, install cython (using pip or from a package manager) if you
don't already have them. `pip install cython`

Then just run `python setup.py develop` to build the project in-place.

The module (with its wrapped C functions `c_hello`) will then be importable in python:
```shell-script
>>> from cython_lib import c_hello, factorial
```

## Wrapped example functions

2 examples functions are defined in [wrapped.pyx](cython_example_proj/wrapped.pyx):

- A direct wrapping of a simple C "hello world" function, implemented in [cfunc.c](cython_example_proj/lib/cfunc.c)
- A C function to compute the factorial of a python integer, built using
    Cython syntax.

# Benchmarks

For a quick benchmark of the two ndarray functions listed, run `python3 test_lib.py`.

```
$ python3 test_lib.py
[+] cython finished : 0.0001804828643798828 s
[+] python finished : 2.987328052520752 s
```
