# A food list
foods = ["Rice", "Apple", "Eggs"]

# Access an item in the list
rice = foods[0]
apple = foods[1]
eggs = foods[2]

print(rice) # Rice
print(apple) # Apple
print(eggs) # Eggs

# Changing / Updating
foods[0] = "Pasta"
pasta = foods[0] # Pasta

# Adding / Appending
foods.append("Bacon")
bacon = foods[3] # Bacon

# Deleting an item
del foods[0] # Deleting "Rice"

# Get a number of items
print(len(foods)) # 3 items, remember, we deleted "Rice"

# Reverse a list
reversedFoods = foods.reverse()
