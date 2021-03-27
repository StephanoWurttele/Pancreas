import pydicom
from pydicom import dcmread
import numpy as np

# Dicom in npy
#url = "/content/drive/MyDrive/Colab Notebooks/images-test/tomografias1/1/patient11-19.dcm"
#ds_1 = dcmread(url)
#arr_1 = ds_1.pixel_array
#print(arr_1)

# Test mask
#x = np.array([[1,2],[2,3],[3,4]])
#mask = np.array([[0,1],[0,1],[0,1]]).astype(bool)
#x[np.array(mask)]


# Real mask
path=r"C:\Users\usuario\Desktop\Pancreas-CT\PANCREAS_0001\11-24-2015-PANCREAS0001-Pancreas-18957\Pancreas-99667"
import matplotlib.pyplot as plt
import pydicom
from pydicom import dcmread
from pydicom.data import get_testdata_file
import os
arr1=np.empty([240,512,512])
i=0
for filename in os.listdir(path):
    f = os.path.join(path,filename)
    ds = dcmread(f)
    arr1[i]=ds.pixel_array
    i+=1
no_segmentado = arr1
#print(no_segmentado)
segmentado = np.load(r'C:\Users\usuario\Downloads\01.npy')
print("Dimensiones segmentado", len(segmentado), len(segmentado[0]), len(segmentado[0][0]))
print("Dimensiones no_segmentado", len(no_segmentado), len(no_segmentado[0]), len(no_segmentado[0][0]))

arr2= np.array(segmentado)
arr3=np.multiply(arr1,arr2)
print(np.sum(arr3))
arr4=[[[1,1,1],[2,3,1],[5,4,3]]]
arr5=[[[8,6,5],[4,5,7],[3,4,5]]]
print(np.multiply(arr4,arr5))
