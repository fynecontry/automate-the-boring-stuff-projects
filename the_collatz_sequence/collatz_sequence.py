#!/usr/bin/env python3

def collatz(number):
    """
    Recurvise function which reduces passed integer to 1 using Collatz sequence
    """

    # Check if number is even or odd
    if number % 2 == 0:
        return_value = (number // 2)
        print(return_value)
        return return_value
    else:
        return_value = (3 * number + 1)
        print(return_value)
        return return_value

#Catch bad inputs (non-integers)
try:
    selected_number = int(input("Enter number: "))
except ValueError:
    print(f"Invalid input, please enter an integer.")


collatz_value = collatz(selected_number)

# Loop until collatz returns value 1
while collatz_value > 1:
    collatz_value = collatz(collatz_value)
