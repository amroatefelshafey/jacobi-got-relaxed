import numpy as np
import timeit
np.set_printoptions(linewidth=10000)

matrix = np.array([
    [15, -2, -3, -1, 0, -6],
    [-2,-15, 0,  1, 3,   8],
    [ 3, -9, 0,  2, 0, -15],
    [ 1,  1, 2, -6, 2,   0],
    [ 0,  3, 0,  2, -9, 16]
]).astype(float)

rows, cols = matrix.shape


rows, cols = matrix.shape
# the amount of iterations we need is exactly the number of columns minus 1
print(f"matrix before change\n {matrix}\n\n")
for j in range(cols - 1):
    i = j
    MaxInCol = i +  np.argmax(np.abs(matrix[i:, j]))
    #print(f"Row Index of Max in column: {MaxInCol}, current i={i}")
    #check if the max is not in the current row, if not? swap them
    if MaxInCol != i:
      matrix[[i, MaxInCol]] = matrix[[MaxInCol, i]]
    # this should divide the value of the element in the diagonal position
    # by the entire row, normalizing the value to 1
    matrix[j] = matrix[j] / matrix[j, j]
    for i in range(rows):
      if i == j:
        continue
      matrix[i] = matrix[i] - (matrix[i, j] * matrix[j])

print(f"matrix after change\n {matrix}")

