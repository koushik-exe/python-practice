class Payment:
    def __init__(self,amount):
        self.amount = amount
    
    def pay(self):
        return f"Processing Payment..."

class CreditCard(Payment):
    def pay(self):
        return f"₹{self.amount} paid via Credit Card"

class UPI(Payment):
    def pay(self):
        return f"₹{self.amount} paid via UPI"

P1 = Payment(400)
C1 = CreditCard(5000)
U1 = UPI(4500)
print(P1.pay())
print(C1.pay())
print(U1.pay())
