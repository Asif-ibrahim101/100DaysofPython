import os
from logo import logo

#Addition
def Add(num1, num2):
    Addition = num1 + num2
    return Addition

#substraction
def Substraction(num1, num2):
    Subs = num1 - num2
    return Subs

#Multiplication
def Multiplication(num1, num2):
    Mult = num1 * num2
    return Mult

#Division
def Division(num1, num2):
    divide = num1 / num2
    return divide

Operations = {
    "+":  Add,
    "-": Substraction,
    "*": Multiplication,
    "/": Division
}
      
def Calculator():
    print(logo)
        
    # num1 = int(input("Give your first number: "))
    num1 = float(input("+"))
    for symbol in Operations: 
            print(symbol)
    isTaken = True

    while isTaken:
        operation_symbols = input("Select one of those symbols: ")
        num2 = int(input("Give your next number: "))
        result = Operations[operation_symbols]
        answer = result(num1, num2)

        print(f"{num1} {operation_symbols} {num2} = {answer}")
        # os.system('cls')
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            isTaken = False
            os.system("clear")
            Calculator()

Calculator()
            