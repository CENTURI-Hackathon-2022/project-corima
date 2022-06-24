#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 19:34:09 2022

@author: kateriniovi
"""


from skimage import io
import os
import matplotlib.pyplot as plt
import numpy as np

# io.use_plugin('pil')
# img1 = io.imread('20220117_E2_Cell8BF.tif')

# plt.imshow(img1)
# plt.show()

# img2 = io.imread('topo_20220107_Exp2Cell8map-data-2022.01.07-16.34.34.510_processed-2022.01.10-12.38.51.tif')

# plt.imshow(img2)
# plt.show()

# print(img1)

# 10x : 1022 nm/px (JPK camera) - not sure we can really be precise at the nm for this one.
# 20x: 506 nm/px (JPK camera)

from PIL import Image
im = Image.open('20220117_E2_Cell8BF.tif')
plt.imshow(im)
pix = np.array(im)
print(pix)



#fjxhfksdh

# import numpy as np
# imarray = np.array(image)
# imarray


# import numpy
# imarray = numpy.array(im)
# print(imarray.shape)

# from PIL import image
# from skimage import io
# io.use_plugin('pil')
# images = os.listdir(train_data_path)
# for image_name in images:
#     img = io.imread(os.path.join(train_data_path, image_name))