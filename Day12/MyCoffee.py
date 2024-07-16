from CofeeData import MENU
from CofeeData import Resources

# Report function
def Report(resources):
    print(f"Water: {resources['Water']} ml")
    print(f"Milk: {resources['Milk']} ml")
    print(f"Coffee: {resources['Coffee']} gm")
    print(f"Money: {resources['Money']} $")

# Choice function
def Choose_item(item):
    Money_required = MENU[item]["cost"]
    ingredients_required = MENU[item]["ingredients"]
    
    # Check if resources are sufficient
    for ingredient in ingredients_required:
        if Resources[ingredient.capitalize()] < ingredients_required[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return
    
    print("Please insert money")
    quarter = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))
    
    quarter_converted = quarter * 0.25
    dimes_converted = dimes * 0.10
    nickels_converted = nickels * 0.05
    pennies_converted = pennies * 0.01
    
    Total_money_inserted = quarter_converted + dimes_converted + nickels_converted + pennies_converted
    
    if Total_money_inserted < Money_required:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        Change = Total_money_inserted - Money_required
        print(f"Here is ${round(Change, 2)} in change.")
        print(f"Here is your {item}. Enjoy!")
        
        # Deduct resources
        for ingredient in ingredients_required:
            Resources[ingredient.capitalize()] -= ingredients_required[ingredient]
        
        # Add money to Resources
        Resources["Money"] += Money_required

is_running = True
while is_running:
    user_choice = input("What would you like? (latte/cappuccino/espresso): ").lower()
    
    if user_choice == "off":
        is_running = False
    elif user_choice == "report":
        Report(Resources)
    elif user_choice in MENU:
        Choose_item(user_choice)
    else:
        print("Invalid choice. Please choose latte, cappuccino, or espresso.")