import numpy as np
# array properties

arr=np.array([[1,2,3],[4,5,6]])
print("shape:",arr.shape)
print("Dimension:",arr.ndim)
print("data Type:",arr.dtype)
print("size:",arr.size)

# Array Reshaping

arr1=np.arange(12)
print(arr1)

reshape=arr.reshape((2,3))
print("reshaped array: \n",reshape)

flatened=reshape.flatten()  #it return copy
print("flatened array: \n",flatened)

raveled=flatened.ravel() 
print("raveled array: \n",raveled)  #ravel returned vew insted of copy 

transpose=reshape.T
print("transpose array: \n",transpose)