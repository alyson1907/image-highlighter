# This file contains the methods/filters used to apply/change colors in a greyscale image

import numpy as np
from skimage.color import rgb2hsv
from skimage.color import gray2rgb

def change_contrast(img, k=0.035):
  """
  Applies an contrast factor to the original image, increasing or decreasing it.

  Parameters:
    img: image to change the contrast
    k: amount to increase/decrease contrast (greater = more intense)
  """
  # Handling greyscale images
  if (len(np.shape(img)) == 2):
    img = gray2rgb(img)

  # convert the input image to HSV
  img_hsv = rgb2hsv(img)
  img_out = (255 / (1 + np.exp(-k * (img.astype(np.int32) - 127))))
  return img_out
