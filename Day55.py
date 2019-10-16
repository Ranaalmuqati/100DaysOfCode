import json

# some JSON:
x = '{"Name":"Rana", "Age":23, "City":"Riyadh"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y["Age"])


x = {"Name": "Rana", "Age": 23, "City": "Riyadh"}
# convert into json
y = json.dumps(x)
# the result is a json string
print(y)


x = {
  "name": "Rana",
  "age": 23,
  "married": False,
  "divorced": False,
  "children": None,
  "pets": True,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)
print(y)
