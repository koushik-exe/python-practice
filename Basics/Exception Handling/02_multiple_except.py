try:
    price = int(input("Enter product price: "))
    quantity = int(input("Enter Quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity cannot be zero")
    if price <= 0:
        raise ValueError("Price cannot be negative")
    total = price * quantity
    print(f"Total Bill: ₹{total}")
except ValueError as error:
    print(f"Invalid input: {error}")
except Exception as error:
    print(f"Unexpected error: {error}")
