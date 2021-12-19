import numpy as np 
import cv2 as cv
from numpy import asarray

def obj_size(imagePaths):

    imgg = cv.imread(imagePaths)
    image_arr = asarray(imgg)

    result = (len(image_arr[image_arr != 255]))/1000

    return result
