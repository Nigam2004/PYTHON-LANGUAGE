import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

add_arr=np.concatenate((arr1,arr2))
print(add_arr)

##vstack is used add array in vertically(row wise)

original=np.array([[1,2],[5,6]])
new_arr=np.array([8,5])
vertical_arr=np.vstack((original,new_arr))
print("vertical adding array: \n",vertical_arr)

##hstack is used add array in horizental (column wise)

original_h=np.array([[1,2],[5,6]])
new_arr_h=np.array([[8,5],[7,9]])
horizental_arr=np.hstack((original_h,new_arr_h))
print("horizentaly adding array:\n",horizental_arr)

#DELETION OF DATA FROM AN ARRAY

arr=np.array([4,5,63,2,8,4,65,5,5])
deleted_arr=np.delete(arr,2)
print("deleted array:",deleted_arr)