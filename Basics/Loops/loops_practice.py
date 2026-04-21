# ============================================
# 🧪 Loops Practice Questions
# ============================================

# ===== Q1 — Print fruits with for loop =====
print("===== Q1. Print Fruits =====")
fruits = ["apple", "mango", "banana"]
for i in fruits:
    print(i)
# Output: apple mango banana (one per line)

# ===== Q2 — Print fruits with number =====
print("\n===== Q2. Numbered Fruits =====")
count = 1
for i in fruits:
    print(count, i)
    count += 1
# Output: 1 apple / 2 mango / 3 banana

# ===== Q3 — Print only even numbers =====
print("\n===== Q3. Even Numbers =====")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 1:
        continue
    print(num)
# Output: 2 4 6 8 10

# ===== Q4 — Sum of all numbers =====
print("\n===== Q4. Sum of Numbers =====")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print("Total:", total)
# Output: 55

# ===== Q5 — Login system with while =====
print("\n===== Q5. Login System =====")
correct_password = "python123"
enter_password = ""
while correct_password != enter_password:
    enter_password = input("Enter your password: ")
    if correct_password != enter_password:
        print("Wrong password! Try again")
print("Login Successful!")

# ===== Q6 — Shopping cart with while + for =====
print("\n===== Q6. Shopping Cart =====")
items = []
while True:
    item = input("Add item (type 'done' to finish): ")
    if item.lower() == "done":
        break
    items.append(item)
count = 1
for i in items:
    print(count, i)
    count += 1

# ===== Q7 — Find highest price =====
print("\n===== Q7. Highest Price =====")
prices = [120, 450, 900, 670, 230, 55, 890]
highest = 0
for price in prices:
    if price >= highest:
        highest = price
print("Highest price:", highest)
# Output: 900

# ===== Q8 — Employee salaries =====
print("\n===== Q8. Employee Salaries =====")
salaries = [25000, 45000, 18000, 62000, 33000, 15000, 78000]
total_salary = 0
below_20k = 0
for salary in salaries:
    total_salary += salary
    if salary < 20000:
        below_20k += 1
print("Total salary:", total_salary)
print("Employees below 20000:", below_20k)
# Output: 276000 / 2 employees
