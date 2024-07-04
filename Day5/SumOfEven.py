Number = int(input("Give me a number: "))
Sum = 0

for Sum_even in range(2, Number + 1, 2):
    Sum += Sum_even

print(Sum);