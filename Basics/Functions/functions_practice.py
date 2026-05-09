# ============================================
# 🧪 Advanced Functions — Practice Questions
# ============================================

# ===== *args Practice =====

# Q1 — Count items
def count_items(*args):
    return len(args)

print(count_items(10, 20, 30))       # 3
print(count_items(1, 2, 3, 4, 5))   # 5

# Q2 — Average
def average(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

print(average(10, 20, 30))           # 20.0
print(average(5, 10, 15, 20))        # 12.5

# Q3 — Zomato bill with GST
def zomato_bill(*args):
    total = 0
    for i in args:
        total += i
    gst = 0.18
    return f"Final Bill: {total + total * gst}"

print(zomato_bill(100, 200, 150))    # 530.0

# Q4 — Student result
def student_result(*args):
    total = 0
    for i in args[1:]:
        total += i
    average = total / len(args[1:])
    result = "Pass" if average >= 35 else "Fail"
    return f"{args[0]} - Average: {average} - Result: {result}"

print(student_result("Koushik", 80, 75, 90, 69))
print(student_result("Ravi", 20, 15, 30, 25))

# ===== **kwargs Practice =====

# Q1 — Show order
def show_order(**kwargs):
    print("Order Summary")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_order(item="Dosa", price=80, quantity=2)

# Q2 — Student profile
def student_profile(**kwargs):
    print("Student Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student_profile(name="Koushik", age=23, course="Python")

# Q3 — Zomato order with total
def zomato_order(**kwargs):
    print("Order Summary")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    total = kwargs["quantity"] * kwargs["price"]
    print(f"Total: {total}")

zomato_order(item="Dosa", quantity=2, price=80)

# Q4 — Employee profile with annual salary
def employee_profile(**kwargs):
    print("Employee Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    annual_salary = kwargs["monthly_salary"] * 12
    print(f"Annual Salary : {annual_salary}")

employee_profile(name="Koushik", role="AI Engineer", monthly_salary=50000)
