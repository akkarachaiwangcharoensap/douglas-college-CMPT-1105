# CMPT 1105 | Local Variable

Local variable is the variable inside the function or inner of something. That is what local is referring to.

For examples
```python
def foo ():
  x = 10

print(x) # this will throw out errors
```

```python
x = 123
def foo ():
  x = 10
  print(x)

foo() # this will output 10
print(x) # this will output 123
```
