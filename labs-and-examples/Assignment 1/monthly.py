'''
Write a program that asks the user to enter the monthly cost of the following expenses
incurred from operating his/her automobile:

Loan payment,
Insurance,
Gas,
Tires.

The program receives these numbers in the main program (outside any function) and passes them
to a function called `total`. The function total calculates and returns annual cost.
The total annual cost is displayed in the main program.

Name the program file: monthly.py
'''

print ("Please enter your automobile expenses:")

loanPayment = float(input("Loan Payment"))
insurance = float(input("Insurance"))
gas = float(input("Gas"))
tires = float(input("Tires"))

def total(loanPayment, insurance, gas, tires):
        return (loanPayment + insurance + gas + tires) * 12;

total = total(loanPayment, insurance, gas, tires)

print("Total annual cost is ", total)
        
