
########  Restaurant Menu Update  #########
# Add a new category called "Beverages" with at least two items:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Late" : 2.30, "Tea": 1.60}

# Update the price of "Steak" to 17.99:

restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters". 

restaurant_menu["Starters"].pop("Bruschetta", None)

print(restaurant_menu)