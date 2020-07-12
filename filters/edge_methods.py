# This file contains the methods/filters related to edge detection and enhancement

import numpy as np
from filters import helpers as hp

def laplacian_of_gaussian(img, n=3, sigma=1):
  """
  Applies Laplacian of Gaussian  filter to a grayscale image.

  Parameters:
    img: image to apply LoG to
    n: size of the filter
    sigma: Gauss sigma to be applied to the image
  """
  log_filter = np.zeros((n, n))
  r = int(n / 2)
  for i in range(-r, r):
      for j in range(-r, r):
          log_filter[i][j] = -(np.pi * sigma ** 4) ** (-1) * (1 - (i ** 2 + j ** 2)/ (2 * sigma ** 2)) * np.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))
    
  img_out = hp.apply_filter_to_image(img, log_filter, n)

  return img_out

def sobel_operator(img):
  """
  Applies Sobel Operator to an image.

  Parameters:
    img: image to apply the filter to
  """
  fx = np.array([[-1, 0, 1], [-2, 0, 2], [-1 ,0 ,1]])
  fy = np.array([[-1 ,-2, -1], [0 ,0 ,0], [1 ,2 ,1]])

  img_out = np.zeros((img.shape[0] - 2, img.shape[1] - 2, 3))
  for y in range(1, img.shape[0] - 1):
      for x in range(1, img.shape[1] - 1):
          gx = np.sum(np.multiply(img[y-1:y+2, x-1:x+2], fx))
          gy = np.sum(np.multiply(img[y-1:y+2, x-1:x+2], fy))
          img_out[y - 1][x - 2] = np.sqrt(gx ** 2 + gy ** 2)

  return hp.trim_dimension(img_out)
