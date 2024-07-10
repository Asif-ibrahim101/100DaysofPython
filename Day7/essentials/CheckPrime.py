def PrimeNumberCheck(Number):
    is_prime = True
    for i in range(2, Number):
        if Number % i == 0:
            is_prime = False
    
    if is_prime:
        print("its a prime number")
    else:
        print("its not a prime number")
        
Given_number = int(input(f"Give me a number: "))
PrimeNumberCheck(Given_number)