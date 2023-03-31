number1 = int (input ("Enter number to see if it is a palindrome: "))

number2 = number1
reverseNumber = 0
while(number2 > 0):
    numRemainder = number2 % 10
    reverseNumber = (reverseNumber * 10) + numRemainder
    number2 = number2 // 10

if reverseNumber == number1:
    print("This number is a Palindrome!")
else:
    print("This number is not a Palindrome!")

a = 14 // 3 ** 2 * 2 ** 3 ** 2 / 2 % 5
print(a)

print('Imagine' <= 'book')