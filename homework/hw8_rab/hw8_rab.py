# Robyn Baumann
# AST4762 HW8
# October, 14, 2026

# import needed libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from hw8_rab_support_functions import normmedcomb, skycormednorm
from hw6_rab import *
import pwd
import time 

# Practicum 5 problem 1:
print('\nPracticum 5:')
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

# Start HW 8:
print('\nHomework 8:')

# problem 1: in log

# problem 2:
print('Problem 2:')

# create array to hold sky subtracted data
sky_sub_dat = np.zeros_like(objs, dtype=np.float64)

for i in range(len(objs)):
    sky_sub_dat[i] = skycormednorm(objs[i], norm_data, norm_region)

# write header for the sky frame
head["History"] = ('File Created. ' + time.strftime('%a %b %d %H:%M:%S %Z %Y ') \
                   + username)

# write fits file for last object in sky_sub_dat
fits.writeto('stars_13s_9_nosky.fits', sky_sub_dat[-1], header = head, overwrite=True)

# print pixel value
print('Pixel [217,184] of the sky array is', sky_sub_dat[-1, 217,184])
