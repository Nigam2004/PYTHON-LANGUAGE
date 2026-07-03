import numpy as np

arr=np.arange(12)
print(arr)

print("basic slicing:",arr[1:5])
print("with step:",arr[1:10:3])
print("negetive indexing:",arr[-1])


arr_2d=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print("specific alement:",arr_2d[1,2])
print("entire row:",arr_2d[1])
print("entire column:",arr_2d[:,1])