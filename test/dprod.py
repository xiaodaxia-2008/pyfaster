##############################################
# from typing import List
# # pure python version
# def dprod(l0: List[float], l1: List[float]) -> float:
#     n: int = len(l0)
#     r: float = 0
#     for i in range(n):
#         r += l0[i] * l1[i]
#     return r

##############################################

# pythran export dprod(float64[:], float[:])
def dprod(l0, l1):
    n = len(l0)
    r = 0
    for i in range(n):
        r += l0[i] * l1[i]
    return r

##############################################
# for numba test
# from numba import njit

# @njit
# def dprod1(l0, l1):
#     n = l0.shape[0]
#     r = 0
#     for i in range(n):
#         r += l0[i] * l1[i]
#     return r

##############################################


# if __name__ == "__main__":
#     import timeit
#     import numpy as np
#     x = [float(i) for i in range(100000)]
#     y = [float(i) for i in range(100000)]
#     xarr = np.asarray(x)
#     yarr = np.asarray(y)
#     num = 1000
#     duration = timeit.timeit("dprod(x, y)", globals=globals(), number=num)
#     print(f"pure python version, average time: {duration/num * 1000} ms")

#     dprod1(xarr, yarr)
#     duration = timeit.timeit("dprod1(xarr, yarr)",
#                              globals=globals(), number=num)
#     print(f"numba version, average time: {duration/num * 1000} ms")

#     duration = timeit.timeit("np.dot(xarr, yarr)",
#                              globals=globals(), number=num)
#     print(f"numpy version, average time: {duration/num * 1000} ms")
