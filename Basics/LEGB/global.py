# G - Global Scope
# A variable created outside all functions is global.
# It works both inside and outside functions.

name = "Koushik"

def my_function():
    print(name)

my_function()
print(name)