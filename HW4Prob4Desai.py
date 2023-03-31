import numpy as np

X = np.array([[7, 1, 5, 6], [2, 6, 1, 1], [6, 1, 7, 2], [6, 6, 3, 1], [5, 5, 6, 1], [3, 6, 7, 1]])
sizeMatrix = np.shape(X)
rows = sizeMatrix[0]
cols = sizeMatrix[1]
originalRow = X[0]
frequencyDict = {}
frequencyArray = []
trialArray = []

for i in range(cols):
    frequencyDict[X[0][i]] = 1
    
for j in X[1:]:
    for k in j:
        if k in frequencyDict.keys():
            frequencyDict[k] += 1

for i in originalRow:
    if frequencyDict[i] - 1 == len(X):
        frequencyArray.append(i)
    
print('X =',  X)
print('Common Elements:', frequencyArray)