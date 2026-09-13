"""This is the support function library for hw3_rab in AST4762.

It contains the functions: 
    'square' which will allow you to square a value or array of values
"""

# import any libraries needed
import os 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt  
import astropy.io.fits as fits


#if you need to import functions from other files you can do it
#afterwards like this:
from my_module import my_func, other_func

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
    >>> a=[1,2,3]
    >>> return sq=[1,4,9]
    
    Revisions
    ---------
    2026-09-12 ro235529@ucf.edu created the file and function
    """
    # square the input
    sq = val**2

    # return the squared value
    return sq

def 
