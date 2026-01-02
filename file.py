f = open("file.txt", "r")

data = f.read(5)    #the value inside the read() inicates to read the first 5 letters in the text file.
read_line = f.readline()    #this line indicates to read the first line

print(data)
print(read_line)
print(type(data))
print(len(data))
f.close()



file = open("file.txt","r")
data1 = file.readline()
print(data1)
data2 = file.readline()
print(data2)

data3 = file.readline()
print(data3)
# in the 3rd case the next line will show as empty beacause all the data is already read so there is no data left to read so it will show as empty line in the end.



