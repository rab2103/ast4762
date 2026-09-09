# Robyn Baumann
# AST4762
# Homework 2
# Sun Sep 6, 2026

# import the libraries to be used in this assignment
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Problem 1 recorded in the log

# Begin Problem 2 here:
print ("Problem 2:")

# a1) Create an array of integers x from 0 to 1000
x = np.arange (0, 1001) # this has 1001 elements

# how many elements needed? Proof with length:
print ( "The array x has", len(x), "elements.")

# a2) Print the datatype of the array and the array’s minimum and maximum.
print ( "x's type:", type(x) )
print ( "Min. value of x = ", np.min(x) )
print ( "Max. value of x = ", np.max(x) )

# b1) Re-scale x to contain values from 0 to 2π
x = x * 2 * np.pi / 1000

# b2) Print the minimum and maximum values of the new x array.
print ( "New min. value of x = ", np.min(x) )
print ( "New max. value of x = ", np.max(x) )

# c) Make an array y whose values are the sine of the values of x.
y = np.sin(x)

# d) Print the value of element 234 of y
print ( "The value of element 234 of y is:", y[234] )

# begin problem 3:
print ( "\nProblem 3:" )

# a) Plot y vs. x from problem 2c. Make the plot publication-ready using reasonable axis labels etc. 

#let's first turn interactive mode on for the .py file:
plt.ion()

# setting for the graph, I'm choosing my fav color
plt.figure( figsize = (8, 8) )
plt.plot( x, y, color = 'blue' , linewidth = 3 )
plt.title ( r'Sin($\theta$) vs. $\theta$' )

#change the labels, using LaTex to get theta
plt.xlabel( r'$\theta$ [radians]', fontsize = 14 )
plt.ylabel( r'Sin($\theta$)', fontsize = 14 )

# make the ticks a little bigger
plt.yticks( fontsize = 16 )
plt.xticks( fontsize = 16 )

# b) Save your plot as a PNG using the appropriate Python commands 
plt.savefig('hw2_rab_problem3_graph1.png')

# begin problem 4
print ( "\nProblem 4:" )

# a1) Make a “ramp” array r with 101 evenly spaced elements going from -1 to +1.
r = np.linspace(-1, 1, 101)
print ("Proof that r is 101 elements, the length is:", len(r))

# print og r before clipping (for part b)
plt.figure( figsize = (10, 8) )
plt.plot( r, color = 'blue' , linewidth = 2 )
plt.title ( 'Clipped Ramp', fontsize = 14 )

# a2) “Clip”, or mask, the array so that any value greater than 0.5 is set to 0.5 and any value less than -0.5 is set to -0.5. 
r[np.where(r > 0.5) ] =  0.5
r[np.where(r < -0.5)] = -0.5

# now print clipped ramp (for part b) 
plt.plot( r, color = 'red', linewidth = 2 )

# add axis labels to match photo in Hw directions
plt.xlabel( 'X', fontsize = 10 )
plt.ylabel( 'Y', fontsize = 10 )

# b2) Use the appropriate python command to save the plot as a PDF. Name the PDF appropriately
plt.savefig('hw2_rab_problem4_graph1.pdf')

# begin problem 5
print ( "\nProblem 5:" )

print ("""
\t The first python resource I found was sunpy at https://sunpy.org/. sunpy 
is based off of astropy with a focus on solar physics. It was originally 
founded by a small group of NASA researchers and aims to help programmers 
process data specifically relating to the sun. It aslo has built-in models 
specifically for our sun, and allows for solar data to be easily integrated 
so it can be used with other common python packages.
\t The second python resource I found was chiantipy at 
https://chiantipy.sourceforge.net/welcome.html. Chiantipy specializes in 
performing calculations with the Chianti atomic data base in relation to 
astrophysical spectra. The functions can help with spectral line data and 
can help with plotting of both emmission and absorption spectra. 
""")
