#include "/home/xiaodaxia/Documents/py2cpp/11l/_11l_to_cpp/11l.hpp"

double dprod(Array<double> &l0, Array<double> &l1)
{
    int n = l0.len();
    double r = 0;
    for (auto i : range_el(0, n))
        r += l0[i] * l1[i];
    return r;
}

int main()
{
}
