# Image Highlighter
## Author
Alyson Matheus Maruyama Nascimento - 8532269

# Proposal
## Project Description
The main objective of this project is to implement a python code capable of processing grey-scaled images to improve its visibility. In order to achieve that, both **image restoration and colorizing filters** will be applied to the images so that the output images has an better overall visibility, highlighting their most important sections. 

## Application Area
The program should be able to perform well with any grey-scaled image containing distinction of borders and objects to the human eye.  

As an example of medical application, the program must be able to highlight the blood vessels within an [Angiography](https://en.wikipedia.org/wiki/Angiography) or the bones in an [X-Ray](https://en.wikipedia.org/wiki/X-ray) image.

Another application example would be to run the program over X-ray images of vehicles crossing country borders, so that it becomes easier to identify illegal immigrants or criminal drug trafficking.

## Example Images
The following images are good examples of what kind of input images the program should be able to handle:

| Cerebral Angiography | Lateral Elbow Radiography | Illegal Drugs |
| --- | --- | --- | 
|![](./demo/img/cerebral_angiography.jpg)|![](./demo/img/lateral_elbow.jpg)| ![](./demo/img/border_vehicles.png) |

# Partial Report
## Main Objective
As briefly described before, the main objective of this project is to implement a Python program that will apply image processing techniques 
in order to improve visibility of the original image.

Although the objective is to create a generic program that will be able to handle any grayscale image, the Datasets used by this repository
consist only by X-Ray images.

## Datasets
In this project, we use two kind of images: the first one consists in chest X-Rays from patients affected by COVID-19's suffering from pneumonia, while the second one consists in X-Rays from hands.

Both of them were downloaded from **Kaggle.com**: a website that offers open and free datasets and machine learning projects.

The selected datasets can be found in the following links:
- COVID-19 Radiography: https://www.kaggle.com/tawsifurrahman/covid19-radiography-database?
- Hand Bone Age: https://www.kaggle.com/kmader/rsna-bone-age/data?

**Here are some examples:**

 <div float="left" align="middle">
  <img src="./images/COVID-19-Pneumonia/1.png" height="300">
  <img src="./images/Hand-XRay/2.png" height="300">
 </div>

# How it Works
> **NOTE:** when running the program, the user must specify what filters to be applied in each step

### Step 1 - Image Enhancement
The first step is to apply some Smoothing filter to the original image in order to reduce possible noises. This repository implements 2 filters of this type:

1. Median Filter [read more](https://en.wikipedia.org/wiki/Median_filter)
2. Gaussian Filter [read more](https://en.wikipedia.org/wiki/Gaussian_filter)

### Step 2 - Edge Detection
After that, using the pre-processed image from the step before, in order to improve overall visibility of the image, we apply some Edge Detection filter.  
The user can select one of the following:

1. Laplacian of Gaussian [read more](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)
1. Sobel Operator [read more](https://en.wikipedia.org/wiki/Sobel_operator)

>**NOTE:** For the last one (Sobel Operator), the program will apply a default `scalar` value to the normalized output image in order to increase white pixels intensity. Feel free to set the scalar value to **1** to disable it and see the raw result from the Sobel filter

### Step 3 - Normalizing
The program normalizes the image (the implementation of the normalizer function is located at `helpers.py` file)

### Step 4 - Showing the Results
The final step is to show the final image.

If you are running the Jupyter Notebook, the output image will be displayed in the own Notebook, but if you're running the program by the `main.py` file, it should save the output image to the root directory of this project (default file name: `out.png`).

## Examples 
The images below represent two types of processing applied to the same image from our dataset:

| Original Image | Gaussian Filter + LoG | Gaussian Filter + Sobel |
| -- | -- | --|
| <img src="./images/Hand-XRay/2.png" height="300"> | <img src="./demo/smoothing_results/hand_LoG.png" height="300"> | <img src="./demo/smoothing_results/hand_sobel.png" height="300"> |

Now applying the same filters to an image in our `demo/` folder (containing some random images from the internet):

| Original Image | Gaussian Filter + LoG | Gaussian Filter + Sobel (`scalar=1`) |
| -- | -- | --|
| <img src="./demo/img/cerebral_angiography.jpg" height="300" width="300"> | <img src="./demo/smoothing_results/cerebral_LoG.png" height="300" width="300"> | <img src="./demo/smoothing_results/cerebral_sobel.png" height="300" width="300"> |
