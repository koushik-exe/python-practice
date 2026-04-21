# ============================================
# 🔀 If/Else Basics in Python
# ============================================

# ===== Simple if/else =====
print("===== Voting Age =====")
age = 15
if age >= 18:
    print("You Can Vote")
else:
    print("You Can't Vote")

# ===== elif — Multiple Conditions =====
print("\n===== Grade System =====")
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

# ===== Nested if =====
print("\n===== Driving License — Nested if =====")
license_age = 17
has_license = "Yes"

if license_age >= 18:
    if has_license == "Yes":
        print("You Can Drive")
    else:
        print("You Need to Take Licence and Enjoy the Driving")
else:
    print("You are under 18, You Can't Drive and Apply Licence")

# ===== Logical Operators with if =====
print("\n===== Driving License — Logical Operator =====")
if license_age >= 18 and has_license == "Yes":
    print("You Can Drive")
else:
    print("You Can't Drive")

# ===== Combined — and + or + in =====
print("\n===== Discount System =====")
order_amount = 100
days = "sat"
membership = "no"

if (order_amount >= 1000 and days in ["sat", "sun"]) or membership == "yes":
    print("Eligible for 20% Discount")
else:
    print("Not Eligible for Coupon")
