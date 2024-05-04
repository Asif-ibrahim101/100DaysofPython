##Welcome
# number of people
# percentage 10, 12, 15
# total price

print("Welcome to the python Tip calculator");
total_price = float(input("Give me the total amount: ")) #take this as an float
Tip_percentage = float(input("How much tip you want to give: 10, 12, 15"))
people = float(input("how many peoples you have: "))

percentage_amount = Tip_percentage / 100;
amount_after_per = total_price * percentage_amount;
total_amount_with_per = total_price + amount_after_per;

total_tip = total_amount_with_per / people;
print(total_tip)
print(total_tip * percentage_amount);

