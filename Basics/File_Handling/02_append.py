with open("orders.txt", 'a', encoding="utf-8") as file:
    file.write("Ravi - Idli - ₹60\n")
    file.write("Deepa - Noodles - ₹150\n")

with open("orders.txt", 'r', encoding="utf-8") as file:
    print(file.read())