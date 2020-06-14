# This file gathers all the methods implemented and exports the "main functions" used to apply each method  

import numpy as np
from filters import smoothing_methods as sm
from filters import edge_methods as em

def edge_filter(img, selected=2):
    """
    Depending on the selected method, applies an Edge Filter to the image
    1 - Laplace of Gaussian
    2 - Sobel Operator

    Parameters:
        img: image to apply the filter
        selected: number of the method
    """
    if(selected == 1):
        return em.laplacian_of_gaussian(img, n=4, sigma=1)

    elif(selected == 2):
        return em.sobel_operator(img)
    
    else: print('Not an valid Edge Filter')

    return img

def smoothing_filter(img, n=3, sigma=0.5, selected=1):
    """
    Applies the selected Smoothing Filter to the image
    1 - Median Filter
    2 - Gaussian Filter

    Parameters:
        img: image to apply the filter
        n: size of the filter
        sigma: standard deviation (used by gaussian filter)
    """
    if (selected == 1):
        return sm.median_filter(img, n)
    
    elif (selected == 2):
        return sm.gaussian_filter(img, n, sigma)
    
    else: print('Not an valid Smoothing Filter)')
