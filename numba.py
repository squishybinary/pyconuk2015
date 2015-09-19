#First talk in Science track at Pycon2015

#numbda tutorial is in tutorial.zip 

#powerpoint is in pyconuk folder

#command list for tutorial setup:
#    conda env create -f=environment.yml
#    source activate pyconuk-numba
#    ipython notebook

from numba import jit

@jit
def add(x, y):
    return x + y

add(1, 2)
