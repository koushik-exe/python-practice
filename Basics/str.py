def add(a, b):
    return(a + b)

result = add(5, 10)
print(result)

def multiply(x,y):
    return x*y

koushik = multiply(8,7)
print(koushik)

def full_name(first, last):
    return (f"{first} {last}")

names = full_name("Koushik", "Raja")
print(names)

def discount_price(price, discount_percent):
    return (f"Final Price: {price - price * discount_percent}")

discount = discount_price(1000,0.10)
print(discount)

def is_eligible(age):
    if age >= 18:
        return("Eligible to Vote")
    else:
        return("Not Elible to Vote")

check_age = is_eligible(17)
print(check_age)