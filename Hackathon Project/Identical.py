from PIL import Image, ImageChops
import numpy as np
import os
import math
from flask import Flask
app = Flask(__name__)

'''class Runner:'''



'''database = {} '''

"""Constructs the database, takes in a list of URLs, list of usernames and list of listPasswords
"""
'''@app.route('/initialize')
def __init__(self, array):
	self.masterkey = array[0]'''


"""Add another entry into the database."""

@app.route('/database')
def addDataBase(array):
	f = open('keep.txt' , 'a+')
	f.write(array[0] + ", " + array[1] +", " + array[2] + ", "+ array[3]+"\n")
	

"""Compares the filenames of two prints, should be used to compare most recent against
master key."""
addDataBase(["fingerprint", "www.facebook.com", "saroj", "swag"])
addDataBase(["fingerprint2", "www.gmail.com", "justin", "12345"])
holder = np.loadtxt('keep.txt', list, delimiter = ', ').astype(str)
print(holder[0][0])



@app.route('/compareTo')
def compareTo(website):
	os.chdir("C:\Images")
	im1 = Image.open(findRecent())
	holder = np.loadtxt('keep.txt', list, delimiter = ', ').astype(str)
	for x in holder:
		count = 0
		im2 = Image.open(x[0][2:-1])
		diff = ImageChops.difference(im2, im1)
		pixels = list(diff.getData())
		for i in range(len(pixels)):
			count = count + pixels[i]
		count = count / len(pixels)
		if count < 90:
			if str(x[1][2:-1]) == website:
				return [x[2][2:-1], x[3][2:-1]]
	os.chdir("C:\Users\JSWAG JSWAG\Desktop\calhacks620\Hackathon Project")
	return "Not in database"


"""Finds the most recent image scanned by the finger print scanner"""

@app.route('/findRecent')
def findRecent():
	os.chdir("C:\Images")
	x= 0
	keepdict = {}
	name = [filename for filename in os.listdir()]
	time = [os.stat(filename).st_mtime for filename in os.listdir()]
	keepdict = {key: value for (key, value) in zip(time, name)}
	keeper = sorted(keepdict)
	print(keepdict[keeper[-1]])
	os.chdir("C:\Users\JSWAG JSWAG\Desktop\calhacks620\Hackathon Project")
	return keepdict[keeper[-1]]

"""Use to retrieve the username and password of the dictionary, assumes that compareTo 
returns True."""





@app.route('/username')
def getUsername(website):
	holder = np.loadtxt('keep.txt', list, delimiter = ', ')
	for x in holder:
		if str(x[1][2:-1]) == website:
			return x[2][2:-1]
print(getUsername('www.facebook.com'))






@app.route('/password')
def getPassword(website):
	holder = np.loadtxt('keep.txt', list, delimiter = ', ')
	for x in holder:
		if str(x[1][2:-1]) == website:
			return x[3][2:-1]
print(getPassword('www.facebook.com'))


@app.route('/url')
def getURLS():
	holder = np.loadtxt('keep.txt', list, delimiter = ', ')
	return [x[1][2:-1] for x in holder]
print(getURLS())
'''
def getUserNameList(self):
	return [self.database[x][0] for x in list(self.database.keys())]

def getPasswordList(self):
	return [self.database[x][1] for x in list(self.database.keys())]
'''

if __name__ == "__main__":
app.run()
