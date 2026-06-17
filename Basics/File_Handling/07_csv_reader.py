import csv

with open("products.csv", 'r', encoding="utf-8") as file:
    next(file)
    read = csv.reader(file)
    for i in read:
        print(i)

with open("products.csv", 'r', encoding="utf-8") as file:
    read = csv.DictReader(file)
    for i in read:
        print(f"Product: {i["name"]} | Price: {i["price"]} | Category: {i["category"]}")