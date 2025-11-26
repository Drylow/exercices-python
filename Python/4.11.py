currency = input("Enter currency (E for euros or $ for dollars) : ")
amount = float(input("Enter amount 10: "))

if currency == "E":
    conversion = amount * 1.1
    print(f"{amount} euros = {conversion} dollars")
else:
    conversion = amount / 1.1
    print(f"{amount} dollars = {conversion} euros")