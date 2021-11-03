firstName = str(input("Please enter your first name"))
middleName = str(input("Please enter your middle name"))
lastName = str(input("Please enter your last name"))

firstInitial = firstName[0]
secondInitial = middleName[0]
thirdInitial = lastName[0]

stringOutput = firstInitial + '.' + secondInitial + '.' + thirdInitial
print(stringOutput)
