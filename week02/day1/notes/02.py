import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape((2,3))
#print(reshaped)

arr = np.array([1,2,3])
expanded = arr[:, np.newaxis]
#print(expanded)
