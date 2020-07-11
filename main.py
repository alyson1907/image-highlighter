
import imageio
import matplotlib.pyplot as plt
import numpy as np
# Project modules
from filters import filter_appliers as f
from filters import helpers as hp
from filters import color_methods as color

# User inputs
filename = str(input("Enter the image name: "))
img = imageio.imread('images/' + filename)

# Handling third dimension of some Gray images
img = hp.trim_dimension(img)

selected_smoothing = int(input("Smoothing Filter number: "))
# Applying filter to the image
img_out = f.smoothing_filter(img, n=5, sigma=0.5, selected=selected_smoothing)

selected_edge = int(input("Edge Filter number: "))
# Applying filter to the image
img_out = f.edge_filter(img, n=3, sigma=1, selected=selected_edge)
img_out = hp.normalize(img_out)

# We apply the scalar if Sobel Operator is selected in order to turn white edges more visible
scalar = 4
img_out_restored = (img_out * scalar) if (selected_edge == 2) else img_out

selected_color = int(input("ColorMap number: "))
# Applying Color Filters
img_final = color.colorize(img_out_restored, selected=selected_color)
img_final = hp.normalize(img_final)

# img_final = color.change_contrast(img_final, k=0.025)

# Saving image
img_final = img_final.astype(np.uint8)
imageio.imwrite('out.png', img_final)
