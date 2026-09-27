# Robyn Baumann
# AST 4762
# Practicum 3
# Sep 25, 2026

# import what is needed
import numpy as np
import matplotlib.pyplot as plt
from linfit import linfit

# Problem 1
print('Problem 1:')

# part a
# read in data file
f = np.loadtxt('practicum3_1.dat', delimiter=" ")

# assign model 1
x1     = f[:100, 0]
model1 = f[:100, 1]

# plot model 1
plt.scatter(x1, model1, label='Data 1')
plt.xlabel('x', fontsize = 14 )
plt.ylabel('f(x) ', fontsize = 14 )
plt.title('Practicum 3 Model 1', fontsize = 20 ) 

# part b
# pass to linfit and get parameters
fit1 = linfit(model1, x1, 0.5)
yfit1 = fit1[7]

# print the values from fit1
print('\nModel 1:')
print('The y-intercept is: ', fit1[0])
print('The slope is: ', fit1[1])
print('The uncertainty of the y-intercept is: ', fit1[2])
print('The uncertainty of the slope is: ', fit1[3])
print('Chi squared is: ', fit1[4])
print('The probability of a worse Chi squared is: ', fit1[5])
print('The covariance matrix is: ', fit1[6])
print('The y-fit is: ', fit1[7])

# part c : plot the fit and save the graph
plt.plot(x1, yfit1, color='orange', label='Model 1')
plt.legend()
plt.savefig('p3_rab_problem1_graph1.png')
plt.show()

# part d: same for model 2!
# assign model 2
x2     = f[100:, 0]
model2 = f[100:, 1]

# plot model 2
plt.scatter(x2, model2, label='Data 1')
plt.xlabel('x', fontsize = 14 )
plt.ylabel('f(x) ', fontsize = 14 )
plt.title('Practicum 3 Model 2', fontsize = 20 ) 


# pass to linfit and get parameters
fit2 = linfit(model2, x2, 0.5)
yfit2 = fit2[7]

# print the values from fit2
print('\nModel 2:')
print('The y-intercept is: ', fit2[0])
print('The slope is: ', fit2[1])
print('The uncertainty of the y-intercept is: ', fit2[2])
print('The uncertainty of the slope is: ', fit2[3])
print('Chi squared is: ', fit2[4])
print('The probability of a worse Chi squared is: ', fit2[5])
print('The covariance matrix is: ', fit2[6])
print('The y-fit is: ', fit2[7])

# plot the fit and save the graph
plt.plot(x2, yfit2, color='orange', label='Model 2')
plt.legend()
plt.savefig('p3_rab_problem1_graph2.png')
plt.show()
