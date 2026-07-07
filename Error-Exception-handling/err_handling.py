
##Example-1
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
    

##Example-2

try:
    f_open=open("Error-Exception handling/Dommy.txt")
    print("file opened successfully")
    try:
        f_open.write("hii")
        # print(w_file)
    except Exception as error :
        print(f"erro occure when writing the file{error}")
    finally:
        f_open.close()
except:
    print("something went wrong when openig the file")

    