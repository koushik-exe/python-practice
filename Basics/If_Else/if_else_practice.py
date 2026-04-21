# ============================================
# 🧪 If/Else Practice Questions
# ============================================

import sys

# ===== Q1 — Cinema Ticket with Children Discount =====
# Usage: python if_else_practice.py 10
# print("===== Q1. Cinema Ticket =====")
# ticket_cost = 200
# age = int(sys.argv[1])
# if age <= 12:
#     print("Actual Ticket Price is 200")
#     print(f"Children 50% Discount — Final Price: {ticket_cost - ticket_cost * 0.50}")
# else:
#     print("Above 12 years — Ticket price is 200")


# ===== Q2 — Streaming App Plans =====
# Usage: python if_else_practice.py 500
# print("===== Q2. Streaming Plans =====")
# user_amount = int(sys.argv[1])
# if user_amount >= 999:
#     print("Suggested plan: Premium Plan")
# elif user_amount >= 499:
#     print("Suggested plan: Standard Plan")
# elif user_amount >= 199:
#     print("Suggested plan: Basic Plan")
# else:
#     print("There is no Plan for User")


# ===== Q3 — Bank Loan Approval =====
# Usage: python if_else_practice.py 25 30000
# print("===== Q3. Loan Approval =====")
# age = int(sys.argv[1])
# salary = int(sys.argv[2])
# if age >= 21:
#     if salary >= 25000:
#         print("Loan Approved")
#     else:
#         print("Salary too low")
# else:
#     print("Age Requirement not met")


# ===== Q4 — Movie Ticket Booking System =====
# Usage: python if_else_practice.py 8 sat
print("===== Q4. Movie Ticket Booking =====")
children_ticket = 100
adult_ticket = 200
senior_ticket = 50

age = int(sys.argv[1])
day = sys.argv[2].lower()

if age < 5:
    print("Not Allowed")
elif age <= 12:
    if day in ["sat", "sun"]:
        print(f"Weekend rush — Extra 50rs — Children Ticket: {children_ticket + 50}")
    else:
        print(f"Children Ticket: {children_ticket}")
elif age <= 59:
    if day in ["sat", "sun"]:
        print(f"Weekend rush — Extra 50rs — Adult Ticket: {adult_ticket + 50}")
    else:
        print(f"Adult Ticket: {adult_ticket}")
elif age >= 60:
    if day in ["sat", "sun"]:
        print(f"Weekend rush — Extra 50rs — Senior Ticket: {senior_ticket + 50}")
    else:
        print(f"Senior Ticket: {senior_ticket}")
