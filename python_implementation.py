import numpy as np

matrix = np.array([
    [15, -2, -3, -1, 0, -6],
    [-2,-15, 0,  1, 3,   8],
    [ 3, -9, 0,  2, 0, -15],
    [ 1,  1, 2, -6, 2,   0],
    [ 0,  3, 0,  2, -9, 16]
]).astype(float)



_, cols = matrix.shape

# the amount of iterations we need is exactly the number of columns minus 1
for j in range(cols - 1):
    i = j
    MaxInCol = matrix[np.argmax(matrix.abs[i, j:])]

    
    
    