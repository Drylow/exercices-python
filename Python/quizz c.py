car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car["year"])

for k in car.keys():
    print(k)

for v in car.values():
    print(v)

for i, (k, v) in enumerate(car.items()):
    print(i, k, v)

d = {f"cle{i}": car for i in range(1, 4)}
print (d)