# CMPT 1105 | Function

Divide and conquer is a strategy to divide the problem into a small subset of problems. This is to help you manage smaller problem and combine the solutions and solve the issues. If you want better definition, go look up Divide and Conquer Strategy.

Function is a way to reuse or build a function for a specific task.
```python
def functionName:
  # your code goes here
```

For examples
```python
def hello ():
  print("Hello")

hello()
```


```python
x = "Aki"
def greet (name):
  print (name)

greet(x)
```

Function workflow

```python
def greetings():
        print("hello")
        main()
        print("Hola")
        
def main():
        print("I am in the main funtion")
x=6
main()
print(x)
greetings()
print("bye")
greetings()
print("Adios")
```

`main` function is a function that is usually called when the program started. In many programming languages such as Java, C#, C++ and many others. `main` function is what you need to consider when naming your function. You CANNOT name your function `main` or this will conflict and throw out errors.
