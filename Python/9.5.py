def sum_of_positive(numbers: list) -> int:
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

data_1 = [1, -4, 7, 12]
result_1 = sum_of_positive(data_1)
print(f"The sum of positive numbers in {data_1} is : {result_1}")

data_2 = [-1, -2, -3, -4]
result_2 = sum_of_positive(data_2)
print(f"The sum of positive numbers in {data_2} is : {result_2}")

data_3 = [10, 5, 0, -1]
result_3 = sum_of_positive(data_3)
print(f"The sum of positive numbers in {data_3} is : {result_3}")