from cython cimport boundscheck, wraparound

@boundscheck(False)
@wraparound(False)
def dprod(double[:] l0, double[:] l1):
    cdef:
        int n, i
        double r
    n = l0.shape[0]
    r = 0
    for i in range(n):
        r += l0[i] * l1[i]
    return r