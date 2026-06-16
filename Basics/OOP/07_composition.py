class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def restaurant_info(self):
        return f"Restaurant: {self.name} | Cuisine: {self.cuisine}"
    
class ZomatoOrder:
    def __init__(self, customer_name, restaurant):
        self.customer_name = customer_name
        self.restaurant = restaurant
    def order_details(self):
        return f"Customer: {self.customer_name} | Restaurant: {self.restaurant.name} | Cusine: {self.restaurant.cuisine}"
        
R1 = Restaurant("Murugan Idli", "South Indian")
print(R1.restaurant_info())

Z1 = ZomatoOrder("Koushik", R1)
print(Z1.order_details())