#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# Setting up the loop
while True:
  term_input = int(input("How many terms of the Fibonacci Sequence do you want printed? : "))
  if term_input > 0:
    break
  else:
  print("Error! Invalid input, please try again.")

a = 0
b = 1 
for i in range(term_input):
  print(a, end= " ")
  c = a + b

          



