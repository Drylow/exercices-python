def summation(number):
    total = 0
    addition = ""
    for i in range(1, number + 1):
        total += i
        if i < number:
            addition += str(i) + " + "
        else:
            addition += str(i)
    print(addition)
    return total

user_input = int(input("Enter a positive integer : "))
result = summation(user_input)
print(result)