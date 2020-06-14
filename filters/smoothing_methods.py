import numpy as np
from filters import helpers as hp

def median_filter(img, n):
    """
    Parameters:
        img: img that the filter will be applied to
        n: size of the filter to be applied
    """
    x, y = np.shape(img)

    # Padding
    pad_size = n // 2
    img = np.pad(img, (pad_size), 'wrap')

    #get neighborhood matrices on auxiliar matrix
    aux = np.zeros((x , y, n*n))
    for i in range(0, x):
        for j in range(0, y):
            aux[i][j] = img[i:n+i, j:n+j].flatten()

    #calculates img out using collected matrices
    img_out = np.zeros((x, y))
    img_out = np.median(aux, axis=2)

    return img_out

def gaussian_filter(img, n, w):
    """
    Apply gaussian filter over given image

    Parameters:
        img: input image
        n: size of image
        w: standard deviation
    """
    # Generating the gaussian filter matrix to apply to the image
    f = np.zeros((n,n), dtype=float)
    v = np.linspace(-5, 5, n)
    for i in np.arange(n):
        for j in np.arange(n):
            x = v[i]
            y = v[-1-j]
            f[i][j] = (1 / (2 * np.pi * w ** 2)) * np.exp(- ( x ** 2 + y ** 2) / (2 * w ** 2))
    f = f / np.sum(f)

    # Applying the filter to the image
    img_out = hp.apply_filter_to_image(img, f, n)
    return img_out
