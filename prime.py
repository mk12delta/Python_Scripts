#!/usr/bin/env python3

#Application to check if submitted number is prime

def prime_check(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # 2 is the only even prime
    if n == 2:
        return True
    # Exclude all other even numbers
    if n % 2 == 0:
        return False

    #Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False #this finds factors, so no prime

    return True #No factors, this is prime

while True:
    entry = input("Enter a number to check if it's prime\n"
                    "(or 'quit' to exit): ")
    if entry == "quit":
        print("Exiting the prime number program.")
        break
    
    number = int(entry)

    if prime_check(number) == True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

