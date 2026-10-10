"""This is the support function library for hw7_rab in AST4762.

It contains the functions: 
    'box_function' which takes in an array of x values, location
    of the center window, height and width and returns a box 
    function model fit.
"""

# import any libraries needed
import numpy as np

def box_function( x, center, width, height, baseline = 1.):
    """This function takes in a data set and finds a box function 
        model to return.

    This fucntion will calculate the box function from provided 
    x-data, venter location, width, and height. It will write a 
    function to fit the parameters provided and return it.

    Parameters
    ----------
    x : array_like
        data should be the array of data for the x-axis

    center: int or float
        this is the location of the center of the box
        
    width: int or float
        this is the width of the box

    height: int or float
        this is the height of the box

    baseline: into or float {1.}
        This is the height of the data before dip of the box. 
        Default value is set to 1 so that it assumes a normalized
        output, but added so that box functions could be written for 
        non-normalized data.
        
    Returns
    -------
    y : numpy array
        the array of y values for the box function

    Examples
    --------
    >>>a = np.arange( 0, 10, 1)
    >>>y = box_function(a, 4, 2, 0.3, 2)
    >>>print(y)
    [2.  2.  2.  0.3 0.3 0.3 2.  2.  2.  2. ]
    
    Revisions
    ---------
    2026-10-10 ro235529@ucf.edu created the file and function
    """
    y = np.ones(len(x)) * baseline
    y[(x >= center - width/2) & (x <= center + width/2)] = height
    return y
    