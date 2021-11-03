import datetime

firstName = input("What is your first name?")
lastName = input("What is your last name?")
yearOfBirth = int(input("What is your year of birth?"));

year = datetime.datetime.now().year
age = year - yearOfBirth;

print("Your first name is: " + firstName);
print("Your last name is: " + lastName);
print("You are: " + str(age));