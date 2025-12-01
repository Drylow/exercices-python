def abbreviate_name(name: str) -> str:
    parts = name.split(" ")
    first_initial = parts[0][0].upper()
    second_initial = parts[1][0].upper()
    return f"{first_initial}.{second_initial}"

result_1 = abbreviate_name("Sam Harris")
print(f"Sam Harris initials: {result_1}")

result_2 = abbreviate_name("Patrick Feeney")
print(f"Patrick Feeney initials: {result_2}")

result_3 = abbreviate_name("John Doe")
print(f"John Doe initials: {result_3}")