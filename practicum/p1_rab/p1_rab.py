# Robyn Baumann
# AST4762 
# Practicum 9/11

import numpy as np
import matplotlib.pyplot as plt

# Problem 1: With Loops:

# parameters for the loop 
row = 300
col = 200

# create empty 2D array
arr1 = np.zeros( (300, 200) )

# loop to fill
for i in range(row):
    for j in range(row):
        arr1[i:j] = i

# check that y is correct 
print ("Should be 5.0:", arr1[5,8])
print ("Should be 178.0:", arr1[178,113])

# plot the graph
plt.imshow(arr1, cmap='gray', origin='lower')

#Problem 1: Without Loops:

# make the 2D array:
arr2 = np.zeros( (300, 200) )

# array to hold values:
y = np.arange(300)

# need to turn the array
y = y.reshape(300,1)

#store new values into array
arr2 += y

# check y is correct
print ("Should be 15.0:", arr2[15,8])
print ("Should be 278.0:", arr2[278,113])

# plot the graph
plt.imshow(arr2, cmap='gray', origin='lower')

# read info about the file
fits.info('m42_40min_ir.zip')

# read header info
fits.getheader('m42_40min_ir.zip')

data = fits.getdata('m42_40min_ir.zip') # save data to plot

# create image with appropriate labels
plt.imshow(data, cmap = 'gray', origin='lower')
plt.xlabel( 'Right Ascention' )
plt.ylabel( 'Declination' )
plt.title( 'Nebula (Orion) and Robyn')

# save image with proper naming conventions
plt.savefig('p1_rab_problem3_image1.png')

