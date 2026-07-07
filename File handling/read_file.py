#Theere is two of synrax for read a file

# Syntax-1
file=open("File handling/file.txt")
print(file.read())
file.close()

# Syntax-2
with open("File handling/file.txt") as f:
    print(f.read())
    f.close()