# CMPT 1105 | Person Information

A Python example of taking multiple inputs and displaying in an appropriate manner. It also demonstrates the use of a Python module called `datetime`.

```python
firstName = input("What is your first name?")
lastName = input("What is your last name?")
yearOfBirth = int(input("What is your year of birth?"));

year = 2020
age = year - yearOfBirth;

print("Your first name is: " + firstName);
print("Your last name is: " + lastName);
print("You are: " + str(age));
```

A future-proof version
```python
import datetime

firstName = input("What is your first name?")
lastName = input("What is your last name?")
yearOfBirth = int(input("What is your year of birth?"));

year = datetime.datetime.now().year
age = year - yearOfBirth;

print("Your first name is: " + firstName);
print("Your last name is: " + lastName);
print("You are: " + str(age));
```
