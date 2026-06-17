"""
import csv

with open("products.csv", 'r', encoding="utf-8") as file:
    read = csv.DictReader(file)
    for i in read:
        print(i)

if i["category"] == "Electronics":
print(i["name"], i["price"])
"""

with open("products.csv", 'r', encoding="utf-8") as file:
    next(file)
    for i in file:
        parts = i.strip().split(",")
        print(f"Products: {parts[0]} | Price: {parts[1]} | Category: {parts[2]}")
        # split each line by comma
        # print each value