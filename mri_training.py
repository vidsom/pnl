# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:03:13 2017

@author: sk834
"""

#Import modules
from medpy.io import load
import matplotlib.pyplot as plt

#Load the image you want to visualize
image_data, image_header = load('/rfanfs/pnl-zorro/home/ju342/Python/DATA/case104_RTAP.nii')


#Loop through every slice
for x in range(1, image_data.shape[2]):
    axial_middle = x
    #This displays each image
    plt.figure('Showing the datasets')
    plt.subplot(1, 2, 1).set_axis_off()
    plt.imshow(image_data[:, :, axial_middle].T, cmap='gray', origin='lower')
    plt.show()

    

