file=open("output.txt","w")
write=str(input("Enter text to write to the file: "))
writing_file=file.write(write+"\n")
file.close()
if writing_file==len(write)+1:'''1 is for \n like hi is 2 +1 for \n and 
len because the output of write is in the number'''
    print("Data successfully written to output.txt")
else:
    print("Data successfully not written to output.txt")
file=open("output.txt","a")
append=str(input("Enter additional text to append: "))
appending_file=file.write(append)
file.close()
if appending_file==len(append):
    print("Data successfully appended")
else:
    print("Data successfully not appended")
file=open("output.txt","r")
reading_file=file.read()
print("Final contents of output.txt:")
print(reading_file)
file.close()

