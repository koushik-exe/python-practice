# today learning form the youtube is Loops in python 
'''
names = ["Koushik", "Arun Kumar", "Viswesh", "kirthika", "IshWarya"]

for test in names:
    print(test.upper())
'''
'''
correct_pin = '1234'
entered_pin=''

while entered_pin != correct_pin:
    entered_pin = input("Enter your Correct Pin: ")

print("Access Granted")
'''
'''
number = [1,3,4,7,6,9,8,2,5,10,11,12,13,44]

for i in number:
    if i == 5:
        break
    print(i)
'''
"""
numbers = [10,-5,-8,5,-9,6,4,-3]

for num in numbers:
    if num <0:
        continue
    print(num)

for num in numbers:
    pass # future logic implementation
"""
"""
count = 5

while count >0:
    print(f"countdown: {count}")
    count -= 1

print("Time's Up!")
"""
# above countdown function is not understanding for me claude in youtube lerning 

items = []

while True:
    item = input("Add item(type 'done' to finish): ")
    if item.lower() == "done":
        break
    items.append(item)

print("Items in cart:", items)
