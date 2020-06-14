# NOTE: This File contains general helper functions used in multiple files along the project

import matplotlib.pyplot as plt
import numpy as np

def apply_filter_to_image(img, filter_matrix, n):
    """
    Applies the received filter to an image

    Params:
        img: image that the filter will be applied to
        filter_matrix: filter to apply to the image
    """
    x,y = np.shape(img)
    # Padding the received filter with Zeroes to match the image shape
    filter_matrix = np.pad(filter_matrix,((0, x - n),(0, y - n)), 'constant', constant_values=(0, 0))
    fft2 = np.fft.fft2(filter_matrix)

    # applying Fourier Transform
    img_out = np.fft.fft2(img)
    img_out = np.multiply(img_out, fft2)

    # ifft2 below is the Inverse Fourier Transform
    img_out = np.fft.ifft2(img_out)
    return img_out.real

def normalize(img):
    """
    Normalizes an image.

    Parameters:
    img: input image to be normalized
    """
    img = img.astype(float)
    return (255 * (img - np.min(img)) / (np.max(img) - np.min(img))).astype(np.uint8)

def printImg(img):
  plt.rcParams['figure.figsize'] = [7, 7]
  plt.imshow(img, cmap="gray")
  plt.show()
