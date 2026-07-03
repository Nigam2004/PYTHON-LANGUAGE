
import numpy as np

# Array Reshaping

arr1=np.arange(12)
print("original arra:",arr1)

reshape=arr1.reshape(3,4)
print("reshaped array: \n",reshape)

flatened=reshape.flatten()  #it return copy
print("flatened array: \n",flatened)

raveled=flatened.ravel() 
print("raveled array: \n",raveled)  #ravel returned vew insted of copy 

transpose=reshape.T
print("transpose array: \n",transpose)