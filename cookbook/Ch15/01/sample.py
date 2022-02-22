# sample.py

import ctypes
import os

# Try to locate the .so file in the same directory as this file
_file = 'libsample.so'
_path = os.path.join(*(os.path.split(__file__)[:-1]+(_file,)))
print(_path)

_mod = ctypes.cdll.LoadLibrary(_path)


# int gcd(int int)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int
