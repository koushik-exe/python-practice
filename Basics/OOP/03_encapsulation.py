class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
    
    def deposit(self,deposit):
        self.__balance += deposit
        return f"₹{deposit} Deposited. New Balance: ₹{self.__balance}"

    def withdraw(self,withdraw):
        if withdraw > self.__balance:
            return f"Insufficient Balance"
        self.__balance-= withdraw
        return f"₹{withdraw} Withdrawn. New Balance: ₹{self.__balance}"
    
    def get_balance (self):
        return f"Account Holder: {self.account_holder} | Balance: ₹{self.__balance}"

person1 = BankAccount("Koushik", 7000)
person2 = BankAccount("Claude", 10000)

print(person1.deposit(4000))
print(person1.get_balance())

print(person2.withdraw(3000))
print(person2.get_balance())

print(person2.withdraw(8000))
