# Robyn Baumann
# AST4762 P7 and HW10
# Fri Nov 6, 2026

# import necessary libraries
import os
import numpy as np
from hw9_rab import *
from hw10_rab_support_functions import apphot
import gaussian as g

# Start Practicum 7:
print('\nPracticum 7:\n')

# problem 1 was write the function, now on to problem 2: 
print('Problem 2:')

# save info to test
sig    = 2
r      = 6
inr    = 7
outr   = 10
size   = 21
center = size / 2

# create gaussian
coord = np.indices((size, size))
obj1  = g.gaussian(coord, sig, (center, center))

# pass to apphot
test_appot = apphot(obj1, None, r, inr, outr, (center, center))

# print results
print('Test Flux: {:.6f}'.format(test_appot[0]))
print('Test Average sky: {:.6f}'.format(test_appot[1]))
print('Test Number of Bad Pixels: {0:2d}'.format(test_appot[2]))

# we got a flux near 1 and an average sky near 0, which is to 
# be expected from a standard Gaussian function without noise