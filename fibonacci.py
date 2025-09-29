#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#Lab 3 Part 1: Fibonacci Sequence
# Setting up the loop
while True:
    term_input = input("Enter the number of terms: ")
    try:
        terms = int(term_input)
        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Error! Invalid input, please enter a valid input.")

#Print the Fibonacci sequence
#Fibonacci Sequence: 0 1 1 2 3 5 8 13 21 34 55 89 144
a = 0
b = 1
for i in range(terms):
    print(a, end=' ')
    a, b = b, a + b
          



