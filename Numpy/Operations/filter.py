import numpy as np

arr=np.array([4,5,63,2,8,4,65,5,5])
even_number=arr[arr%2==0]
print("even number:",even_number)

#filter with mask 
mask=arr>5
print("number which is greater than 5/mask:",arr[mask])

#fancy indexing vs np.where()

index=[0,2,3]
print("fancy indexing:",arr[index])

where_index=np.where(arr>5)
print(where_index)
print("where indexing:",arr[where_index])

conditon_arr=np.where(arr>5,True,False)
print(conditon_arr)