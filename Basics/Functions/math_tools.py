# ============================================
# 🔧 math_tools.py — Reusable Math Functions
# ============================================
# This file contains reusable functions
# Import from other files using:
# from math_tools import add, multiply

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
