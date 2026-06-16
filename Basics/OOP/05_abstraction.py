from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

class RazorPay(PaymentGateway):
    def process_payment(self):
        return f"RazorPay\n₹{self.amount} processed via RazorPay"

class Stripe(PaymentGateway):
    def process_payment(self):
        return f"Stripe\n₹{self.amount} processed via Stripe"

RP1 = RazorPay(5000)
print(RP1.process_payment())
S1 = Stripe(3000)
print(S1.process_payment())