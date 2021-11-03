# CMPT 1105 | Global Variable

Global variable is a variable that can be accessed anywhere and anytime? Usually global variable is not a good practice due to its accessability. You should consider working with private or local variable since this variable will be destroyed and managed by the Garbage Collector (GC).

For examples

```python
def foo ():
  global x

foo()

x = 10 # 10

print(x)

x = 12

print(x) # 12
```
