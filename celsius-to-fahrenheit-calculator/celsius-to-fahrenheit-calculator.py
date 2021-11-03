# Fahrenheit = 1.8C + 32

celsius = float(input("Enter a celsius value"))
fahrenheit = format(1.8 * celsius + 32, '0.1f');

print("Celsius: " + str(celsius), " Fahrenheit: " + fahrenheit)