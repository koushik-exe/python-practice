class ZomatoCart:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
    
    def __str__(self):
        return f"Customer: {self.customer}\nItems: {self.items}"

    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return f"ZomatoCart(Customer = '{self.customer}', Items = {self.items})"

C1 = ZomatoCart("Koushik", ["Biryani", "Dosa", "Pizza"])
print(C1)         
print(len(C1))    
print(repr(C1))   
        