def factorial(x):
    # Basic example of a python function, which defines
    # python-like operations and control flow on defined c types

    m = x

    if x <= 1:
        return 1
    else:
        for i in range(1, x):
            m = m * i
        return m
