import os
# create a demo2.txt in the same foleder
try:
    if os.path.exists("File handling/demo2.txt"):
        os.remove("File handling/demo2.txt")
        print("file deleted successfully") 
except Exception as err:
    print("something wrong",err)


# To delete an entire folder, use the os.rmdir() method:
