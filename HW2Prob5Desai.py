import math

k = int(input("How many numbers do you want to go up to? "))

primeNumber = [True for i in range(k)]

primeNumber[0] = False
primeNumber[1] = False

for i in range(2, math.ceil(math.sqrt(k))):
    if(primeNumber[i] == True):
        square = i * i
        while square < k:
            primeNumber[square] = False
            square += i
for i in range(k):
    print("{} = {}".format(i, primeNumber[i]))