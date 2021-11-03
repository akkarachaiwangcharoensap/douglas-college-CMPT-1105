'''
A customer in store is purchasing five items.
Write a program that asks for the price of each item, and then displays

the subtotal,
the amount of GST, PST,
and the total.

Name the program file: store.py
'''

# How many items
totalItems = 5;

GST = 0.05; # GST: 5%
PST = 0.07; # PST: 7%

subtotal = 0;
total = 0;
newGST = 0;
newPST = 0;

# Store the item prices
for index in range(0, totalItems):
        item = float(input("Please enter the item's price"))

        # Calculate the subtotal
        subtotal = subtotal + item

newGST = newGST + (subtotal * GST)
newPST = newPST + (subtotal * PST)

total = subtotal + (newGST + newPST);
        
print("Sub total", format(subtotal, "0.2f"))
print ("GST: ", format(newGST, "0.2f"))
print ("PST: ", format(newPST, "0.2f"))
print ("Total: ", format(total, "0.2f"))
