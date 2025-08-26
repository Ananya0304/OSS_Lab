import numpy as np
array1=np.array([0,10,20,40,60])
array2=np.array([10,30,40,50,70])
print("Array 1: ",array1)
print("Array 2 ",array2)
res=np.column_stack((array1,array2))
print(res)