inputs = []
for index in range(6):
        newNumber = int(input("Please enter an integer number"))
        inputs.append(newNumber)

n = int(input("Please enter a number you want to compare"))

for number in inputs:
        if (number > n):
                print("Number: " + str(number) + " is greater than " + str(n))


