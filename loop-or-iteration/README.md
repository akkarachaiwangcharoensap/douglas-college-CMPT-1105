# CMPT 1105 | Loop or Iteration

Loop or iteration is way to iterate or go through each item in the array, collection or dictionary.

There are many different types of iteration.

While Loop

```python
i = 0
while (i < 5):
  print(i)
  i = i + 1
```

While Loop: Infinite

```python
while (2 > 1)
  print("INFINITE POWER!!!")
```

For Loop
```python
for i in [1, 2, 3, 4, 5, 6]:
  print(i);
```

The square bracket above is called array or list.
You can put multiple values there.
For example,

```python
myArray = ["Hello", "I am", "a", "JEDI!"]

for i in myArray:
  print(i)
```

Using range() function instead of an array. This will generate a number from 0 - 4. It is not 5 because, if you count each number correctly. You will reach at the end by number 4. You count at 0.

```python
for i in range(5):
  print(i)
```

If you want to get from a to b, you need something like this:
```python
for i in range(1, 5 + 1):
  print(i)
```

For loop with each step value to other than 1
```python
for i in range(0, 10, 2):
  print(i)
```

This will skip every 2s
