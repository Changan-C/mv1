import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from pylab import  *
import os

import cv2

##im = cv2.imread('goodluck.jpg')
im = Image.open('goodluck.jpg')
im = np.array(im)
##cv2.imshow('original',im)
##cv2.waitKey(0)
##t =type(im)
##s = im.shape
##print(t,s)
print(im)
img = im.resize(800, 800)
img.save('goodlk.png')


