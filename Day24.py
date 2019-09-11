car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
newcar = car.copy()  # Make a copy of a dictionary with the copy() method:
print(newcar)
newcar = dict(car)  # Another way to make a copy is to use the built-in method dict().
print(newcar)
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004},
  "child2": {
    "name": "Tobias",
    "year": 2007},
  "child3": {
    "name": "Linus",
    "year": 2011}}
print(myfamily)
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)

car = dict(brand="Ford", model="Mustang", year=1964)
print(car)
