# Robyn Baumann
# AST4762 HW8
# October, 14, 2026

# import needed libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from hw8_rab_support_functions import normmedcomb
from hw6_rab import *
import pwd
import time 

# Practicum 5 problem 1:
print('Practicum 5:')
print('Problem 3:')

# above, I imported the object array from hw6, so now pass it to the comb
norm_region = ((225, 225), (-225, -225))
norm_info   = normmedcomb(objs, norm_region)

# save factors and data to their own variable
norm_data    = norm_info[0]
norm_factors = norm_info[1]

# create header for new fits file
head            = fits.Header()
username        = pwd.getpwuid(os.getuid())[0]
head["HISTORY"] = ('Normalized Median Combination Method used to creat this file. ' \
                  + time.strftime('%a %b %d %H:%M:%S %Z %Y ') + username)

# write to a fits file
fits.writeto('sky_13s_mednorm.fits', norm_data, header = head, overwrite=True)


# print the normaliazation factors
print('Normalization Factors:')
print(norm_factors)
# I got: [10864. 11057. 10536. 10559. 11046. 10623.  9916.  9916.  9859.]

