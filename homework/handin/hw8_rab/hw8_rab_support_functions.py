"""This is the support function library for hw8_rab in AST4762.

It contains the functions: 
    'normmedcomb' which takes in an array of the dark subtracted 
    flux, implements a normalized median combination method, and 
    returns a tuple containing the normalized array and an array 
    of the normalization factors.
"""

# necessary libraries
import numpy as np

def normmedcomb(data, region = None ):
    """This function takes in a 3D array of data that contains 
    the dark-subtracted sky flux.

    This fucntion will calculate and return the normalization
    factors as well as create a normalized array of the data.

    Parameters
    ----------
    data : 3D array
        this should be a numpy 3D array that contains the dark
        subtracted data to be normalized

    region: tuple {None}
        the corner coordinates of the normalization region in 
        the form of ((y1,x1),(y2,x2)), default is set to 
        include the entire image    
        
    Returns
    -------
    new_data, factors: 2D array
        this is a 2D array of the normalized data

    factors: 1D array
        this is an array of the normalization factors

    Examples
    --------
    >>>
    
    Revisions
    ---------
    2026-10-14 ro235529@ucf.edu created the file and function
    2026-10-17 ro235529@ucf.edu commented out loop, and rewrote 
               without the loop
    """
    # get shape of the data array
    n, nx, ny = data.shape
    
    # create region of normalization
    if region == None:
        (y1, x1) , (y2, x2) = (0, 0) , (ny, nx)
    else:
        (y1, x1) , (y2, x2) = region

    # create array for normalized data
    new_data = np.array(data, dtype=np.float64, copy=True)

    # median combine the frames, for x and y in images
    norm = np.median(data[:, y1:y2 , x1:x2], axis = (1,2), keepdims = True)
    new_data /= norm

    # create array of normalization factors
    factors = norm.reshape(data.shape[0])
    
    # loop to normalize each object and get factors
    #for i in range (n):
        #factors[i]  = np.median(data[i, y1:y2 , x1:x2])
        #new_data[i] = data[i] / factors[i]

    # combine the median
    new_data = np.median(new_data, axis=0)
    
    # return normalized data ana dnormalization factors
    return new_data, factors
