# ============================================
# 🔤 String Methods in Python
# ============================================

name = "KoushiK"
mobile = "9865789394"

# ===== Case Methods =====
print("===== Case Methods =====")
print(name.lower())       # koushik — all lowercase
print(name.upper())       # KOUSHIK — all uppercase
print(name.title())       # Koushik — first letter capital

# ===== strip() — Remove spaces =====
print("\n===== strip() =====")
city = "  chenNAI   "
print(city.strip())           # removes spaces both sides
print(city.strip().title())   # clean + proper case = Chennai

# ===== Slicing — Masking =====
print("\n===== Slicing — Phone Masking =====")
print(mobile[:2])                        # 98 — first 2 digits
print(mobile[-2:])                       # 94 — last 2 digits
print(mobile[:2] + "******" + mobile[-2:])  # 98******94

# ===== replace() =====
print("\n===== replace() =====")
location = "Karur Bus Stand"
new_location = location.replace("Karur Bus Stand", "Karur New Bus Stand")
print(new_location)

# ===== split() + chaining =====
print("\n===== split() + chaining =====")
message = "your Rapido booking id is: Rpo1234. please keep it safe"
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)   # Rpo1234

# Step by step breakdown:
# message.split(":")         → ['your Rapido booking id is', ' Rpo1234. please keep it safe']
# .split(":")[1]             → ' Rpo1234. please keep it safe'
# .split(":")[1].split(".")  → [' Rpo1234', ' please keep it safe']
# [0]                        → ' Rpo1234'
# .strip()                   → 'Rpo1234'

# ===== in — Membership Check =====
print("\n===== in keyword =====")
promo_msg = "use Zomato100 to get 100 off on your first order"
if "Zomato100" in promo_msg:
    print("Offer Applied")
else:
    print("Offer not Applied")

# ===== find() — Find Position =====
print("\n===== find() =====")
print(promo_msg.find("Zomato100"))  # returns position number

# Difference:
# in     → returns True or False (exists or not)
# find() → returns position number (where it starts)

# ===== Word Count =====
print("\n===== Word Count =====")
sentence = "Koushik is learning python with Claude and youtube"
word_count = len(sentence.split())
print("Word count:", word_count)
