'''
Write a program that asks for a number in the range of 1 through 7.
The program displays the corresponding day of the week.

1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
7 = Sunday

The program displays an error message if the user enters a number outside
the range of 1 through 7.

Name it program file: week.py
'''

day = int(input("Please enter a number of the day of the week, 1 to 7"))

if (day < 0 or day > 7):
        print("ERROR: the input is out of range")

elif (day == 1):
        print("It is Monday.")
elif (day == 2):
        print("It is Tuesday.")
elif (day == 3):
        print("It is Wednesday.")
elif (day == 4):
        print("It is Thursday.")
elif (day == 5):
        print("It is Friday.")
elif (day == 6):
        print("It is Saturday.")
elif (day == 7):
        print("It is Sunday.")
