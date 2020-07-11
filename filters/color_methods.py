# This file contains the methods/filters used to apply/change colors in a greyscale image

import numpy as np
from skimage.color import rgb2hsv
from skimage.color import gray2rgb
from skimage.color import rgba2rgb
import matplotlib.pyplot as plt
import filters.helpers as hp

def handle_double_channels_img(img):
  if (len(np.shape(img)) == 2):
    img = gray2rgb(img)
  return img

def change_contrast(img, k=0.035):
  """
  Applies an contrast factor to the original image, increasing or decreasing it.

  Parameters:
    img: image to change the contrast
    k: amount to increase/decrease contrast (greater = more intense)
  """
  # Handling greyscale images
  img = handle_double_channels_img(img)

  # convert the input image to HSV
  img_hsv = rgb2hsv(img)
  img_out = (255 / (1 + np.exp(-k * (img.astype(np.int32) - 127))))
  return img_out

def colorize(img, selected=0):
  """
  Applies an colormap to the original image.

  Parameters:
    img: image to change the contrast
    selected: the selected colormap to apply
      - 0. None
      - 1. Hot
      - 2. Inferno
      - 3. Twilight
      - 4. Rainbow
      - 5. Jet
  """

  img = handle_double_channels_img(img)

  cmap = None
  if (selected == 0):
    return img

  elif (selected == 1):
    cmap = plt.cm.hot
  
  elif (selected == 2):
    cmap = plt.cm.inferno
  
  elif (selected == 3):
    cmap = plt.cm.twilight
  
  elif (selected == 4):
    cmap = plt.cm.rainbow
  
  elif (selected == 5):
    cmap = plt.cm.jet
    
  x, y, z = np.shape(img)
  img_out = np.zeros((x, y, 3)).astype(np.uint8)

  # Applying colormap
  img_out = cmap(img)
  img_out = rgba2rgb(img_out)
  img_out = hp.trim_dimension(img_out)

  return img_out
  