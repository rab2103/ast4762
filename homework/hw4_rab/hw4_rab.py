# Robyn Baumann
# AST4762 HW4
# Fri Sep 18

# import libraries needed for the program
import matplotlib.pyplot as plt
import numpy as np

# begin problem 2
print('Problem 2:')

# a) create Gaussian distribution with sample siz 10,000
# standard deviation 13 and mean 55
mu  = 55
std = 13
N   = 10000
gaussian = np.random.normal(mu, std, N)

# b) plot histogram
plt.figure( figsize = (10,5))
plt.hist(gaussian, bins=np.arange(0,100,1))
plt.grid()

# add titles and axis labels
plt.title( 'Gaussian Distribution Histogram', fontsize = 20 )
plt.xlabel( 'Value, x', fontsize = 12 )
plt.ylabel( 'Number of Values, x', fontsize = 12 )

# save the figure 
plt.savefig('hw4_rab_problem2b_graph1.png')

# c) plot gaussian over the histogram and save new graph

# create array for center of bins
x = np.arange(0.5, 100, 1) 

# start with calculating the gaussian function fron the distribution
gfunct = (1 / (std* np.sqrt(2 * np.pi))) * np.exp(-0.5*((x - mu)/std)**2)

# account for number of trials bc gfunct is a sum to 1
gfunct *=N

# plot the Gaussian on top of the histogram
plt.plot(x, gfunct)

#save new figure
plt.savefig('hw4_rab_problem2c_graph2.png')

#show new figure
plt.show()

print('\nProblem 3: Please see hw4_rab_problem3_work.pdf')