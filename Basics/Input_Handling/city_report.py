# ============================================
# 🌍 Real World — City Sales Report
# ============================================
# Usage: python city_report.py Chennai 500000
# This script is a Data Engineering tool!
# Pass city and sales amount directly from terminal

import sys

# ===== Practice Q1 — Hello Message =====
# Usage: python city_report.py Koushik
# if len(sys.argv) == 2:
#     name = sys.argv[1]
#     print(f"Hello {name}! Welcome to Data Engineering")
# else:
#     print("Please provide your name!")

# ===== Practice Q2 — Add Two Numbers =====
# Usage: python city_report.py 10 20
# if len(sys.argv) == 3:
#     num1 = int(sys.argv[1])
#     num2 = int(sys.argv[2])
#     print(num1 + num2)
# else:
#     print("Please enter two valid numbers!")

# ===== Practice Q3 — Sales Report =====
# Usage: python city_report.py Chennai 500000
if len(sys.argv) == 3:
    city = sys.argv[1]
    sales = int(sys.argv[2])
    tax = sales * 0.18
    total = sales + tax
    print("--- Sales Report ---")
    print(f"City: {city}")
    print(f"Sales Amount: {sales}")
    print(f"Tax (18%): {tax}")
    print(f"Total: {total}")
else:
    print("Please provide correct values!")
    print("Usage: python city_report.py Chennai 500000")
