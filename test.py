from cython_lib import test
import time

if __name__ == "__main__":
    t = time.time()
 
    print("cython finished :", time.time() - t, "s")

    t = time.time()
 
    print("python finished :", time.time() - t, "s")
    print()
