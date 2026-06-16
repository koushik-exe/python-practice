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

R1.book_ride()                    # ✅ instance - on object
RapidoRide.calculate_fare(10)     # ✅ static - on class
RapidoRide.company_info()         # ✅ class - on class