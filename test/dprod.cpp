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