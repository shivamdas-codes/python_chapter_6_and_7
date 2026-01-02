f = open("file.txt", "r")

data = f.read(5)    #the value inside the read() inicates to read the first 5 letters in the text file.
read_line = f.readline()    #this line indicates to read the first line

print(data)
print(read_line)
print(type(data))
print(len(data))
f.close()

