# CMPT 1105 | Province Majority

```python
birthdate = int(input("Please enter your year of birth."))
province = input("Please enter your province")

# 18
ALBERTA = "AB"
MANITOBA = "MB"
ONTARIO = "ON"
PRINCE_EDWARD_ISLAND = "PI"
SASKATCHEWAN = "SK"

# 19
BRITISH_COLUMBIA = "BC"
NEW_BRUNSWICK = "NB"
NEWFOUNDLAND = "NF"
NOVA_SOCOTIA = "NS"

age = 2020 - birthdate

if (age >= 18 and (province == ALBERTA or province == MANITOBA or province == ONTARIO or province == PRINCE_EDWARD_ISLAND or province == SASKATCHEWAN)):
    print ("You are now an adult, now, become a free and responsible citizen.")
elif (age >= 19 and (province == BRITISH_COLUMBIA or province == NEW_BRUNSWICK or province == NEWFOUNDLAND or province == NOVA_SOCOTIA)):
    print ("You are now an adult, although, a late one. Now, become a free and responsible citizen.")
else:
    print ("BRRT, you are either an underage or not from the true great north of CANADA.")
```
