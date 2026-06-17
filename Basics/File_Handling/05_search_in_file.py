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