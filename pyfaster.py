#!/usr/bin/python3

import os
import sys
import argparse

src_dir = os.path.dirname(__file__)

parser = argparse.ArgumentParser(
    description="Convert python3 code to cpp code using 11l or cython or pythran")
parser.add_argument("-l", "--l11", action="store_true",
                    help="using 11l")
parser.add_argument("-c", "--cython", action="store_true",
                    help="using cython")
parser.add_argument("-p", "--pythran", action="store_true",
                    help="using pythran")
parser.add_argument("-n", "--nuitka", action="store_true",
                    help="using nuitka")
parser.add_argument("-d", "--pybind11", action="store_true",
                    help="using pybind11")
parser.add_argument("src")

args = parser.parse_args()
if args.src:
    src = args.src
    filename, ext = os.path.splitext(os.path.basename(src))
    filepath = os.path.dirname(src)

else:
    print("using 'python3 py2cpp.py [-l/c/p/d] src'")

if args.l11:
    # use 11l
    os.makedirs(os.path.join(filepath, "l11_ext"), exist_ok=True)
    os.system("{}/11l/11l {}".format(src_dir, src))
    os.chdir(filepath)
    os.system("mv {f}.11l {f}.cpp {f} ./l11_ext/".format(f=filename))
elif args.cython:
    # use cython
    filepath = os.path.join(filepath, "cython_ext")
    os.makedirs(filepath, exist_ok=True)
    filename = os.path.join(filepath, filename)
    os.system("cython --cplus -p -3 -a {} -o {}.cpp".format(src, filename))
    os.system("g++ `python3-config --cflags --ldflags` -O3 --shared -fPIC -o {}`python3-config --extension-suffix` {}.cpp".format(filename, filename))
elif args.pythran:
    # use pythran
    filepath = os.path.join(filepath, "pythran_ext")
    os.makedirs(filepath, exist_ok=True)
    filename = os.path.join(filepath, filename)
    os.system("pythran -w -o {}`python3-config --extension-suffix` {}".format(
        filename, src))
elif args.nuitka:
    # use nuitka
    filepath = os.path.join(filepath, "nuitka_ext")
    os.makedirs(filepath, exist_ok=True)
    filename = os.path.join(filepath, filename)
    # to a python module
    os.system("python3 -m nuitka --module --output-dir {} {}".format(filepath, src))
    # to a standalone executable program
    # os.system("python3 -m nuitka --output-dir {} {}".format(filepath, src))
elif args.pybind11:
    # use pybind11
    import pybind11
    pybind11_includes = pybind11.get_include()
    filepath = os.path.join(filepath, "pybind11_ext")
    os.makedirs(filepath, exist_ok=True)
    filename = os.path.join(filepath, filename)
    cmd = ("g++ `python3-config --cflags --ldflags` -I{} -O3 --shared -fPIC -o {}`python3-config --extension-suffix` {}".format(pybind11_includes, filename, src))
    os.system(cmd)
else:
    print("using 'python3 py2cpp.py [-l/c/p] src'")
