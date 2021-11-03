# CMPT 1105 | Celsius To Fahrenheit Calculation

A Python example of converting celcius to fahrenheit. This demonstrates the usage of taking user input, format a string, and output appropriate string format.

```python
# Fahrenheit = 1.8C + 32

celsius = float(input("Enter a celsius value"))
fahrenheit = format(1.8 * celsius + 32, '0.1f');

print("Celsius: " + str(celsius), " Fahrenheit: " + fahrenheit)
```
