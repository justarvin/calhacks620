from PIL import Image, ImageChops
import numpy as np
import os
import math

class Runner:

	os.chdir("C:/Images")
	
	database = {}
	def __init__(self, filename, listURLs, listUsernames, listPasswords):
		self.database = { x : y for x,y in zip(listURLs, zip(listUsernames, listPasswords))}
		self.masterkey = filename

	def addDataBase(websiteurl, username, password):
		self.database[wibsiteurl] = (username, password)


	def compareTo(string1, string2):
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
	print(compareTo("enroll_2016-11-11_22-38-59_00.bmp", "enroll_2016-11-11_22-39-12_00.bmp"))


	os.chdir("C:\Images")
	def findRecent():
		x= 0
		keepdict = {}
		name = [filename for filename in os.listdir()]
		time = [os.stat(filename).st_mtime for filename in os.listdir()]
		keepdict = {key: value for (key, value) in zip(time, name)}
		keeper = sorted(keepdict)
		print(keepdict[keeper[-1]])
		return keepdict[keeper[-1]]

	def getUsername(website):
		return self.database[website][0]

	def getPassword(website):
		return self.database[website][1]

	
