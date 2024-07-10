import math

def pain_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    value = math.ceil(number_of_cans)
    print(value)
    
GivenHeight = int(input("Give me a Height : "))
GivenWdith = int(input("Give me a width : "))
Givencover = int(input("Give me a cover : "))

pain_calc(GivenHeight, GivenWdith, Givencover)