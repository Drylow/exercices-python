def mixed_sum(arr: list) -> int:
    total = 0
    for item in arr:
        total += int(item)
    return total

data_1 = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
result_1 = mixed_sum(data_1)
print(f"The sum of the mixed array {data_1} is : {result_1}")

data_2 = [9, 3, '7', '3']
result_2 = mixed_sum(data_2)
print(f"The sum of the mixed array {data_2} is : {result_2}")

data_3 = ['10', '10', '10']
result_3 = mixed_sum(data_3)
print(f"The sum of the mixed array {data_3} is : {result_3}")