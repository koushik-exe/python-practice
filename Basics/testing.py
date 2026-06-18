"""
class BankAccount:
    def __init__ (self,account_holder, account_number,balance,pin):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance
        self.__pin = pin
    
    def __validate_pin(self, entered_pin):
        return self.__pin == entered_pin

    def _get_bank_view(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.__balance}\n"
            
    
    def get_customer_view(self):
        return f"Account Holder: {self.account_holder}\nBalance: {self.__balance}\n"
    
class BankStaff:
    def show_account(self, account):
        return account._get_bank_view()

class CustomerApp:
    def show_account(self, account):
        return account.get_customer_view()

acc = BankAccount("Koushik", "SB001", 50000, 1234)

staff = BankStaff()
customer = CustomerApp()

print("Bank Staff View:")
print(staff.show_account(acc))

print("Customer View:")
print(customer.show_account(acc))

"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

S1 = Student("Koushik", 85)
print(S1)

