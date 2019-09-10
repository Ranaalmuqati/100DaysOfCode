car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in car:
    print("Yes, model in car dictionary")
print(len(car))
car["color"] = "Red"  # Adding an item to the dictionary is done by using a new index key and assigning a value to it
print(car)
car.pop("model")  # The pop() method removes the item with the specified key name
print(car)
car.popitem()  # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed
print(car)
del car["year"]  # The del keyword removes the item with the specified key name
print(car)
car.clear()  # The clear() keyword empties the dictionary
print(car)




