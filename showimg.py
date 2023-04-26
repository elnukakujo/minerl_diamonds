from matplotlib import pyplot as plt
import numpy as np

X = np.load("X_tree.npy")
print(X.shape)

plt.imshow(X[1])
plt.show()