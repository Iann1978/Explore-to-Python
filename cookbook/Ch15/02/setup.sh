python setup.py build_ext --inplace

tmppath=`pwd`
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$tmppath
unset tmppath
