# Robyn Buamann
# AST4762 P6 and HW9
# October 22, 2026

# import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from hw9_rab_support_functions import disk
from hw8_rab import *
from gaussian import fitgaussian
import pwd
import time 

# start practicum work:
print('\n Practicum 6:\n')

# start problem 1:
print('Problem1:')

# create test disk mask
test_disk = disk(6.2, (12.3, 14.5), (25, 30))

# save test disk
fits.writeto('disktest.fits', test_disk.astype(np.uint8), overwrite=True)

# check requested pixels:
print('The pixel [14, 14] is: ', test_disk[14, 14])
print('The pixel [2, 1] is: ',   test_disk [2, 1])

# start problem 2: 
print('\nProblem 2:')

# part a
# lists to store the data of lampon/lamp off data
lamp_on  = []
lamp_off = []

# populate the lists with loops
for filename in os.listdir(datadir):
    if 'k_lampon' in filename and filename.endswith(fext):
        lamp_on.append(filename)
    if 'k_lampoff' in filename and filename.endswith(fext):
        lamp_off.append(filename)

# sort the data to be alphabetical/number order
lamp_on.sort()
lamp_off.sort()

# save number of each file and size of file
n_on  = len(lamp_on)
n_off = len(lamp_off)
nx, ny = fits.getdata(datadir + lamp_on[0]).shape

# create arrays to hold data
lamp_on_arr  = np.zeros( (n_on, ny, nx),  dtype = np.float64 )
lamp_off_arr = np.zeros( (n_off, ny, nx), dtype = np.float64 )

#populate the arrays
for i in range(n_on):
    lamp_on_arr[i] = fits.getdata(datadir + lamp_on[i])

for i in range(n_off):
    lamp_off_arr[i] = fits.getdata(datadir + lamp_off[i])

# median combine the two 
lamp_on_med  = np.median(lamp_on_arr,  axis = 0)
lamp_off_med = np.median(lamp_off_arr, axis = 0)

# suptract the two
flat = lamp_on_med - lamp_off_med

#create normalization factor
flat_norm_reg = flat[norm_region[0][0]:norm_region[1][0],
                     norm_region[0][1]:norm_region[1][1]]

flat_factor   = np.median(flat_norm_reg)

# normalize
flat_norm = flat/flat_factor

# renew header
head["History"] = ('File Created. ' + time.strftime('%a %b %d %H:%M:%S %Z %Y ') \
                   + username)

#save to fits file
fits.writeto('flat.fits', flat_norm, header = head, overwrite=True)

# print the value of pixel index [217, 184]
print('Pixel [217,184] of the flat field is', flat_norm[217,184])

# part b: Apply the flat field to all the sky-subtracted object data
print('Number of zero pixels:', np.sum(flat_norm == 0))
#should we change those to NaN?
#flat_norm[flat_norm == 0] = np.nan
corr_sky = sky_sub_dat / flat_norm

# print the value of pixel index [217, 184]
print('Pixel [217,184] of the corrected sky frames are', corr_sky[:,217,184])

# write to fits file
fits.writeto('stars_13s_9_flat.fits', corr_sky[-1], header = head, overwrite=True)

# start of HW9:
print('\nHomework 9:')

# problem 2:
print('\nProblem 2:')

# initialize array to hold photometry data:
# Stellar photometry:
photometry = np.array( [ # yguess, xguess, width, cy, cx, star, sky
    # star 0
    [ [ 698,   512,    np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 0
      [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 1
      [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], # frame 2
    # star 1
    [ [ 668,   520,    np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 0
      [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 1
      [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], # frame 2
    # star 2
    [ [ 568,   283,    np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 0
      [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 1
      [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]  # frame 2
    ], dtype=float)

# save indices under what they rep
yguess, xguess, width, cy, cx, star, sky = 0, 1, 2, 3, 4, 5, 6

# created fits files for the 3 frames to be able to find star guesses
#fits.writeto('stars_13s_1_flat.fits', corr_sky[0], header = head, overwrite=True)
#fits.writeto('stars_13s_2_flat.fits', corr_sky[1], header = head, overwrite=True)
#fits.writeto('stars_13s_3_flat.fits', corr_sky[2], header = head, overwrite=True)

# Save guesses for star 0 of other frames
photometry[0,1,yguess] = 464
photometry[0,1,xguess] = 518
photometry[0,2,yguess] = 228
photometry[0,2,xguess] = 522

# calculate the offset of x and y
x_off_01 = photometry[0,0,xguess] - photometry[0,1,xguess]
y_off_01 = photometry[0,0,yguess] - photometry[0,1,yguess]
x_off_02 = photometry[0,0,xguess] - photometry[0,2,xguess]
y_off_02 = photometry[0,0,yguess] - photometry[0,2,yguess]

# find number of stars and frames from table itself
nstars, nframes, nparams = photometry.shape

# loop to add offset to other stars
for i in range(1, nstars):
    photometry[i,1,xguess] = photometry[i,0,xguess] - x_off_01
    photometry[i,1,yguess] = photometry[i,0,yguess] - y_off_01
    photometry[i,2,xguess] = photometry[i,0,xguess] - x_off_02
    photometry[i,2,yguess] = photometry[i,0,yguess] - y_off_02

# printed photometry table after calcs and compared it to
# the images in DS9, it seems to be good!
# print(photometry)

# start problem 3
print('\nProblem 3:')

# part a: use gaussian to get widths and locations of stars
# startwith a guess on the width, stars seem to be about 10 pixels wide, 
# so a width of 30, half of 15 should be good
halfwidth = 15

# loop to caluclate and pass to table
for k in range(nstars):
    for j in range(nframes):
        # range for Gaussian
        y0 = int(photometry[k,j,yguess] - halfwidth)
        y1 = int(photometry[k,j,yguess] + halfwidth)
        x0 = int(photometry[k,j,xguess] - halfwidth)
        x1 = int(photometry[k,j,xguess] + halfwidth)

        # create subarray copy
        sub = corr_sky[j][y0:y1, x0:x1].copy()

        # take median of subarray and subtract
        sub_med = np.median(sub)
        sub -= sub_med
        
        # first try was off, try making guesses to pass to gaussian:
        g_wid  = (3,3) #from visual inspection
        g_cent = (photometry[k, j, yguess] - y0,
                  photometry[k, j, xguess] - x0)
        g_h    = sub.max()
        g      = (g_wid, g_cent, g_h)

        # get gaussian fit, abrev of what was returned (see docstring for fitgaussian)
        wid, cent, h, err = fitgaussian(sub, guess=g)

        # fill in table
        photometry[k, j, width] = np.mean(np.abs(wid))
        photometry[k, j, cy]    = cent[0] + y0
        photometry[k, j, cx]    = cent[1] + x0

# print the new table
print('Photometry table:\n', photometry)

#this is what printed: 
#[[[698. 512. 1.00567655 698.6200605  512.38627249 nan nan]
#  [464. 518. 0.9746056  464.37328784 517.41685338 nan nan]
#  [228. 522. 1.13509715 228.43288141 521.93195395 nan nan]]
# [[668. 520. 1.04634846 667.88227563 520.22562706 nan nan]
#  [434. 526. 0.98219128 433.57877762 525.305009   nan nan]
#  [198. 530. 1.17421007 197.63680196 529.79168385 nan nan]]
# [[568. 283. 1.07702914 568.25822246 283.30273705 nan nan]
#  [334. 289. 0.9770288  333.95975008 288.36023236 nan nan]
#  [ 98. 293. 1.10883357  98.07114219 292.89930066 nan nan]]]
        
# part b: average of all widths
avg_width = np.mean(photometry[:,:, width])
print('\nThe average width is', avg_width, 'pixels.')

# multiple average width for data to use later
aperture_r  = 3 * avg_width
# I chose 2.5 because FWHM is about 2.5 sigma
inner_sky_r = 5 * avg_width
outer_sky_r = 8 * avg_width
# we want the sky far enough away from the star for it to not have 
# light from the star affecting it, but not so far that other factors
# could affet it
sub_size    = 15 * avg_width
# sub array needs to be biggest of the above so it can contain everything needed

