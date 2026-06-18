
name = input("Enter the Name :")
found = False
with open("students.txt", 'r', encoding="utf-8") as file:
    for i in file:
        if i.strip() == name:
            found = True
            break

if found:
    print(f"{name} found in the file!")
else:
    print(f"{name} not found in the file!")


products = ["Mobile", "TV", "Washing Machine", "Fridge"]

product = input("Enter The Product Name: ")

found = False

for i in products:
    if i == product:
        found = True
        break

if found:
    print(f"{product}  is Found")
else:
    print(f"{product} is Not Found")