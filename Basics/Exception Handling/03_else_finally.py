try:
    price = int(input("Enter product price: "))
    quantity = int(input("Enter Quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity cannot be zero")
    if price <= 0:
        raise ValueError("Price cannot be negative")
    total = price * quantity
except ValueError as error:
    print(f"Billing failed: {error}")
except Exception as error:
    print(f"Unexpected error: {error}")

else:
    print("----DMart Bill----")
    print(f"Price per Item: ₹{price}")
    print(f"Quantity: {quantity}")
    print(f"Total: ₹{total}")
    print("-----------------------")

finally:
    print("Thank you for shopping at DMart!")