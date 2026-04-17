# ============================================
# 📥 Input Handling in Python
# ============================================

# Without int() — Python treats input as string
print("===== Without int() =====")
a = input("Enter number one: ")
b = input("Enter number two: ")
print("Result (string concat):", a + b)
# Output: 1020 (not 30!) because input is string by default

# With int() — converts string to integer
print("\n===== With int() =====")
x = int(input("Enter number one: "))
y = int(input("Enter number two: "))
print("Result (actual addition):", x + y)
# Output: 30 (actual math!)

# Key Learning:
# input() always returns STRING
# Wrap with int() to convert to integer
# Wrap with float() for decimal numbers
