from PIL import Image, ImageChops
import numpy as np
import os
import math

class Runner:

	os.chdir("C:/Images")
	
	database = {}

	"""Constructs the database, takes in a list of URLs, list of usernames and list of listPasswords
	"""
	def __init__(self, filename, listURLs, listUsernames, listPasswords):
		self.database = { x : y for x,y in zip(listURLs, zip(listUsernames, listPasswords))}
		self.masterkey = filename

	"""Add another entry into the database."""

	def addDataBase(self, websiteurl, username, password):
		self.database[websiteurl] = (username, password)

	"""Compares the filenames of two prints, should be used to compare most recent against
	master key."""
	def compareTo(self, string1, string2):
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
	

	"""Finds the most recent image scanned by the finger print scanner"""
	os.chdir("C:\Images")
	def findRecent(self):
		x= 0
		keepdict = {}
		name = [filename for filename in os.listdir()]
		time = [os.stat(filename).st_mtime for filename in os.listdir()]
		keepdict = {key: value for (key, value) in zip(time, name)}
		keeper = sorted(keepdict)
		print(keepdict[keeper[-1]])
		return keepdict[keeper[-1]]

	"""Use to retrieve the username and password of the dictionary, assumes that compareTo 
	returns True."""

	def getUsername(self, website):
		return self.database[website][0]

	def getPassword(self, website):
		return self.database[website][1]

	def getUserNameList(self):
		return [self.database[x][0] for x in list(self.database.keys())]

	def getPasswordList(self):
		return [self.database[x][1] for x in list(self.database.keys())]

	
