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
import PIL
from PIL import Image
from PIL.TiffTags import TAGS
im = Image.open('topo_20220107_Exp2Cell8map-data-2022.01.07-16.34.34.510_processed-2022.01.10-12.38.51.tif')
plt.imshow(im)

pix = np.array(im)

# meta_dict = {TAGS[key] : im.tag[key] for key in im.tag_v2}
# meta_dict
# info_dict = {
#     "Filename": im.filename,
#     "Image Size": im.size,
#     "Image Height": im.height,
#     "Image Width": im.width,
#     "Image Format": im.format,
#     "Image Mode": im.mode,
#     "Image is Animated": getattr(im, "is_animated", False),
#     "Frames in Image": getattr(im, "n_frames", 1),
#     "info": im.info
# }

# for label,value in info_dict.items():
#     print(f"{label:25}: {value}")

print(PIL.__version__)
exifdata = im.getexif()

for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
    
for label,value in exif():
    print(f"{label:25}: {value}")


# import tifffile as tiff
# import cv
# a = tiff.imread('topo_20220107_Exp2Cell8map-data-2022.01.07-16.34.34.510_processed-2022.01.10-12.38.51.tif')
# im = cv2.imread('a.tif', -1)


# print(pix)
# meta_dict = {TAGS[key] : im.tag[key] for key in im.tag_v2}
# print(meta_dict)
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