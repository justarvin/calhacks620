def addDataBase(array):
	f = open('keep.txt' , 'r+')
	f.write("test")
	f.write(array[0] + " " + array[1] +" " + array[2] + " "+ array[3]+"\n")

addDataBase(["a", "b", "c", "d"])