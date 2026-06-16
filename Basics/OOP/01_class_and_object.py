class ZomatoOrder:
    def __init__ (self, customer_name, item, price):
        self.customer_name = customer_name
        self.item = item
        self.price = price
    
    def order_summary(self):
        return f"Customer: {self.customer_name} | Item: {self.item} | Price: ₹{self.price}"

ZO1 = ZomatoOrder("Koushik", "Biryani",250)
print(ZO1.order_summary(),"\n")

ZO2 = ZomatoOrder("Claude", "Anthropic", 100000)
print(ZO2.order_summary())

