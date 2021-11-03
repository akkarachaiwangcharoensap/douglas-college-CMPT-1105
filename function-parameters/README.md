# CMPT 1105 | Function Parameters

You can pass and change the order of the parameters or arugments pass in to the function.

```python
def greetings(x,y):
    print(y)
    x=x+1
    print(x)
    
print('good morning')
x=5
greetings(x,4.5)
print(x)
greetings(6,4.5)
```

To change the order of parameters:
```python
def foo (x, y):
  print(x)
  print(y)

foo(y=12, x=8)
```
