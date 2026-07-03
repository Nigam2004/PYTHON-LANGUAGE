import numpy as np

Unsort_arr=np.array( [1,4,3,7,2,11,4,6,7,9])

print("sorted array:",np.sort(Unsort_arr))

arr_2d_us=np.array([[3,2],
                    [5,6],
                    [7,4]])
print("2d array sorted:\n",np.sort(arr_2d_us,axis=0)) # sorted in column wise
print("2d array sorted:\n",np.sort(arr_2d_us,axis=1)) # sorted in row wise