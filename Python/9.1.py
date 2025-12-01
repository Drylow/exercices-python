def hello(name: str = None) -> str:
    if name is None:
        return "Hello Anonymous"
    return f"Hello {name}"

greeting1 = hello("Jean")
print(f"Test 1 (Jean): {greeting1}") 

greeting2 = hello()
print(f"Test 2 (vide): {greeting2}")

greeting3 = hello("Elliot Alderson")
print(f"Test 3 (Elliot Alderson): {greeting3}")