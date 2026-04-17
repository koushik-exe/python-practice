# ============================================
# ⚙️ sys.argv — Terminal Arguments in Python
# ============================================

# Why sys.argv?
# input() stops the program and waits for you to type
# sys.argv lets you pass information directly while running
# Example: python argv_basic.py Chennai
# Perfect for Data Engineering automation!

import sys

# sys.argv is a LIST — catches everything typed in terminal
# sys.argv[0] → always the filename (automatic)
# sys.argv[1] → first thing you type after filename
# sys.argv[2] → second thing you type after filename

print("===== What sys.argv contains =====")
print(sys.argv)

# Run this as: python argv_basic.py Koushik Chennai
# Output: ['argv_basic.py', 'Koushik', 'Chennai']
