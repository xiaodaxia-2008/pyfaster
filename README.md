A toolkits to make your python faster easily with the following tools:
- [cython]()
- [numba]()
- [pythran]()
- [pybind11]()
- [nuitka]()
- [11l]()
- [pypy]()

### Requirements
There are some modules need to be installed.
```
python3 -m pip install nuitka pybind11 cython numba pythran
```

### Simple useage
Suppose you have a python scripy like:
```python
## test/dprod.py

def dprod(l0, l1):
    n = len(l0)
    r = 0
    for i in range(n):
        r += l0[i] * l1[i]
    return r
```
just simply run 
```shell
python pyfaster.py -n test/dprod.py
```
Then you will get a python extension module generated by pythran, which will runs faster.   

The option means:

- `-p` with `pythran`
- `-c` with `cython`
- `-n` with `nuitka`
- `-d` with `pybind11`
- `-l` with `11l`


### Advanced usage
Some tools need you to make a small modification of your python code, but never so much.   

#### pythran
To use `pythran`, you need add some directives like:
```python
## test/dprod.py for pythran

# pythran export dprod(float64[:], float[:])
def dprod(l0, l1):
    n = len(l0)
    r = 0
    for i in range(n):
        r += l0[i] * l1[i]
    return r
```

#### pybind11
To use `pybind11`, it is for you to write the `.cpp` file and wrapper code.
```c++
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;
using namespace py::literals;

double dprod(const double *l0, const double *l1, unsigned n)
{
    double r = 0;
    for (unsigned i = 0; i < n; ++i)
    {
        r += l0[i] * l1[i];
    }
    return r;
}

PYBIND11_MODULE(dprod, m)
{
    m.def("dprod", [](py::array_t<double> l0, py::array_t<double> l1) {
        py::buffer_info l0buf = l0.request(), l1buf = l1.request();
        return dprod((double *)l0buf.ptr, (double *)l1buf.ptr, l0buf.shape[0]);
    });
}
```

#### cython
To use cython, it's better to revise the code with cython grammar.
```python
## test/dprod.pyx

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
```