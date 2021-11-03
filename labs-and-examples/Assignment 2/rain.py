'''
Design a program that lets the user enter the total rainfall for each of 12
months. These numbers are stored in a list. The program should calculate
and display the total rainfall for the year, the average monthly rainfall, and
the months with the highest and lowest amounts. So, if in July (7th month of
a year) rainfall has been the minimum with a value of 2 mm, your program
should display a message like this:

Month 7 (July) had the minimum rainfall (2 mm)

Name the program file: rain.py
'''

totalRainfall = 0;
averageRainfall = 0;
months = []

# ask for inputs
for i in range(12):
        rainfall = int(input("What is the rainfall of this month (mm)?"))
        totalRainfall = totalRainfall + rainfall;
        months.append(rainfall)

# get the average
averageRainfall = totalRainfall / 12;

# assume the lowest raindrop is at first month
lowest = months[0]

lowestCounter = 0
lowestAtIndex = -1;
# find the lowest rainfall
for month in months:
        if (lowest > month):
                lowestAtIndex = lowestCounter;
                lowest = month

        lowestCounter = lowestCounter + 1;

largest = months[0]

largestCounter = 0
largestAtIndex = -1;
# find the largest rainfall
for month in months:
        if (largest < month):
                largestAtIndex = largestCounter;
                largest = month

        largestCounter = largestCounter + 1;

def getRainfall (month, lowest):
        # Assume we start at index = 0;
        if (month == 0):
                return 'Month '+str(month + 1)+' (January) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 1):
                return 'Month '+str(month + 1)+' (February) had the minimum rainfall ('+str(lowest)+ ' mm)'
        elif (month == 2):
                return 'Month '+str(month + 1)+' (March) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 3):
                return 'Month '+str(month + 1)+' (April) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 4):
                return 'Month '+str(month + 1)+' (May) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 5):
                return 'Month '+str(month + 1)+' (June) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 6):
                return 'Month '+str(month + 1)+' (July) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 7):
                return 'Month '+str(month + 1)+' (August) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 8):
                return 'Month '+str(month + 1)+' (September) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 9):
                return 'Month '+str(month + 1)+' (October) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 10):
                return 'Month '+str(month + 1)+' (November) had the minimum rainfall ('+str(lowest)+' mm)'
        elif (month == 11):
                return 'Month '+str(month + 1)+' (December) had the minimum rainfall ('+str(lowest)+' mm)'

print("The total rainfall is " + format(totalRainfall, '0.1f'))
print("The average rainfall is: " + format(averageRainfall, '0.1f'))
print(getRainfall(lowestAtIndex, lowest))
print(getRainfall(largestAtIndex, largest))

