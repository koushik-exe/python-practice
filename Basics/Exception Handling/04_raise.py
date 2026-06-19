try:
    age = int(input("Enter Your Age: "))
    distance = int(input("Enter Distance in KM: "))
    if age < 18:
        raise ValueError("You must be 18 or older to book a ride")
    if distance <= 0:
        raise ValueError("Distance cannot be zero or negative")
    if distance > 100:
        raise ValueError("We don't serve distances above 100km")
    fare = distance *12
except ValueError as error:
    print(f"Booking failed: {error}")
except Exception as error:
    print(f"Unexpected error: {error}")

else:
    print("---- Rapido Booking Confirmed ----")
    print(f"Distance: {distance} km")
    print(f"Fare: ₹{fare}")
    print("----------------------------------")

finally:
    print("Thank you for choosing Rapido!")