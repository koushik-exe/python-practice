 # L - Local Scope
# A variable created inside a function is local.
# It lives inside that function only.
# You cannot use it outside.

def my_function():
    message = "I am a local variable"
    print(message)

my_function()

# print(message)  - This will give NameError
# Because message is local to my_function