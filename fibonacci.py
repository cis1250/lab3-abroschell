#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#Lab 3 Part 1: Fibonacci Sequence
# Setting up the loop
while True: # starts the infintie loop
    input = input("Enter the number of terms: ") # getting the user input for the amount of terms
    try:
        terms = int(input)
        if terms <= 0: # checks if it is a non-positive integer
            print("Please enter a positive integer.")
        else:
            break
    except ValueError: # if the user input is not valid prints the error
        print("Error! Invalid input, please enter a valid input.")

# print the user input
print("User Input: ", terms)

#Print the Fibonacci sequence
#Fibonacci Sequence: 0 1 1 2 3 5 8 13 21 34 55 89 144
a = 0
b = 1
for i in range(terms): 
    print(a, end=' ')
    a, b = b, a + b # the new value of a becomes b's old value, the new value of b is the old a and b added together
          



