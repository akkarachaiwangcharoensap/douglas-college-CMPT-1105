gst = 0.05; # GST: 5%
pst = 0.07; # PST: 7%

price = float(input("Enter the price"))

newGST = (price * gst)
newPST = (price * pst)

total = newGST + newPST + price;

print ("GST: ", format(newGST, "0.2f"));
print ("PST: ", format(newPST, "0.2f"));
print ("Total: ", format(total, "0.2f"));