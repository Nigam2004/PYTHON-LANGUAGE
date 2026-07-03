import numpy as np

#CREATING ARRAYS
zeros=np.zeros((2,3))
print("zeros array \n:",zeros)

ones=np.ones((2,3))
print("ones array \n:",ones)

full=np.full((2,3),7)
print("full array \n:",full)

random=np.random.random((1,1))
print("Random array \n:",random)

sequence=np.arange(0,11,2)
print("sequence array \n:",sequence)

#VECTOR, MATRIX, TENSOR
vector=np.array([10,20,30,40]) #1D array
print("1d array/vector: \n",vector)


matrix=np.array([[10,20,30,40],
                 [50,60,70,80]])  #2D array
print("2d array/matrix: \n",matrix)

tensor=np.array([[[1,2],[3,4]], #3D array
                 [[5,6],[7,8]]])
print("3d array/tensor: \n",tensor)