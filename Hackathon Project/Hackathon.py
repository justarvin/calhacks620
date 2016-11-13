from PIL import Image, ImageChops
import numpy as np
import os
import math

def convertImage(filename):
	im = Image.open(filename)
	col, row = im.size
	data = np.zeros((row*col, row*col))
	pixels = im.load()
	print(type(pixels))
	for i in range(row):
		for j in range(col):
			r,g,b = pixels[i, j]
			data[i*col + j, :] = r, g, b, i, j
	return data
os.chdir("C:/Images")
"""print(convertImage("enroll_2016-11-11_22-38-59_00.bmp"))"""

def samePerson(string1, string2):
	keep1 = convertImage(string1)
	keep2 = convertImage(string2)
	count = 0
	for i in range(len(keep1)):
		for j in range(len(keep1[0])):
			if abs(keep1[i][j] - keep2[i][j]) < 100:
				count += 1
				if count >= 9000:
					return True
			j += 1
		i += 1
	return False

def finalTry(string1, string2):
	im1 = Image.open(string1)
	im2 = Image.open(string2)
	diff = ImageChops.difference(im2, im1)
	pixels = list(diff.getdata())
	count = 0
	for i in range(len(pixels)):
		count = count + pixels[i]
	count = count / len(pixels)
	if count < 90:
		return True
	return False
print(finalTry("enroll_2016-11-11_22-38-59_00.bmp", "enroll_2016-11-11_22-39-12_00.bmp"))