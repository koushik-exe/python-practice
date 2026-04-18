# ============================================
# 🧪 String Methods — Practice Questions
# ============================================

import sys

# ===== Q1 — Clean City Name =====
print("===== Q1. Clean City Name =====")
city = "  chenNAI   "
print(city.strip().title())
# Output: Chennai

# ===== Q2 — Clean Email =====
print("\n===== Q2. Clean Email =====")
email = "  KOushik.RAJA@Gmail.COM   "
print(email.lower().strip())
# Output: koushik.raja@gmail.com

# ===== Q3 — Extract Booking ID =====
print("\n===== Q3. Extract Booking ID =====")
rapido = "Booking confirmed: RPD5678. Enjoy your ride!"
print(rapido.split(":")[1].split(".")[0].strip())
# Output: RPD5678

# ===== Q4 — Employee ID Check =====
print("\n===== Q4. Employee ID Check =====")
message = "My employee ID is EMP2024 and my department is HR"
if "EMP2024" in message:
    print(True)
else:
    print(False)
print(message.find("EMP2024"))
# Output: True, 18

# ===== Q5 — School Initials Generator (sys.argv) =====
# Usage: python string_practice.py Koushik Raja
print("\n===== Q5. Student Initials Generator =====")
if len(sys.argv) == 3:
    print(f"Word count: {len(sys.argv[1:])}")
    initials = sys.argv[1:]
    hot_box = []
    for word in initials:
        hot_box.append(word[0].upper())
    print("Initials:", "".join(hot_box))
else:
    print("Please provide the correct name!")
    print("Usage: python string_practice.py Koushik Raja")
