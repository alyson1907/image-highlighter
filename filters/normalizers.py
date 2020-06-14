import numpy as np

# Normalizes an image.
# params:
#   img: input image to be normalized
def normalize(img):
    img = img.astype(float)
    return (255 * (img - np.min(img)) / (np.max(img) - np.min(img))).astype(np.uint8)
