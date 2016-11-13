import os
os.chdir("C:\Images")
x= 0
keepdict = {}

name = [filename for filename in os.listdir()]
time = [os.stat(filename).st_mtime for filename in os.listdir()]
keepdict = {key: value for (key, value) in zip(time, name)}
keeper = sorted(keepdict)
print(keepdict[keeper[-1]])

    
