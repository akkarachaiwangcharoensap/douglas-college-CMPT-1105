'''
A particular talent competition has four judges, each of whom awards a score between 0
and 10 to each performer. Fractional scores, such as 8.3, are allowed. A performer’s final
score is determined by averaging the four scores. Write a program that reads in 4 scores
and displays the average score. Your program would show an error message if any
score entered by the user is negative or greater than 10


Name the program file: Q2.py
'''

# How many integers
totalScoreInputs = 4;

# Total score
total = 0;

# The average score
average = 0;

# Ask for 4 inputs
for index in range(0, totalScoreInputs):
        # Ask the user for a float input
        scoreInput = float(input("Please enter a score"))

        while (scoreInput < 0 or scoreInput > 10):
                scoreInput = float(input("ERROR: Please enter a score value between 0 - 10"))

        # Add each integer to the total
        total = total + scoreInput

average = total / totalScoreInputs

print("The average score is: ", average)
