import pydicom
from pydicom import dcmread
import pylibjpeg
import numpy as np

# Dicom in npy
url = "/content/drive/MyDrive/Colab Notebooks/images-test/tomografias1/1/patient11-19.dcm"
ds_1 = dcmread(url)
arr_1 = ds_1.pixel_array
print(arr_1)

# Test mask
x = np.array([[1,2],[2,3],[3,4]])
mask = np.array([[0,1],[0,1],[0,1]]).astype(bool)
x[np.array(mask)]


# Real mask
no_segmentado = np.load("/content/drive/MyDrive/Colab Notebooks/numpys/no_segmentado/0016.npy")
#print(no_segmentado)
segmentado = np.load("/content/drive/MyDrive/Colab Notebooks/numpys/segmentado/16.npy")
print("Dimensiones segmentado", len(segmentado), len(segmentado[0]), len(segmentado[0][0]))
print("Dimensiones no_segmentado", len(no_segmentado), len(no_segmentado[0]), len(no_segmentado[0][0]))


# Esta linea es la que no funciona por dimensiones
#no_segmentado[np.array(segmentado.astype(bool))]
