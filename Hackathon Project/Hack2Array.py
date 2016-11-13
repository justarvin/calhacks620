import os
from PIL import Image
import numpy as np

def toByteArray(filename):
	with open(filename, "rb") as imageFile:
		f = imageFile.read()
		b = bytearray(f)
	return b
os.chdir("C:/Images")
toByteArray("enroll_2016-11-11_22-38-59_00.bmp")
def compareTo(filename1, filename2):
	array1 = toByteArray(filename1)
	array2 = toByteArray(filename2)
	count = 0
	for i in range(len(array1)):
		if array1 == array2:
			count += 1
		if count > len(array1)/1000. :
			return True
		i += 1
	return False



def toArray(filename):
	im = Image.load(filename)
	im = im.convert('L')

	arr = np.fromiter(iter(im.getdata()), np.uint8)
	arr.resize(im.height, im.width)
	print(arr)
print(toArray("enroll_2016-11-11_22-38-59_00.bmp"))

		
