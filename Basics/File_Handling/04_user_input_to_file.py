students = []

for i in range(3):
    name = input("Enter Student Name: ")
    students.append(name)

with open("students.txt", 'w', encoding="utf-8") as file:
    for i in students:
        file.write(i + "\n")

with open("students.txt",'r', encoding="utf-8") as file:
    print (file.read())