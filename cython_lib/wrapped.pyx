cimport cython

# To import external python library
# import numpy as np
# cimport numpy as np

cdef extern from "lib/cfunc.h":
    # Imports definitions from a c header file
    # Corresponding source file (cfunc.c) must be added to
    # the extension definition in setup.py for proper compiling & linking

    void hello()


cpdef c_hello():
    # Exposes a c function to python

    hello()

# decorator turns off bounds-checking for speed
@cython.boundscheck(False)
cpdef factorial(int x):
    # Basic example of a cython function, which defines
    # python-like operations and control flow on defined c types

    cdef int m = x
    cdef unsigned int i

    if x <= 1:
        return 1
    else:
        for i in range(1, x):
            m = m * i
        return m
