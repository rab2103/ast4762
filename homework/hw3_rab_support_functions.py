"""This is the support function library for hw3_rab in AST4762.

It contains the functions: 
    'square' which will allow you to square a value or array of values
"""

# import any libraries needed
import os 
import numpy as np
import matplotlib.pyplot as plt  

def square(val) :
    #this is our function's docstring!
    """This function takes in a number or array, squares the value(s) 
    and returns the squared value(s).

    The input is saved as val, then val is squared

    Parameters
    ----------
    val : array_like
        val can be an integer or an array. If val is an array, then
        all the elements in the array will be squared

    Returns
    -------
    sq : array_like
        sq will be the squared value(s) of val.

    
    Notes
    -----
    sq = val**2

    Examples
    --------
    >>> a=np.array([1,2,3])
    >>> print( hw3_rab_support_functions.square(a) )
    [1,4,9]
    
    Revisions
    ---------
    2026-09-12 ro235529@ucf.edu created the file and function
    """
    # square the input
    sq = val**2

    # return the squared value
    return sq

def squareplot(low, high, num, saveplot=False) :
    """This function will create an array from the lowest number 
    (low) to highest number (high) with the number of entries in 
    the array (num) and then plot the array and their squares, 
    with an option to save the plot.

    The low entry will be the first number in an array and the 
    high entry will be the highest number or arrays. The array
    will be created with linspace, and the number of values 
    between low and hig hwill be given by num. Then this function
    passes the array to square, and with the returned array will
    then create a plot and show the plot in the output. There is 
    an option to save the plot as a pdf if saveplot is set to 
    True, but the default will be False.

    Parameters
    ----------
    low : int or float
        This will be the first number in the linspace array.
    high : int or float
        This will be the last number (inclusive) in the 
        linspace array
    num : int or float
        This will be the number of values in the linspace
        array.
    saveplot : {'False', 'True'}, optional
        Choices in brackets, default first when optional. 
        If changed to True, the plot will be saved as a pdf.

    See Also
    --------
    square : returns a square of the array to plot


    Notes
    -----
    The Plot will have the horizontal axis labeled “Input” 
    and vertical axis labeled “Output”, and the title of 
    the plot will be “Square Function”.

    Examples
    --------    
    >>> hw3_rab_support_functions.squareplot(1,8,5)
    a plot with the x-axis for the input numbers and the y-axis
    of the squares. It should have 5 data points and the graph
    will not be saved.

    >>> hw3_rab_support_functions.squareplot(1, 100, 200, True)
    a plot with the x-axis for the input numbers and the y-axis
    of the squares. It should have 200 data points and the graph
    will be saved as a pdf named hw3_rab_problem3_graph1.pdf.


    Revisions
    ---------
    2026-09-12 ro235529@ucf.edu created the file and function
    """

    # Create the linspace array
    x = np.linspace(low, high, num)

    # pass to square to get y-axis values
    y = square(x)

    # create the plot
    plt.figure( figsize = 10,10)
    plt.scatter( x, y)

    # add titles and axis labels
    plt.title( 'Square Function' )
    plt.label( 'Input' )
    plt.ylabel( 'Output' )

    # show plot
    plt.show()

    # save the figure if they want to
    if saveplot!=False:
        plt.savefig('hw3_rab_problem3_graph1.pdf')

    return
