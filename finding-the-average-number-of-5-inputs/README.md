# CMPT 1105 | Finding The Average Number of 5 Inputs

While loop
```python
i = 0;
total = 0;
while (i < 5):
    number = int(input("Please enter a number"));

    total += number
    i+=1

average = int(total / 5);
print(average);
```

For loop
```python
total = 0
for i in range(0, 5):
    number = int(input("Please enter a number"))
    total += number;

average = int(total / 5)
print(average)
```
