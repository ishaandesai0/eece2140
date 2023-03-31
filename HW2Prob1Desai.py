def farenheitToC(cTemp):
    fTemp = (9/5)* cTemp + 32
    return fTemp

print('Celcius Temp','\t','Fahrenheit Temp')
for i in range (-10, 101):
    print(" ", (i) , '\t', '\t', " %.3f"%farenheitToC(i))