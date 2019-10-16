import json

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
# use four indents to make it easier to read the result
'''
You can also define the separators, default value is (" . ", " = "), 
which means using " . " and a space to separate each 
object, and  using " = " and a space to separate keys from values
'''
# Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=4, separators=(".", "="), sort_keys=True))
