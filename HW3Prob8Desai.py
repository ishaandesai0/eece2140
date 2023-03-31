import numpy as np

matrix1 = np.arange(2, 19, 2)
matrix1 = matrix1.reshape(3,3)
print("Matrix 1:\n", matrix1,"\n")

matrix2 = np.arange(9, 0, -1)
matrix2 = matrix2.reshape(3, 3)
print("Matrix 2:\n", matrix2,"\n")

product = np.zeros((3,3), dtype = int)

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            product[i][j] += matrix1[i][k] * matrix2[k][j]
  
print ("Product of Matrix 1 and Matrix 2 Matrix-wise:\n", product)
print ("Product of Matrix 1 and Matrix 2 Element-wise:\n", matrix1*matrix2)