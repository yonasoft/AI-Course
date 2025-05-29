import numpy as np

np.random.seed(42)

random_array = np.random.rand(3,3)
print(random_array)
random_int = np.random.randint(0, 10, size=[2,3])
print(random_int)