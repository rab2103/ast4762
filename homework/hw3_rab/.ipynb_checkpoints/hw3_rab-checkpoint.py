# Robyn Baumann
# AST4762 Homework 3
# Sep 12, 2026

# import libraries needed for the program
import matplotlib.pyplot as plt
import numpy as np
import astropy.io.fits as fit
from hw3_rab_support_functions import square, squareplot

# Begin Problem 2 
print("Problem 2:\n")

# create first test array for square and print
test_square_1 = np.arange(0,10)
print ('test_square_1 before square:', test_square_1, '\n' )

# square and print
test_square_1 = square(test_square_1)
print ('test_square_1 after square:', test_square_1, '\n' )

# second test for square and print:
test_square_2 = np.linspace(0,25,25).reshape(5,5)
print ('test_square_2 before square:', test_square_2, '\n' )

# square and print
test_square_2 = square(test_square_2)
print ('test_square_2 after square:', test_square_2, '\n' )

# Begin Problem 3:
print('Problem 3:\n')

# call the square plot function with array (1, 2.5, 4, 5.5, 7), and save the figure
squareplot(1., 7, 5, True)
