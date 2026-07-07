
#"w" - Write: for over writing in an existing file
with open("File handling/file.txt","w") as f:
    f.write(" hii I am raj")
with open("File handling/file.txt") as f:
    print(f.read())


#for create an new file
with open("File handling/demo.txt","w") as f_d:
    f_d.write("hii i am demo file")
with open("File handling/demo.txt") as f_d:
    print(f_d.read())

#"a" - Append: will append to the end of the file
with open("File handling/file.txt","a") as f:
    f.write(" and nigam ")
with open("File handling/file.txt") as f:
    print(f.read())


# "x" - Create:will create a file, returns an error if the file exists
with open("File handling/file.txt","x") as f:
    print(f.read())
#gives an error