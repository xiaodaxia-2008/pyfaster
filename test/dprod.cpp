double dprod(const double *l0, const double *l1, unsigned n)
{
    double r = 0;
    for (unsigned i = 0; i < n; ++i)
    {
        r += l0[i] * l1[i];
    }
    return r;
}

// #include <pybind11/pybind11.h>
// #include <pybind11/numpy.h>

// namespace py = pybind11;
// using namespace py::literals;

// PYBIND11_MODULE(dprod, m)
// {
//     m.def("dprod", [](py::array_t<double> l0, py::array_t<double> l1) {
//         py::buffer_info l0buf = l0.request(), l1buf = l1.request();
//         return dprod((double *)l0buf.ptr, (double *)l1buf.ptr, l0buf.shape[0]);
//     });
// }

#include <vector>
#include <chrono>
#include <iostream>
#include <numeric>
int main()
{
    std::vector<double> l0(100000), l1(100000);
    std::iota(l0.begin(), l0.end(), 0);
    std::iota(l1.begin(), l1.end(), 0);
    auto t0 = std::chrono::high_resolution_clock::now();
    for (unsigned i = 0; i < 1000; ++i)
    {
        double r = dprod(l0.data(), l1.data(), l0.size());
    }
    auto t1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> duration = t1 - t0;
    std::cout << "average time: " << duration.count() / 1000 << " ms\n";
    return 0;
}