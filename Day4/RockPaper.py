import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
Game = [rock, paper, scissors]
computer_choice = random.randint(0, 2);
print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors: ");
Choose = input();
user_choice = int(Choose);

# Print the user's choice
if user_choice > 2 :
    print("pls select an valid number")
    exit()
else :
    print(f"You chose:\n{Game[user_choice]}")

#print Computer choice
print(f"Computer chose:\n{Game[computer_choice]}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")

#this is my way of doing it
# if Choose == 0 :
#     printGame = Game[0]
#     print("You Chosed: ")
#     print(printGame)

#     printComgame = Game[RandomPick]
#     print("the Computer picked: ")
#     print(printComgame)

#     if printGame == printComgame :
#         print("its a draw")
#     elif printComgame == Game[1] :
#         print("You loose")
#     elif printComgame == Game[2] :
#         print("You win")
# elif Choose == 1 :
#     printGame = Game[1]
#     print("You Chosed: ")
#     print(printGame)

#     printComgame = Game[RandomPick]
#     print("the Computer picked: ")
#     print(printComgame)

#     if printGame == printComgame :
#         print("its a draw")
#     elif printComgame == Game[0] :
#         print("You win")
#     elif printComgame == Game[2] :
#         print("You loose")
# elif Choose == 2 :
#     printGame = Game[2]
#     print("You Chosed: ")
#     print(printGame)

#     printComgame = Game[RandomPick]
#     print("the Computer picked: ")
#     print(printComgame)

#     if printGame == printComgame :
#         print("its a draw")
#     elif printComgame == Game[0] :
#         print("You loose")
#     elif printComgame == Game[1] :
#         print("You win")
# else :
#     print("Invalid input! Please enter 0, 1, or 2.");