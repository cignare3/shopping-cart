import pandas
import os
import statistics
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print("Welcome to Tyler's Grocery Outlet")

total_price = 0
product_ids = []
options = str(list(range(1,21)))

while True:
    Selection_Identifier = input("Please enter a product id number or 'DONE' if there are no more items: ")
    if Selection_Identifier == "DONE":
        break 
    elif not Selection_Identifier:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
    elif Selection_Identifier not in options:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
    else: 
        product_ids.append(Selection_Identifier)       

print("--------------------------")
print("Tyler's Grocery Outlet")
print("Website: www.tylersgroceryoutlet.com Phone: 888-123-2345")
print("--------------------------")
now = datetime.datetime.now()
print ("Checkout At: " + now.strftime("%Y-%m-%d %I:%M:%S %p"))
print("--------------------------")

for Selection_Identifier in product_ids:
    matching_products = [p for p in products if str(p["id"]) == str(Selection_Identifier)]
    matching_product = matching_products[0]
    matching_product_price = "${0:,.2f}".format(matching_product["price"])
    total_price = total_price + matching_product["price"]
    tax_amount = total_price * .0875 
    total_amount = total_price + tax_amount
    print("Selected Product: " + matching_product["name"] + " ..... " + matching_product_price)

total_price = "${0:,.2f}".format(total_price)
print("SUBTOTAL: " + str(total_price)) 
tax_amount = "${0:,.2f}".format(tax_amount)
print("TAX: " + str(tax_amount))
total_amount = "${0:,.2f}".format(total_amount)
print("TOTAL: " + str(total_amount))


print("Thank you for shopping with us!")



    
    
