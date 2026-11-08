"""This is the support function library for hw8_rab in AST4762.

It contains the functions: 
    'disk' which creates a 2D mask array with the image of a disk. 
    Pixels in the image will have a value of True for each pixel whose
    center is within a certain radius of a given position, and False
    elsewhere.
"""

# necessary libraries
import numpy as np

def disk(r, center, im_shape):
    """This function takes in information on the size of the 
    overall image, the location (center) for a circle, and the 
    radius of said circle to create a 2D mask array of a disk.

    Parameters
    ----------
    r : int or float
        this is the radius of the disk

    center: 2D array or tuple 
        the center of the disk (y,x)

    im_shape: 2D array or tuple
        the size of the total image (y,x)
        
    Returns
    -------
    im_disk: 2D Boolean array
        2D mask with the image of a disk, the pixels within the 
        disk are True, the pixels outside the disk are False.

    Examples
    --------
    >>>
    
    Revisions
    ---------
    2026-10-22 ro235529@ucf.edu created the file and function
    """
    # create array to hold all the x and y coordinates
    coord = np.indices(im_shape)
    
    # distance of each point from the center
    dist = np.sqrt((coord[0]-center[0])**2 + (coord[1]-center[1])**2)

    # create the boolean, true for pixels less than radius
    im_disk = dist <= r

    return im_disk

    