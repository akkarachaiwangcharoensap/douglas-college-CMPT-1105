# CMPT 1105 | Math Operators

In Python you can do basic arithmetic operations such as `addition`, `substraction`, `multiplication`, and `division`.

```python
a = 2;
b = 10;

a + b # = 12
a - b # = -8
a * b # = 20
a / b # = 0.2
```

However, there is a useful math operator called `Modulus`. The `Modulus` operator gives us a remainder of the division.

```python
10 % 2 # = 0
10 % 3 # = 1
```

A basic example usage of `modulus` is to determine if the value is an `even` or `odd`

```python
x = 10

if x % 2 == 0:
  print(x, 'is even')
else:
  print(x, 'is odd')

```
