class RapidoRide:
    company = "Rapido"

    def __init__(self,rider_name, distance):
        self.rider_name = rider_name
        self.distance = distance
    
    def book_ride(self):
        return f"{self.rider_name} booked a ride for {self.distance}KM"

    @staticmethod
    def calculate_fare(distance):
        return f"Fare for {distance}km: {distance * 12}"
    
    @classmethod
    def company_info(cls):
        return f"Company: {cls.company}"

R1 = RapidoRide("Koushik", 10)
print(R1.book_ride())
print(R1.calculate_fare(10))
print(R1.company_info())