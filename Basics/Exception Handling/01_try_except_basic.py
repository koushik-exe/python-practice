try:
    price = int(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))
    total = price * quantity
    print(f"Total Bill: {total}")
except Exception:
    print("Invalid input! Please enter numbers only.")