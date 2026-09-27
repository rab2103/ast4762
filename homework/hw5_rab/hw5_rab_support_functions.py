"""This is the support function library for hw35_rab in AST4762.

It contains the functions: 
    'sigrej' which takes in a data set and finds the indices of 
        values not within the desired multiples of standard 
        deviation. These indices are then returned as a boolean mask.
"""

# import any libraries needed
import numpy as np

def sigrej(data, rej_req, mask=[True,True]):
    """This function takes in a data set and finds the indices of 
        values not within the desired multiples of standard deviation.

    This fucntion will calculate the mean of the given data, find
    where the data fits within the provided multiples of standard
    deviation, and return a boolean mask for the good indices of 
    data.

    Parameters
    ----------
    data : array_like
        data should be the array of data you want clipped

    rej_req: tuple
        the length of the tuple should be the number of times the 
        function should clip the data, with the value in each place
        the multiples od the standard deviation to clip by

    mask: boolean array, {'True', 'False'}, optional
        This array should contain only boolean values and match the 
        size of the data array. Any False in the array will first be
        cut from the data before clipping by the standard deviation.
        This is optional, and arrays are automatically assumed to be 
        fully True.
        
    Returns
    -------
    new_mask : boolean array, {'True', 'False'}
        the array of the indices that match the desired clipping

    Examples
    --------
    >>> a = np.array([1,1,1,1,1,2,2,3,3, 12, 44])
    >>> indices = np.ones(len(a), dtype=bool)
    >>> indices[2] = False
    >>> new_ind = sigrej(a,(1., 1., 1.),indices)
    >>> print(new_ind)
    [ True  True False  True  True  True  True False False False False]
    
    Revisions
    ---------
    2026-09-26 ro235529@ucf.edu created the file and function
    """
    # create mask if not provided
    if all(mask) == True:
        new_mask = np.ones(len(data), dtype=bool)
        clipped = data
    else:
        new_mask = mask
        clipped = data[new_mask == True]

    # create loop to run desired number of times
    for i in range(len(rej_req)):

        #calculate standard deviation and mean
        st_dev = np.std(clipped)
        mean    = np.mean(clipped)

        # edit mask to find the bad values
        new_mask[np.where( np.abs(data - mean) >= rej_req[i] * st_dev )] = False

        # re-assign clipped to new values
        clipped = data[ new_mask == True ]
        i += 1

    # return the boolean mask
    return new_mask