# CMPT 1105 | If Statements

The `if` statement is a boolean-comparison operation of a given input.

```python
if condition:
  statement1
  statement2
  statement3
```

For example,

```python
if (2 > 1):
  # The condition is true
  print('Number 2 is larger than number 1')
else:
  # The condition is false
  print('Impossible!')
```

Else If Statement
```python
x = 5
if (x > 5):
  print('x is greater than 5')
elif (x <= 5)
  print('x is less than or equal to 5')
```

Nested If Statement
```python
if (x < 5):
  print('x is less than 5')
  if (x == 2)
    print('and x is equal to 2')
```

Multiple ifs VS Multiple elifs
`if () if () if () VS if () elif() elif()`

```python
if (1 == 1):
  print('1')
if (1 == 1):
  print('1')
if (1 == 1):
  print('1')

# To see the difference, try to uncomment the code below and comment the code above and vice versa. Compare the string output inside the console.
'''
if (1 == 1):
  print('1')
elif (1 == 1):
  print('1')
elif (1 == 1):
  print('1')
'''
```

Indentation
A tab, or you can use 4 spaces. You MUST indent your code or it will not work. This is important in Python because that is how the interpreter interprets it.
