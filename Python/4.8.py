milk_price = 0.45
cider_price = 3.85
flour_price = 0.9
butter_price = 0.77
nutella_price = 1.87

orderPrice = (2 * milk_price) + (3 * cider_price) + flour_price + butter_price + nutella_price

allowanceMoney = 20
allowanceMoney = allowanceMoney - orderPrice

if allowanceMoney > 0:
    message = "You have spent " + str(orderPrice) + " you have left " + str(allowanceMoney)
elif allowanceMoney < 0:
    amountMissing = abs(allowanceMoney)
    message = "Sorry you're missing " + str(amountMissing) + " euros"
else:
    message = "You are broke!"

print(message)