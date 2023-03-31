fuelUsed = float(input("Enter the gallons used (-1 to stop): "))
total = 0
count = 0

while(fuelUsed != -1):
    milesDriven = float(input("Enter the miles driven: "))
    milesPerGallon = milesDriven/fuelUsed
    print("The miles/gallon for this tank was: ", milesPerGallon)
    total += milesPerGallon
    count += 1
    fuelUsed = float(input("Enter the gallons used (-1 to stop): "))

print("The overall average miles/gallon was: ", (total/count))

var1 = [k**2 for k in range(5)]
var2 = tuple([-k for k in range (4)])

var1 += var2
var2 += var1
var2[-1] = -50
var1[5] = -var2[0]
var2.pop()
