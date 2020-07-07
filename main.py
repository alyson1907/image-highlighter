
import imageio
import matplotlib.pyplot as plt
import numpy as np
# Project modules
from filters import filter_appliers as f
from filters import helpers as hp
from filters import color_methods as color


# User inputs
# filename = str(input("Enter the image name: "))
# img = imageio.imread('images/' + filename)
img = imageio.imread('images/' + 'Hand-XRay/2.png')
# selected_smoothing = int(input("Smoothing Filter number: "))
# selected_edge = int(input("Edge Filter number: "))

# Handling third dimension of some images
img = img[:, :, 0] if (len(np.shape(img)) == 3) else img
img_out = color.change_contrast(img)

# # Applying filters to the image
# img_out = f.smoothing_filter(img, n=5, sigma=0.5, selected=selected_smoothing)
# img_out = f.edge_filter(img, n=3, sigma=1, selected=selected_edge)
# img_out = hp.normalize(img_out)

# # We apply the scalar if Sobel Operator is selected in order to turn white edges more visible
# scalar = 5
# img_out = (img_out * scalar) if (selected_edge == 2) else img_out

# Saving image
img_out = img_out.astype(np.uint8)
imageio.imwrite('out.png', img_out)
