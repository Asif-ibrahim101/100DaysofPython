import random
from logo import logo
   
print(logo)
print("Welcome to the guesing Game!")
print("i am thinking about a number btn 1 to 100.")

#Generate random numbers
def Random():
    random_number = random.randint(1, 100)
    return random_number
Random_number = Random()

# Loop until a valid difficulty level is chosen
Total_chances = 0;
while True:
    difficulty_level = input("Choose your difficulty level: Easy or Hard: ").lower()
    if difficulty_level == "easy":
        Total_chances = 10
        print(f"You have {Total_chances} chances in total. Have fun!")
        break
    elif difficulty_level == "hard":
        Total_chances = 5
        print(f"You have {Total_chances} chances in total. Have fun!")
        break
    else:
        print("Please choose 'easy' or 'hard'.")

def Game(Number):
    life = 0
    flag = False
    
    while life < Total_chances:
        life += 1
        print(f"This is your {life}th attempet you have {Total_chances - life} left")
        Guss_number = int(input("Make a guss: "))
        
        if Guss_number == Number:
            print(f"Congo you did it in {life}th try")
            flag = True
            break
        elif Guss_number < Number:
            print("You Gussed a bit low")
            print("Guss again")
            
        elif Guss_number > Number:
            print("you Gussed a bit High")
            print("Guss again")
            
    
    if not flag:
        print("The number is %d" % Number)
        print("Better Luck Next time!")
        
Game(Random_number)