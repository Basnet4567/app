file =open("read.txt", "r")
print(file.readable()) #readable or not (true or false)
#print(file.readline()) #read 1 line and print
#print(file.readline())
#print(file.readline())


#readlines() multiple line
#print(file.readlines())

#write 
file_write = open("file_write.txt","a")
file_write.write("\nwrite file for the second time") 
file.close()
