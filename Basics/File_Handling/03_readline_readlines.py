with open("orders.txt", 'r', encoding="utf-8") as file:
    print(file.readline())

with open("orders.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for index, i in enumerate(lines,1):
        print(f"Line {index}: {i}")