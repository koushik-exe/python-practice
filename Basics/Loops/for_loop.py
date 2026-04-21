# ============================================
# 🔁 For Loop in Python
# ============================================
# Use for loop when you know how many times to repeat
# It goes through each item in a list one by one

# ===== Basic for loop =====
print("===== Basic For Loop =====")
fruits = ["apple", "mango", "banana"]
for i in fruits:
    print(i)

# ===== for loop with counter =====
print("\n===== For Loop with Counter =====")
count = 1
for i in fruits:
    print(count, i)
    count += 1

# ===== for loop with upper() =====
print("\n===== For Loop with String Method =====")
students = ["koushik", "arun", "priya", "ravi", "ishwarya"]
for i in students:
    print(i.upper())

# ===== for loop with if — skip negatives =====
print("\n===== Skip Negatives =====")
numbers = [10, -5, 8, -3, 6, -9, 4, 2, -1]
for num in numbers:
    if num < 0:
        continue   # skip negative numbers
    print(num)

# ===== for loop with if — even numbers =====
print("\n===== Even Numbers Only =====")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 1:
        continue   # skip odd numbers
    print(num)

# ===== for loop — sum of numbers =====
print("\n===== Sum of Numbers =====")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print("Total:", total)

# ===== for loop — names longer than 4 letters =====
print("\n===== Names Longer Than 4 Letters =====")
names = ["Koushik", "Arun", "Priya", "Ravi", "Ishwarya"]
for name in names:
    if len(name) > 4:
        print(name)

# ===== for loop — find highest price =====
print("\n===== Highest Price =====")
prices = [120, 450, 900, 670, 230, 55, 890]
highest = 0
for price in prices:
    if price >= highest:
        highest = price
print("Highest price:", highest)
