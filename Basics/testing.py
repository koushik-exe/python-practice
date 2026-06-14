with open("students.txt", 'w') as file:
    file.write("Name: Koushik\n")
    file.write("Age: 23\n")
    file.write("City: Karur\n")
    file.write("Course: Python\n")
    file.write("Goal: Data Engineer\n")

"""
with open("students.txt", 'r') as file:
    print(file.read())
"""
with open("students.txt", 'a') as file:
    file.write("Hobby: Coding\n")
    file.write("Status: Learning\n")
"""
with open("students.txt", 'r') as file:
    print(file.read())

with open("students.txt", 'r') as file:
    content = file.readlines()
    print(content[3])
    print(content[4])

with open("students.txt", 'r') as file:
    file.readline()   # line 1 — read but don't print
    file.readline()   # line 2 — read but don't print
    print(file.readline())  # line 3 — print this
    print(file.readline())  # line 4 — print this

with open("students.txt", 'r') as file:
    for i in file:
        if "Karur" in i or "Python" in i:
            print(i)

with open("students.txt", 'r') as file:
    lines = file.readlines()
    for index, value in enumerate(lines, 1):
        print(f"{index} : {value}")
"""
with open("students.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:        # if line is empty — file ended
            break
        print(line.strip()) # strip() removes extra blank lines