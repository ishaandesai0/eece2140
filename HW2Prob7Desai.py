from operator import itemgetter 

invoice = (('83', 'Electric Sander', 7, 57.98),('24', 'Power Saw', 18, 89.82),
('7', 'Sledge Hammer', 11, 24.09),('77', 'Hammer', 76, 11.99 ))

print("Invoice by Item")
print(sorted(invoice, key = itemgetter(1))) 

print("\nInvoice by Price")
print(sorted(invoice, key = itemgetter(3))) 

print('\nInvoice with Part and Quantity')
part1 = () 
for i in invoice: 
    partQuantity = ((i[1], i[2])) 
    part1 += (partQuantity, ) 
print(sorted(part1, key = itemgetter(1))) 

print('\nInvoice with Part and Total Cost per Part')
part2 = () 
for i in invoice: 
    partCost = (i[1], i[2]*i[3]) 
    part2 += (partCost,) 
print(sorted(part2, key = itemgetter(1))) 


for i in part2:
    if i[1] >= 200 and i[1] <= 500:
        print(i)

totalCost = 0 
for i in part2:
    totalCost += i[1] 
print("\nTotal Cost =", " %.2f"%totalCost) 