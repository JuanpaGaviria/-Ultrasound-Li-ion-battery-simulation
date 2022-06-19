import numpy as np
mat = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(mat.shape)
for i in range(mat.size):
    for j in range(mat.size):
        if mat[i,j] == 5:
            print("hola mundo")
            print(i,j)
