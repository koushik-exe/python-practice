try:
    account_balance = 10000
    correct_pin = 1234
    pin = int(input("Enter your PIN: "))
    if pin != correct_pin:
        raise ValueError("Invalid PIN. Access denied.")
    amount = int(input("Enter amount to withdraw: "))
    if amount <=0:
        raise ValueError("Amount must be greater than zero")
    if amount > account_balance:
        raise ValueError("Insufficient balance")

    remaining = account_balance - amount
except ValueError as error:
    print(f"Transaction failed: {error}")

except Exception as error:
    print(f"Unexpected error: {error}")

else:
    print("---- Transaction Successful ----")
    print(f"Amount withdrawn: ₹{amount}")
    print(f"Remaining balance: ₹{remaining}")
    print(f"--------------------------------")

finally:
    print("Session closed. Goodbye!")
