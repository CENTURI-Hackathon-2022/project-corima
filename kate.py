#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 19:34:09 2022

@author: kateriniovi
"""


import io
import os
import matplotlib.pyplot as plt
import numpy as np




import tifffile as tiff
import cv2
a = tiff.imread('topo_20220107_Exp2Cell8map-data-2022.01.07-16.34.34.510_processed-2022.01.10-12.38.51.tif')
#im1 = Image.open('topo_20220107_Exp2Cell8map-data-2022.01.07-16.34.34.510_processed-2022.01.10-12.38.51.tif')
b = tiff.imread('20220117_E2_Cell8BF.tif')

im = cv2.imread('a.tif', -1)
print(a)
print(b)

# from numba import jit
# @jit(nopython=True,parallel=True)


# def dif_mat(M1,M2):
#         for i in range(M1.shape[0],140):
#             for j in rangerange(M1.shape[1],140):
                





def distance_two_images(im1, im2):
    """ the euclidean square distance of two images in terms of intensity is calculated
    :im1 np.array of the big image
    :im2 np.array of the small image   """
    
    (height, width) = np.shape(im1)
    (h, w) = np.shape(im2)
    d = np.empty((height - h, width - w))
    
    for row in range(height - h):
        for col in range(width - w):
            d[row,col] = np.sum( np.square( np.subtract(im1[0+row : h+row, 0+col : w+col] , im2) ))
    
    return d
    

def position_of_min(d):
    """ determine the position of minimum
    :d np.array of distances """
    
    result = np.where(d == np.amin(d))
    print("the minimum distance is: ", np.amin(d))
    print('Tuple of arrays returned : ', result)
    
    return result



distanc = distance_two_images(b, a)
res = position_of_min(distanc)


