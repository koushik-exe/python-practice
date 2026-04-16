# Q1. Write a program that calculates the area of a rectangle. Length = 15, Width = 8
length = 15
width = 8
area = length * width
print("The area of the rectangle is:", area)

# Q2. You have 100 rupees. You bought 3 items for 27 rupees each. How much money is left? Use arithmetic operators only.
total_rupees = 100
cost_per_item = 27
number_of_items = 3
total_cost = number_of_items * cost_per_item
money_left = total_rupees - total_cost
print("Money left after purchase:", money_left)

# Q3. A class has 47 students. They need to be divided into equal groups of 5. How many complete groups are formed? How many students are left out?
total_students = 47
groups = 5
Groups_formed = total_students // groups
groups_left = total_students % groups
print("Complete groups formed:", Groups_formed)
print("Students left out:", groups_left)

# Q4. Create two variables — your age and your friend's age. Check and print who is older using comparison operators.
koushik_age = 23
Arun_kumar_age = 25
if koushik_age > Arun_kumar_age:
    print("Koushik is older than Arun Kumar.")
else:
    print("Arun Kumar is older than Koushik.")

#Q5. A shop sells products above 500 rupees only. Customer brings 350 rupees. Check if customer can buy or not. Print True or False only.
shop_price = 500
customer_money = 350
if customer_money >= shop_price:
    print(True)
else:
    print(False)

# Q6. Movie ticket needs age above 18 AND valid ID. Write the condition only — no need for full code — just the if line.
my_age = 17
valid_id = True
Valid_age = 18
if my_age >= Valid_age and valid_id:
    print("You can buy the movie ticket.")
else:
    print("You cannot buy the movie ticket.")

#Q7. A food app gives free delivery if order is above 300 OR user is a premium member. Write full code with variables and print result.
my_order_value = 500
discount_above_value = 300
user = "premium_member"
if my_order_value >= discount_above_value or user == "premium_member":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")

# Q8. A student has 3 subject marks — Tamil, English, Maths. Pass mark is 35 each. If all three passed print "Promoted" otherwise print "Failed" — use your own example from earlier! 😄
Tamil_mark = 40
English_mark = 30
Maths_mark = 45
pass_mark = 35
if Tamil_mark >= pass_mark and English_mark >= pass_mark and Maths_mark >= pass_mark:
    print("Promoted")
else:    
    print("Failed")
