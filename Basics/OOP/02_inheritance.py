class Vehicle:
    def __init__(self,brand, speed):
        self.brand = brand
        self.speed = speed
    
    def show_details(self):
        return f"Brand: {self.brand} | Speed: {self.speed}kmph"

class Car(Vehicle):
    def __init__(self,brand, speed, fuel_type):
        super().__init__(brand,speed)
        self.fuel_type =fuel_type
    
    def car_info(self):
        return f"{self.brand} runs on {self.fuel_type}"

C1 = Car("Toyota", 120, "Petrol")
print(C1.show_details())
print(C1.car_info())