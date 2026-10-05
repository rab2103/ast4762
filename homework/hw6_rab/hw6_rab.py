# Robyn Baumann
# AST4762 HW6
# Oct 1 2026

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits

# Practicum 4 said to work in this file:
# Problem 2 in P4:
print('Problem 2 on P4:')

# part a: variables for file directory and extension
datadir = 'hw6_data/'
fext    = '.fits'

# part b: lists to store data
objfile = []
darkfile = []

# populate the lists with loops
for filename in os.listdir(datadir):
    if 'stars_13s_' in filename and filename.endswith(fext):
        objfile.append(filename)
    if 'dark_13s_' in filename  and filename.endswith(fext):
        darkfile.append(filename)

# sort the data to be alphabetical/number order
objfile.sort()
darkfile.sort()

# part c: print datadir, fext
print('\n')
print('datadir is: ', datadir)
print('fext is: ',    fext)

# print the last elements of objfile and darkfile
print('\n')
print('Last element in objfile is: ',  objfile[-1])
print('Last element in darkfile is: ', darkfile[-1])

# part d: read one of the objects and assign to x and y
nx, ny = fits.getdata(datadir + objfile[0]).shape

# print the size of the files
print('\n')
print('Number of x-data points in objfile[0]:', nx)
print('Number of y-data points in objfile[0]:', ny)

# part e: save number of objfiles and darkfiles
nobj  = len(objfile)
ndark = len(darkfile)

# print the numebr of files
print('\n')
print('Number of Object Files:', nobj)
print('Number of Dark Files:',   ndark)

# problem 3 in P4:
print('\nProblem 3 in P4:\n')

# part a: create arrays to hold data
objarr  = np.zeros( (nobj, ny, nx), dtype = np.float64 )
darkarr = np.zeros( (ndark, ny, nx), dtype = np.float64 )

#print the chape of the arrays:
print('Shape of the Object Array:', objarr.shape)
print('Shape of the Dark Array:', darkarr.shape)

# part b: populate the array anad header list for object files
for i in range(nobj):
    objarr[i] = fits.getdata(datadir + objfile[i])

# store last header:
objhead = fits.getheader(datadir + objfile[nobj-1])

# populate the array anad header list for dark files
for i in range(ndark):
    darkarr[i] = fits.getdata(datadir + darkfile[i])

# store last header:
darkhead = fits.getheader(datadir + darkfile[ndark-1])

# print the date of object observations:
print('\nThe date the observations for the object file were made is', objhead['DATE-OBS'])

# print the date of dark observations:
print('\nThe date the observations for the dark files were made is', objhead['DATE-OBS'])

# part c: Why not print the time of observations?
# I looked up info on the fits file headers, and it is saying that the 
# time of observation is actually included in the KWARG for "DATE-OBS" 
# in most modern fit-files. 