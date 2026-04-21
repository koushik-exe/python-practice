import sys

childern_ticket = 100
adult_ticket = 200
senior_citizen = 50
age = int(sys.argv[1])
weekend = sys.argv[2].lower()

if age <5:
    print("Not Allowded")

elif age <=12:
    if weekend in ["sat", "sun"]:
        print(f"Weekend rush so  extra 50rs/- : {childern_ticket + 50}")
    else:
        print("Childern ticket is 100")

elif age <= 59:
    if weekend in ["sat", "sun"]:
        print(f"Weekend rush so  extra 50rs/- : {adult_ticket + 50}")
    else:
        print("Adult ticket is 200")

elif age >= 60:
    if weekend in ["sat", "sun"]:
        print(f"Weekend rush so  extra 50rs/- : {senior_citizen + 50}")
    else:
        print("Senior ticket is 50")
