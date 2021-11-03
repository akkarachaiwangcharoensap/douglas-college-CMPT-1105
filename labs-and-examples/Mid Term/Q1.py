'''
Write a program that reads in five integer numbers and that outputs:
- the sum of all positive numbers
- the sum of all negative numbers
- the sum of all numbers, whether positive, negative, or zero.
The user enters the five numbers in any order. Your program does not ask the user to
enter the positive numbers and the negative numbers separately. 


Name the program file: Q1.py
'''

# How many integers
totalIntegerInputs = 5;

# Positive Sum
posTotal = 0;

# Negative Sum
negTotal = 0;

# Sum of all
total = 0;

# Ask for 5 inputs
for index in range(0, totalIntegerInputs):
        # Ask the user for an integer input
        integerInput = int(input("Please enter an integer"))

        # Positive integers
        if (integerInput > 0):
                posTotal = posTotal + integerInput;
        # Negative integers
        else:
                negTotal = negTotal + integerInput;
                
        # Add each integer to the total
        total = total + integerInput

print("The sum of positive integers is: ", posTotal)
print("The sum of negative integers is: ", negTotal)
print("The sum of integers is: ", total)
