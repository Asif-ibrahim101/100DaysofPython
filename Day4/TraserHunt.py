line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter);
number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")






# if position == "A1" :
#     change1 = line1[0] = "X"
#     print(change1)
# elif position == "A2" :
#     change2 = line2[0] = "X"
#     print(change2)
# elif position == "A3" :
#     change3 = line3[0] = "X"
#     print(change3)
# elif position == "B1" :
#     change4 = line1[1] = "X"
#     print(change4)
# elif position == "B2" :
#     change5 = line2[1] = "X"
#     print(change5)
# elif position == "B3" :
#     change6 = line3[1] = "X"
#     print(change6)
# elif position == "C1" :
#     change7 = line1[2] = "X"
#     print(change7)
# elif position == "C2" :
#     change8 = line2[2] = "X"
#     print(change8)
# elif position == "C3" :
#     change9 = line3[2] = "X"
#     print(change9)
# else:
#     print("sorry can't take the input cause its not valid")