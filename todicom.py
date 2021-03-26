from pylab import *
import SimpleITK as sitk
import PIL.Image as image
import numpy as np
import os
import sys

def open_npy(namefile): 
    npy = np.load(namefile)
    return npy

def generate_files(npy_array):     
    i = 0 
    for shape in npy_array:
        image = sitk.GetImageFromArray((shape*255).astype(np.uint8))
        name = str(i) + '.dcm'
        image.SetMetaData("0010|0010", "SEGMENTATION_0")
        image.SetMetaData("0010|0020", "SEGMENTATION_0")
        image.SetMetaData("0020|0013", str(i))
        image.SetMetaData("0008|1030","PANCREAS_SEG")
        image.SetMetaData("0008|103e","PANCREAS_SEG")
        image.SetMetaData("0020|0010","PANCREAS_SEG_0")
        image.SetMetaData("0020|0011","0")
        image.SetMetaData("0020|000d","1.2.826.0.1.3680043.2.1125.1.49694013610161324925937323557017337")
        image.SetMetaData("0020|000e","1.2.826.0.1.3680043.2.1125.1.53952351705296904147440961031683501")
        sitk.WriteImage(image, name)
        print('File ' + name + ' generated.')
        i += 1

namefile = sys.argv[1]
npy = open_npy(namefile)
generate_files(npy) 

