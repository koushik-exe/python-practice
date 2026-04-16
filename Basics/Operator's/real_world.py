# ============================================
# 🌍 Real World Practice — Operators
# ============================================

# Q1. Area of Rectangle
print("===== Q1. Area of Rectangle =====")
length = 15
width = 8
area = length * width
print("The area of the rectangle is:", area)
# Output: 120

# Q2. Money Left After Shopping
print("\n===== Q2. Money Left After Shopping =====")
total_rupees = 100
cost_per_item = 27
number_of_items = 3
total_cost = number_of_items * cost_per_item
money_left = total_rupees - total_cost
print("Money left after purchase:", money_left)
# Output: 19

# Q3. Students Divided Into Groups
print("\n===== Q3. Students Into Groups =====")
total_students = 47
group_size = 5
groups_formed = total_students // group_size
students_left = total_students % group_size
print("Complete groups formed:", groups_formed)
print("Students left out:", students_left)
# Output: 9 groups, 2 students left

# Q4. Who Is Older
print("\n===== Q4. Who Is Older =====")
koushik_age = 23
arun_kumar_age = 25
if koushik_age > arun_kumar_age:
    print("Koushik is older than Arun Kumar.")
else:
    print("Arun Kumar is older than Koushik.")
# Output: Arun Kumar is older

# Q5. Shop Minimum Price Check
print("\n===== Q5. Shop Price Check =====")
shop_price = 500
customer_money = 350
if customer_money >= shop_price:
    print(True)
else:
    print(False)
# Output: False

# Q6. Movie Ticket — Age AND Valid ID
print("\n===== Q6. Movie Ticket =====")
my_age = 17
valid_id = True
valid_age = 18
if my_age >= valid_age and valid_id:
    print("You can buy the movie ticket.")
else:
    print("You cannot buy the movie ticket.")
# Output: You cannot buy the movie ticket.

# Q7. Food App Free Delivery
print("\n===== Q7. Food App Delivery =====")
order_value = 500
minimum_order = 300
user = "premium_member"
if order_value >= minimum_order or user == "premium_member":
    print("You are eligible for free delivery.")
else:
    print("You are not eligible for free delivery.")
# Output: You are eligible for free delivery.

# Q8. Student Pass or Fail
print("\n===== Q8. Student Result =====")
tamil_mark = 40
english_mark = 30
maths_mark = 45
pass_mark = 35
if tamil_mark >= pass_mark and english_mark >= pass_mark and maths_mark >= pass_mark:
    print("Promoted")
else:
    print("Failed")
# Output: Failed — English mark is below 35
