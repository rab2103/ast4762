# Robyn Baumann
# AST4762
# Homework 5
# Sep 26, 2026

# import libraries needed for the program
import matplotlib.pyplot as plt
import numpy as np
from hw5_rab_support_functions import sigrej

# problem 2
print('Problem 2:')

# part a: generate array with 400 data points
x = np.zeros(400)

# make 396 elements random poisson distribution, last 4 being "noise"
x[:396] = np.random.poisson(10000,396)
x[396:] = np.random.uniform(0, 10**6, 4)

# print mean and median with the answers from the array I got:
# the commented numbers will change every time it is ran, but is what 
# I got while testing, and the Hw requested it
print('The original median of the array is: ', np.median(x)) # 9990.5
print('The original mean of the array is: ', np.mean(x))     # 12020

# part b: mask the data

# calculate standard deviation:
st_dev1 = np.std(x)
print('Standard deviation using np.std of the array: ', st_dev1) # 24482

# find how many data points are more than 5 standard deviations
subsample = x[np.where( np.abs(x - np.median(x)) <= 5 * st_dev1 )]

# print mean and median with the answers from the clipped array:
print('The new median of the array is: ', np.median(subsample)) # 9990
print('The new mean of the array is: ', np.mean(subsample))     # 10030

# calculate new standard deviation:
st_dev2 = np.std(subsample)
print('New standard deviation using np.std of the array: ', st_dev2) # 813.27

# problem 3: sub-subsample
print('\nProblem 3:')

# create 2nd subsample
subsub = subsample[np.where( np.abs(subsample - np.median(subsample)) <= 5 * st_dev2 )]

# print the new median, mean and standard deviation
print('The new median of the array is: ', np.median(subsub)) # 9989.5
print('The new mean of the array is: ', np.mean(subsub))     # 9989.93
st_dev3 = np.std(subsub)
print('New standard deviation using np.std of the array: ', st_dev3) # 95.49

# now try calculating data using sigrej
indices = sigrej(x, (5.,5.))
clipped = x[indices == True]

# print requested info
print(' ')
print('The median from sigrej is: ', np.median(clipped)) # 9989.5
print('The mean from sigrej is: ', np.mean(clipped))     # 9989.93
st_dev4 = np.std(subsub)
print('The standard deviation using sigrej: ', st_dev4)  # 95.49