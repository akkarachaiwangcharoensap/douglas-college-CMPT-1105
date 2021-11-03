# CMPT 1105 | Input Validation Using While Loop

```python
grade = int(input("Enter a grade"))

while (grade < 0 or grade > 100):
     grade = int(input("Please enter a grade between 0 and 100"))

if (grade >= 90):
     print("A")
elif (grade > 80):
     print("B")
elif (grade > 70):
     print("B")
elif (grade > 60):
     print("B")
else:
     print("F")
```
