file1=open("sample.txt","r")
reading_line1=file1.readlines(1)
reading_line2=file1.readlines(2)
print("Reading file contents:")
print("Line 1: ",reading_line1)
print("Line 2: ",reading_line2)
file1.close()

try:
    file1=open("sample1.txt","r")
    reading_file1=file1.read()
    print(reading_file1)
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")

