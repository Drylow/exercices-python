import random

price_to_find = random.randint(1, 100)

def find_price():
    while True:
        guess = int(input("Enter a price : "))
        if guess > price_to_find:
            print("It's less.")
        elif guess < price_to_find:
            print("It's more.")
        else:
            print("Well done, you won!")
            break

find_price()