car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
x = car["model"]  # access the items of a dictionary by referring to its key name
print(x)
x = car.get("model")  # # also a method called get() that will give you the same result
print(x)
car["year"] = 2019 # change the value of a specific item by referring to its key name
print(car)
for x in car:  # Print all key names in the dictionary
    print(x)
    print(car[x])  # Print all values in the dictionary
for x in car.values():  # also use the values() function to return values of a dictionary:
    print(x)
print(car.values())
for x, y in car.items():  # Loop through both keys and values, by using the items() function
    print(x, y)
print(car.items())
