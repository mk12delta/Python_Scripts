#!/usr/bin/env python3

#Application to convert temperatures between farenheit and celsius

while True:
    choice = input(
            "Enter 'F' for Fahrenheit to Celsius,\n"
            "'C' for Celsius to Fahrenheit,\n"
            "or 'quit' to exit: "
        )

    if choice == "quit":
        print("Exiting the temperature converter.")
        break

    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f'{fahrenheit:.2f}\N{DEGREE SIGN}F is {celsius:.2f}\N{DEGREE SIGN}C')
        print()

    elif choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f'{celsius:.2f}\N{DEGREE SIGN}C is {fahrenheit:.2f}\N{DEGREE SIGN}F')
        print()

    else:
        print("Invalid choice. Please enter 'F', 'C', or 'quit'.")
