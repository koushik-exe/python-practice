# ============================================
# 🔥 Advanced Functions in Python
# ============================================

# ===== return vs print =====
print("===== return vs print =====")

# print inside — shows but can't store
def add_print(a, b):
    print(a + b)

# return inside — store and use anywhere
def add_return(a, b):
    return a + b

result = add_return(5, 10)
print(result)           # use once
print(result * 2)       # use again
print(f"Sum is {result}")  # use anywhere

# ===== *args — any number of values =====
print("\n===== *args =====")

# *args collects all values into a tuple
def show_args(*args):
    print(args)

show_args(10, 20, 30)  # (10, 20, 30)

# sum with *args
def total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(total(10, 20, 30))        # 60
print(total(1, 2, 3, 4, 5))    # 15

# average with *args
def average(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

print(average(10, 20, 30))      # 20.0

# find highest with *args
def find_highest(*args):
    highest = 0
    for i in args:
        if i > highest:
            highest = i
    return highest

print(find_highest(10, 50, 30, 80, 20))  # 80

# ===== **kwargs — any number of key:value pairs =====
print("\n===== **kwargs =====")

# **kwargs collects all key=value into a dictionary
def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(name="Koushik", age=24, city="Chennai")

# loop through kwargs
def show_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_profile(name="Koushik", age=24, city="Chennai")

# kwargs with calculation
def employee_profile(**kwargs):
    print("Employee Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    annual_salary = kwargs["monthly_salary"] * 12
    print(f"Annual Salary : {annual_salary}")

employee_profile(name="Koushik", role="AI Engineer", monthly_salary=50000)
