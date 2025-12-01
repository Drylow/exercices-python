def count_sheep(number):
    result = ""
    for i in range(1, number + 1):
        result += str(i) + " sheep..."
    return result

user_input = int(input("Enter a positive integer : "))
print(count_sheep(user_input))