price = {}
price["Laser sword"] = 229.0
price["Mintendo DX"] = 127.30
price["Linux cushion"] = 74.50
price["Goldorak briefs"] = 29.90
price["Nextpresso station"] = 184.60
totalPrice = 0.0
for itemPrice in price.values():
    totalPrice += itemPrice
print("The total price for the 5 items is : ", totalPrice)

removeItem = "Goldorak briefs"
if removeItem in price:
    del price[removeItem]
    print(f"{removeItem} has been removed from the price list.")
    totalPrice = 0.0
    for itemPrice in price.values():
        totalPrice += itemPrice
    print("The total price without Goldorak briefs is : ", totalPrice)