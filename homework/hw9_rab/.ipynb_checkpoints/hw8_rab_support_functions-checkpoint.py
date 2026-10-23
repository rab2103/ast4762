"""This is the support function library for hw8_rab in AST4762.

It contains the functions: 
    'normmedcomb' which takes in an array of the dark subtracted 
    flux, implements a normalized median combination method, and 
    returns a tuple containing the normalized array and an array 
    of the normalization factors.

    'skycormednorm' which takes in 2, 2D arrays of an object and 
    a normalized array and returns a subtraction of the two 
    within either a designated region or the entire image.
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
    new_data: 2D array
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
    n, ny, nx = data.shape
    
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
    factors = norm.reshape(new_data.shape[0])
    
    # loop to normalize each object and get factors
    #for i in range (n):
        #factors[i]  = np.median(data[i, y1:y2 , x1:x2])
        #new_data[i] = data[i] / factors[i]

    # combine the median
    new_data = np.median(new_data, axis=0)
    
    # return normalized data and normalization factors
    return new_data, factors

def skycormednorm(obj, norm, region = None):
    """This function takes in 2, 2D arrays of an object and 
    the normalized object and returns a subtraction of the two 
    within either a designated region or the entire image.

    This fucntion will de-normalize the array before 
    subtracting it from the original object to then return 
    the subtracted frame. There is an option to designate 
    a specific region for this to be done over, if not 
    specified, the function will do it over the entire image. 

    Parameters
    ----------
    obj : 2D array
        this should be a 2D array of the image that is already 
        dark subtracted

    norm : 2D array
        this should be the normalized array of obj, or the 
        normalized sky frame

    region: tuple {None}
        the corner coordinates of the normalization region in 
        the form of ((y1,x1),(y2,x2)), default is set to 
        include the entire image    
        
    Returns
    -------
    sky_sub : 2D array
        this is a 2D array of the sky-subtracted object

    Examples
    --------
    >>>
    
    Revisions
    ---------
    2026-10-17 ro235529@ucf.edu created the file and function
    """
    # get shape of the object array
    ny, nx = obj.shape

    # create region of normalization
    if region == None:
        (y1, x1) , (y2, x2) = (0, 0) , (ny, nx)
    else:
        (y1, x1) , (y2, x2) = region

    # create array for the object to subtract sky from
    sky_sub = np.array(obj, dtype=np.float64, copy=True)

    # find the normalized information
    norm_fact = np.median(obj[y1:y2 , x1:x2], axis = (0,1), keepdims = True)

    # de-normalize the sky array
    new_sky = norm * norm_fact

    #subtract the sky frame
    sky_sub -= new_sky

    return sky_sub
    
