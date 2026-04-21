# ============================================
# 🔄 While Loop in Python
# ============================================
# Use while loop when you don't know how many times to repeat
# Keep going UNTIL a condition becomes False

# ===== Basic while loop — countdown =====
print("===== Countdown =====")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1   # without this → infinite loop!
print("Time's Up!")

# ===== while loop — keep asking until correct =====
print("\n===== Enter Number Above 10 =====")
# i = int(input("Enter a number above 10: "))
# while i <= 10:
#     print("Please enter a number above 10")
#     i = int(input("Enter a number above 10: "))
# print("Good job!")

# ===== while True + break — PIN system =====
print("\n===== PIN System =====")
correct_pin = "1234"
# entered_pin = ""
# while entered_pin != correct_pin:
#     entered_pin = input("Enter your PIN: ")
# print("Access Granted!")

# ===== while True + break — Login system =====
print("\n===== Login System =====")
correct_password = "python123"
# enter_password = ""
# while correct_password != enter_password:
#     enter_password = input("Enter your password: ")
#     if correct_password != enter_password:
#         print("Wrong password! Try again")
# print("Login Successful!")

# ===== while True + break — Shopping Cart =====
print("\n===== Shopping Cart =====")
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
