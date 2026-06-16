with open("orders.txt", 'w', encoding="utf-8") as file:
    file.write("Koushik - Biryani - ₹250\n")
    file.write("Pravetha - Dosa - ₹80\n")
    file.write("Claude - Pizza - ₹500\n")

with open("orders.txt", 'r', encoding="utf-8") as file:
    print(file.read())