class BankAccount:
    def __init__(self, account_holder, account_number, balance, pin):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance
        self.__pin = pin
    
    def __validate_pin(self):
        entered_pin = int(input("Enter your Pin: "))
        return self.__pin == entered_pin
    
    def _get_bank_view(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: ₹{self.__balance}"
    
    def get_customer_view(self):
        if self.__validate_pin():
            return f"Account Holder: {self.account_holder}\nBalance: ₹{self.__balance}"
        else:
            return "Invalid PIN"

    def deposit(self, amount):
        if self.__validate_pin():
            self.__balance += amount
            return (
                f"₹{amount} Deposited Successfully!\n"
                f"Current Balance {self.__balance}"
            )
        else:
            return f"Invalid PIN — transaction failed!"
    
    def withdraw(self,amount):
        if self.__validate_pin():
            if amount <= self.__balance:
                self.__balance -= amount
                return (
            f"₹{amount} Withdrawn Successfully!\n"
            f"Current Balance: ₹{self.__balance}"
            )
            else:
                return "Insufficient Balance"
        else:
            return "Invalid PIN — transaction failed!"

class BankStaff:
    def show_account(self,account):
        return account._get_bank_view()

class CustomerApp:
    def show_account(self, account):
        return account.get_customer_view()

acc = BankAccount("Koushik", "SB001", 50000, 1234)

staff = BankStaff()
customer = CustomerApp()

print("Bank Staff View:")
print(staff.show_account(acc))

print("\nCustomer View:")
print(customer.show_account(acc))

print("\nDeposit:")
print(acc.deposit(5000))

print("\nWithdraw:")
print(acc.withdraw(200000))