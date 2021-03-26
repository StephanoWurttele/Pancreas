import matplotlib.pyplot as plt
import pydicom
from pydicom import dcmread
from pydicom.data import get_testdata_file
import os

path = os.getcwd()

# create output file
output_file = open("data_header.txt", "w+")
# iterate in images
for filename in os.listdir(path):
    f = os.path.join(path,filename)
    print(f)
    ds = dcmread(f)
    output_file.write(filename + '\n')
    output_file.write(ds.top() + '\n' + '\n')

# ds = dcmread("../data/Pancreas-CT/PANCREAS_0021/11-24-2015-PANCREAS0021-Pancreas-81508/Pancreas-15844/1-002.dcm")
# print(ds)
# arr = ds.pixel_array

# plt.imshow(arr, cmap="gray")
# plt.show()
