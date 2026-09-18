# Robyn Baumann
# AST4762 Practicum 2
# Sep 18 2026

# load necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print('\nProblem 1')
print('Since N is arbitrary, I am writing a function to take in N and be called.')

def create_gaussian(mu, sigma, N):
    """This function takes a mean, standard deviation, and number of inputs and 
    returns a gaussian distribution with those values.

    Parameters
    ----------
    mu : int or float
        mean of your data spread
    sigma: int or float
        standard deviation of the data spread
    N: int
        number of items in the data set

    Returns
    -------
    gaussian : array_like
        the randomized gaussian distribution

    Notes
    -----
    uses numpy
    
    Revisions
    ---------
    2026-09-18 ro235529@ucf.edu created the file and function
    """
    gaussian = np.random.normal(mu, sigma, N) 

    return gaussian

#assign sigma nad mu from prob 1
sigma = 13
mu    = 55

print('\nProblem 2:')
#Assign N=10
N=10

data = np.zeros((10,3))

#create gaussian distributions:
for i in range (10):
    g = create_gaussian(mu, sigma, N)

    # find mean:
    mean = np.mean(g)

    # find standard deviation
    stdev = np.std(g,ddof=1)

    # save into array
    data[i:] = (i, mean, stdev)

print(data)

print('\nProblem 3: AI\'s code')

# copy and pasted the AI code here without the imports:

N = 10
mu = 55
sigma = 13

results = np.zeros((10, 3))

for i in range(10):
    sample = np.random.normal(mu, sigma, N)
    results[i] = [i, np.mean(sample), np.std(sample)]

print(results)

print('AI without Loop:')

N = 10
mu = 55
sigma = 13

samples = np.random.normal(mu, sigma, (10, N))

results = np.column_stack((
    np.arange(10),
    np.mean(samples, axis=1),
    np.std(samples, axis=1)
))

print(results)

print('\nProblem 4:')

# save data to a text file
np.savetxt('p1_rab_problem4_data.txt', data, delimiter=' ', newline='\n', header=' N = 10:Trial  \t Mean \t Standard Deviation')
print('Saved data to p1_rab_problem4_data.txt')

print('\nProblem 5:')

# open file to append
file = open("p1_rab_problem4_data.txt", "a")

# reuse the loop from problem 2 with different N's
for j in range(5):
    N *= 10
    for i in range (10):
        g = create_gaussian(mu, sigma, N)

        # find mean:
        mean = np.mean(g)

        # find standard deviation
        stdev = np.std(g,ddof=1)

        # save into array
        data[i:] = (i, mean, stdev)

    # write to txt file
    np.savetxt(file, data, header='\n  N = ' + str(N) + ': Trial  \t Mean \t Standard Deviation' )

# let me know the kernal is done
print('finished appending to p1_rab_problem4_data.txt')

file.close()

print('\nProblem 6:')

# create an array to hold the stdev of the samples
std_samples = np.zeros((6, 2))

# read the file 
dat = np.loadtxt("p1_rab_problem4_data.txt")

# save variables from dat
dat_trial, dat_mean, dat_std = dat.T

# new array to hold the trial number and the standard deviations
dat_arr = np.zeros((6,2))

#trial number holder and to hold the file row number
n=10
row = 0

#array to store values of means
mean_arr = np.zeros((10,1))

#loop to find means and store in array
for k in range(6):
    # add the values to the mean_arr
    for p in range(10):
        mean_arr[p] = dat_mean[row]
        row+=1
    std_means = np.std(mean_arr,ddof=1)
    dat_arr[k] = [n,std_means]
    n *= 10

# was getting the array to print, but it was doing scientific, following code from ChatGPT suggestion, with a few edits
print("#Sample size    Std. dev. of mean")
for row in dat_arr:
    print(f"{int(row[0]):<10} \t {row[1]:.2f}")

# re-open file to append
file = open("p1_rab_problem4_data.txt", "a")

# write to txt file
np.savetxt(file, dat_arr, header='\nSample Size \t Std. dev. of mean' )

file.close()

print('\nProblem 7:')

# get x and y from dat_array
x = dat_arr.T[0]
y = dat_arr.T[1]

# create plot
plt.figure( figsize = (10,10))
plt.loglog(x,y)
plt.grid()

# add titles and axis labels
plt.title( 'Standard Deviataion of the Means', fontsize = 20 )
plt.xlabel( 'Sample Size', fontsize = 12 )
plt.ylabel( 'Std. Dev', fontsize = 12 )

# save the figure 
plt.savefig('p2_rab_problem7_graph1.png')

# show the figure
plt.show()
