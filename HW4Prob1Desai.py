import numpy as np

matrixA = np.arange(1, 21)
numRows = 5
numCols = 4
matrixB = matrixA.reshape(numRows, numCols)
matrixC = matrixB.T

for i in reversed(range(1, numCols)):
    print(np.diagonal(matrixB, i))
for i in range(0, len(matrixB)):
    print(np.diagonal(matrixC, i))