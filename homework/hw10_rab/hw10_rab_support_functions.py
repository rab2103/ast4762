"""This is the support function library for hw10_rab in AST4762.

It contains the functions: 
    'apphot' which perfoms aperture photometry on an image. It will 
    intake an image and the desired parameters for the photometry
    and return the stellar flux and average sky values.
"""

# import necessary libraries
import os # standard library imports first
import numpy as np
import matplotlib.pyplot as plt  # NOTE: pyplot, *not* pylab!
import astropy.io.fits as fits
from hw9_rab_support_functions import disk

def apphot(obj, bad_mask, aper_r, inner_r, outer_r, center):
    """This function takes in an image and performs aperature 
    photometry, returning the stellar flux, average sky value, and 
    number of bad pixels as a tuple.

    Within this function, a mask will be created for the sky annulus 
    and the aperture of the star using the disk() function. 
    
    Parameters
    ----------
    obj: 2d array
        this is the image data in the form of a 2D array

    bad_mask: 2D Boolean 
        2D boolean array that has False for any bad pixels to be 
        excluded from the calculations
        
    aper_r : int or float
        this is the radius aperture disk

    inner_r : int or float
        this is the radius of the inner annulus

    outer_r : int or float
        this is the radius of the outer annulus

    center: 2D array or tuple 
        the center of the disk (y,x)
        
    Returns
    -------
    flux : float
        the calculates stellar flux

    avg_sky : float
        the calculated average sky value

    nbad_pix : int
        the number of bad pixels in the image

    See Also
    --------
    disk : this function is used to create the circular masks
        for the annulus and the aperture

    Examples
    --------
    >>>
    
    Revisions
    ---------
    2026-11-6 ro235529@ucf.edu created the file and function
    """

    # start by creating index for the data
    ny, nx = obj.shape
    buffer = 5
    # coord = np.indices(ny,nx)
    cy, cx = center

    # trim image coordinates
    y1 = max(0,  int(cy - outer_r - buffer) )
    y2 = min(ny, int(cy + outer_r + buffer) )
    x1 = max(0,  int(cx - outer_r - buffer) )
    x2 = min(nx, int(cx + outer_r + buffer) )

    # copy the image so it does not change, and apply bad_pix mask
    data = obj[y1:y2, x1:x2].copy()
    if bad_mask != None:
        mask = bad_mask[y1:y2, x1:x2].copy()
    else:
        mask = np.full(data.shape, True)
    new_cent = np.array(data.shape) / 2

    # create disks for aperature and annulus masks
    aper    =  disk(aper_r,  new_cent, data.shape) & mask
    annulus = (disk(outer_r, new_cent, data.shape) \
             ^ disk(inner_r, new_cent, data.shape)) & mask

    # calculate average sky from annulus mask
    nsky    = np.sum(annulus)
    sky     = np.sum(data[annulus])
    avg_sky = sky / nsky

    # subtract this value from each pixel in the sub-image
    data -= avg_sky
    
    # calc stellar flux from aper mask
    flux = np.sum(data[aper])

    # number of bad pixels
    nbad_pix = np.sum(mask[aper] == False)
    
    # return the values
    return flux, avg_sky, nbad_pix

    