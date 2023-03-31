def listFunction(nums):
    nums.sort()
    numberDictionary = {}
    for currentNumber in nums:
        if currentNumber not in numberDictionary:
            numberDictionary[currentNumber] = 1
        else:
            numberDictionary[currentNumber] += 1
        newNumber = list(set(nums))
        newNumber.reverse()
        return numberDictionary, newNumber
num1 = [3, 5, 4, 3, 1, 4, 1, 4]
function = (listFunction(num1))
myDictionary = function[0]
myArray = function[1]
print(myDictionary, myArray)
for key, value in myDictionary.items():
    print('Number: ', key, "Count: ", value)
myArray = set(myArray)
newSet1 = set()
for x in range (1, max(myArray)):
    if x not in myArray:
        newSet1.add(x)
print(newSet1)