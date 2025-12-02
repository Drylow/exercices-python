first_list = [1, 3, 2, 7, 4, 10, 46]

print(first_list[:3])

second_list = first_list[2:5]

third_list = first_list + second_list

tuple_of_lists = list(zip(first_list, second_list))

first_list.append(5)

third_list.append(None)

def concat_list(my_list, n=2):
    return my_list * n

i = 0
while third_list[i] is not None:
    print(third_list[i])
    i += 1

count_even = 0
for x in first_list:
    if x % 2 == 0:
        count_even += 1
print(count_even)

even_numbers = []
for element in first_list:
    if element % 2 == 0:
        even_numbers.append(element)

def first_single_letter(s):
    for c in s:
        if s.count(c) == 1:
            return c