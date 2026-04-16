# ============================================
# 🔗 Logical Operators in Python
# ============================================
# and → all conditions must be true
# or  → at least one condition must be true
# not → flips the result

print("===== and Operator =====")
print(True and True)    # True  — both true
print(True and False)   # False — one is false
print(False and False)  # False — both false

print("\n===== or Operator =====")
print(True or False)    # True  — one is true
print(False or False)   # False — both false
print(True or True)     # True  — both true

print("\n===== not Operator =====")
print(not True)         # False — flipped
print(not False)        # True  — flipped

# Real World Example
print("\n===== Real World — Apple Student Discount =====")
age = 20
is_student = True

if age >= 18 and is_student:
    print("You are eligible for Apple student discount.")
else:
    print("You are not eligible.")

print("\n===== Real World — School Admission =====")
child_age = 2.9
can_speak_well = True

if child_age >= 3 or can_speak_well:
    print("Child can get admission.")
else:
    print("Child cannot get admission.")
