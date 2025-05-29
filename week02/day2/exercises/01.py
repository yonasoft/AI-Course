import numpy as np

np.random.seed(32)
dataset = np.random.randint(2, 51, size=(5,5))
print(dataset)

dataset[dataset > 25] = 0
print(dataset)

print(np.sum(dataset))
print(np.mean(dataset))
print(np.std(dataset))