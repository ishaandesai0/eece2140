def convertNumber(num):  
    if num == "zero":
        return 0
    if num == "one":
        return 1
    if num == "two":
        return 2
    if num == "three":
        return 3
    if num == "four":
        return 4
    if num =="five":
        return 5
    if num =="six":
        return 6
    if num =="seven":
        return 7
    if num =="eight":
        return 8
    if num =="nine":
        return 9

def convertOperator(op): 
    if op == "plus":
        return '+'
    if op == "minus":
        return '-'
    if op == "times":
        return '*'
    if op == "divided by":
        return '/'

def solveExpression(num1, oper, num2):
    if oper =='+':
        return num1 + num2
    if oper =='-':
        return num1 - num2
    if oper =='*':
        return num1 * num2
    if oper =="/":
        return num1 / num2

equation = input("Enter the expression you wish to calculate:")
list = equation.split()

if len(list) == 4:
    list[1] += " by"
    del list[2]

num1 = convertNumber(list[0])
operator = convertOperator(list[1])
num2 = convertNumber(list[2])

print(solveExpression(num1, operator, num2))