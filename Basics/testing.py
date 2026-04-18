"""
name ="KoushiK"
mobile = "9865789394"

print(name.lower())
print(name.upper())

masked = mobile[:2]
masked1 = mobile[-2:]
masked2 = mobile[:2] +"******" +mobile[-2:]

print(masked)
print(masked1)
print(masked2)

teacher = "ClAuDe One who is tEAChing"
student = "KoUsHiK one WHO is LEArning pyTHon"
formated = f"{teacher.title()} - {student.title()}"
print(formated)

location = "Karur Bus Stand"
pick_up_location = location.replace("Karur Bus Stand","Karur New Bus Stand")
print(pick_up_location)

message ="your Rapido booking id is: Rpo1234. please keep it safe"
booking_id = message.split(":")[0]
booking_id1 = message.split(":")[1]
booking_id2 = message.split(":")[1]. split(".")[0]
booking_id3 = message.split(":")[1]. split(".")[0].strip()
print(booking_id)
print(booking_id1)
print(booking_id2)
print(booking_id3)

promo_msg ="use Zomato100 to get 100 off on your first oder"
if "Zomato100" in promo_msg:
    print("offer_applied")
else:
    print("Offer not Applied")

postion_finder =f"position is: {promo_msg.find("Zomato100")}"
print(postion_finder)

friend = "arun kumar"
initials = ([word[0].upper() for word in friend.split()])
initials_1 ="".join([word[0].upper() for word in friend.split()])
print(initials)
print(initials_1)

word1 ="Koushik is learning python with using Claude and youtube"
word_count = len(word1.split())
print(word_count)


friend = "arun kumar"
words = friend.split()
initials = []

for word in words:
    initials.append(word[0].upper())

print(initials)

students = ["koushik", "arun", "priya", "ravi"]
print(students)
capital_students = [] # this is an Hot Box empty 
for word in students:
    capital_students.append(word.upper())
print(capital_students)
"""
"""
name = "koushik raja"
words = name.split()
hot_box = []
for word in words:
    hot_box.append(word[0].upper())
print("".join(hot_box))
"""

names = ["koushik raja", "arun kumar", "priya devi"]

for name in names:
    words = name.split()
    hot_box = []
    for word in words:
        hot_box.append(word[0].upper())
    print("".join(hot_box))
