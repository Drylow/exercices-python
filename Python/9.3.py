def is_divisible(n: int, x: int, y: int) -> bool:
    return n % x == 0 and n % y == 0

result_1 = is_divisible(3, 1, 3)
print(f"Is 3 divisible by 1 and 3? {result_1}")

result_2 = is_divisible(12, 2, 6)
print(f"Is 12 divisible by 2 and 6? {result_2}")

result_3 = is_divisible(100, 5, 3)
print(f"Is 100 divisible by 5 and 3? {result_3}")

result_4 = is_divisible(12, 7, 5)
print(f"Is 12 divisible by 7 and 5? {result_4}")