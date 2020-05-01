from cython_lib import c_hello, factorial as cython_factorial
from python_func import factorial as python_factorial
import time

if __name__ == "__main__":

    # c_hello() The c method

    t = time.time()
    r = cython_factorial(99999)
    print("[+] cython finished :", time.time() - t, "s")

    t = time.time()
    r = python_factorial(99999)
    print("[+] python finished :", time.time() - t, "s")
    print()
