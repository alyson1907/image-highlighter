# NOTE: This File contains general helper functions used in multiple files along the project

import matplotlib.pyplot as plt
import numpy as np

def trim_dimension(img):
  """
  Params:
      img: image to be reshaped
  """

  shape = np.shape(img[:-1])

  if (len(shape) == 3): 
    return img[:, :, 0]

  elif (len(shape) == 4):
    return img[:, :, 0 , :]

  return img

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

def printImg(*imgs, size=10):
  """
  Prints multiple images side by side.

  Parameters:
  imgs: Array of images to be shown
  """
  if (len(imgs) == 1):
    plt.rcParams['figure.figsize'] = [size, size]
    plt.imshow(imgs[0], cmap="gray")

  else: 
    _, axs = plt.subplots(1, len(imgs), figsize=(size, size))
    axs = axs.flatten()

    for img, ax in zip(imgs, axs):
      ax.imshow(img, cmap="gray")

  plt.show()
