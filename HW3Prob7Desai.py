import re

converstionQuestion = str(input("Enter the expression to be converted\n"))

typesofLength = 'Inches | Foot | Feet | Yards | Milimeters | Centimeters | Meters | Kilometers'
typesofWeight = 'Ounces | Pounds | Miligrams | Grams | Kilograms'
typesofVolume = 'Cups | Quarts | Gallons | Mililiters | Liters | Kiloliters'
numbers = '[0-9]+'

lengthMatch = re.findall(typesofLength, converstionQuestion, re.IGNORECASE)
weightMatch = re.findall(typesofWeight, converstionQuestion, re.IGNORECASE)
volumeMatch = re.findall(typesofVolume, converstionQuestion, re.IGNORECASE)
numberMatch = re.findall(numbers, converstionQuestion, re.IGNORECASE)

dictLength = {'Inches': 0.0833, 'Yards': 3, 'Milimeters': .0033, 'Centimeters': .033, 'Meters': 3.3, 'Kilometers': 3280.9, 'Foot': 1, 'Feet': 1} 
dictWeight = {'Ounces': 0.0625, 'Miligrams': 0.0000022, 'Grams': 0.0022, 'Kilograms': 2.205, 'Pounds': 1 }
dictVolume = {'Cups': .25, 'Gallons': 4, 'Mililiters': 0.0011,  'Liters': 1.06,  'Kiloliters': 1056.7, 'Quarts': 1}

if (bool(lengthMatch) == True) and (bool(weightMatch) == True):
    print("Enter units with the same measurement, try again!")
elif (bool(lengthMatch) == True and bool(volumeMatch) == True):
    print("Enter units with the same measurement, try again!")
elif (bool(weightMatch) == True and bool(volumeMatch) == True):
    print("Enter units with the same measurement, try again!")
else:
   
    valueList = []
    numbersArray = []
    
    for x in numberMatch:
        numbersArray.append(int(x))
    if bool(lengthMatch) == True:
        for x in lengthMatch:
            if x in dictLength.keys():
                valueList.append(dictLength.get(x))
        conversion = (valueList[1]/(valueList[0])*numbersArray[0])
        print("Per calculations, there are", conversion, lengthMatch[0], "in", numbersArray[0], lengthMatch[1])
    
    if bool(weightMatch) == True:
        for x in weightMatch:
            if x in dictWeight.keys():
                valueList.append(dictWeight.get(x))
        conversion = (valueList[1]/(valueList[0])*numbersArray[0])
        print("Per calculations, there are", conversion, weightMatch[0], "in", numbersArray[0], weightMatch[1])
    
    if bool(volumeMatch) == True:
        for x in volumeMatch:
            if x in dictVolume.keys():
                valueList.append(dictVolume.get(x))
        conversion = (valueList[1]/(valueList[0])*numbersArray[0])
        print("Per calculations, there are", conversion, volumeMatch[0], "in", numbersArray[0], volumeMatch[1])