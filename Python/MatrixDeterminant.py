import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

m = [[2,5,3], [1,-2,-1], [1, 3, 4]]
m1 = [[4]]
print(determinant(m1))