# If the year is divisible by 4, but not by 100, or it is divisible by 400, then it's a leap year.
# If the year is not divisible by 4, or it is divisible by 100 but not by 400, then it's not a leap year.

Year = int(input("Give me a year: "));

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("its a leap year");
else:
    print("its not a leap year");