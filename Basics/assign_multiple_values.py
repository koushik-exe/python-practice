# -----------------------------------
# 🧠 Topic: Assign Multiple Values
# -----------------------------------

# ✅ Example 1: Assign multiple values in one line
x, y, z = "apple", "banana", "mango"

print("x:", x)
print("y:", y)
print("z:", z)


# ✅ Example 2: Assign one value to multiple variables
a = b = c = "Python"

print("a:", a)
print("b:", b)
print("c:", c)


# ✅ Example 3: Unpacking values from a list
fruits = ["apple", "banana", "mango"]

x, y, z = fruits  # Unpacking list into variables

print("Fruit x:", x)
print("Fruit y:", y)
print("Fruit z:", z)


# -----------------------------------
# 🎯 Key Learning
# -----------------------------------
# 1. Multiple assignment → assign many values in one line
# 2. One value → assign same value to multiple variables
# 3. Unpacking → extract values from list/tuple into variables
# 4. Number of variables must match number of values