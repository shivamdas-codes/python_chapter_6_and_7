# reading from a file:
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
file.close()
# in the 3rd case the next line will show as empty beacause all the data is already read so there is no data left to read so it will show as empty line in the end.


# writing to a file:
file = open("file1.txt","w")
file.write("hello im intrested in open source......") #this will override the previous data in the file.
file.write("contributing to real world projects") #this will be added to the previous line without any space or new line.
file.write("\nhey there how are you") #this will be added to the previous line with a new line.
file.close()

# appending to a file:
file = open("sample.txt","a")   #if there is no file with the name sample.txt it will create a new file with that name.
file.close()


# read and write both:    r+
f = open("sample.txt", "r+")
# f.write("hey there how are you")  #this will write at the begining of the file.
f.write("hello")    #this will override the first 5 letters of the file.
data = f.read()   #this will read the file from where the write operation ended.
print(data)
f.close()

# read and write both: w+
f = open("sample.txt", "w+")
f.read()  #this will not read anything as the file is opened in write mode and the file is empty.
f.write("hello world")  #this will write "hello world" to the file.
f.close()

# read and write both: a+
f1 = open("sample.txt", "a+")
f1.read()  #this will not read anything as the file is opened in write mode and the file is empty.
f1.write("hey")  #this will append "hey" to the file.
f1.close()

