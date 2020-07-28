import timeit
from dprod import dprod
from pythran_ext.dprod import dprod as dprod_pythran
from cython_ext.dprod import dprod as dprod_cython
from nuitka_ext.dprod import dprod as dprod_nuitka
from pybind11_ext.dprod import dprod as dprod_pybind11

import numpy as np
from IPython import embed

x = [float(i) for i in range(100000)]
y = [float(i) for i in range(100000)]
xarr = np.asarray(x)
yarr = np.asarray(y)
num = 1000

duration = timeit.timeit("dprod(x, y)", globals=globals(), number=num)
print(f"pure python version, average time: {duration/num * 1000} ms")

duration = timeit.timeit("xarr@ yarr", globals=globals(), number=num)
print(f"numpy version, average time: {duration/num * 1000} ms")

duration = timeit.timeit("dprod_pythran(xarr, yarr)", globals=globals(), number=num)
print(f"pythran version, average time: {duration/num * 1000} ms")

duration = timeit.timeit("dprod_cython(xarr, yarr)",
                         globals=globals(), number=num)
print(f"cython version, average time: {duration/num * 1000} ms")

duration = timeit.timeit("dprod_nuitka(x, y)", globals=globals(), number=num)
print(f"nuitka version, average time: {duration/num * 1000} ms")

duration = timeit.timeit("dprod_pybind11(xarr, yarr)",
                         globals=globals(), number=num)
print(f"pybind11 version, average time: {duration/num * 1000} ms")
embed()
