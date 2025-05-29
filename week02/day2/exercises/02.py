import numpy as np

rand_ints = np.random.randint(0,5, size=[3,3])
print(rand_ints)
print(np.sum(rand_ints, axis=1))
print(np.sum(rand_ints, axis=0))

rand_floats = np.random.rand(3,3)
print(rand_floats)

rand_floats = np.where(rand_floats < .5, 0, 1)
print(rand_floats)
