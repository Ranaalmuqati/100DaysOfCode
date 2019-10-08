import mymodule as mx  # Re naming module
a = mx.person["age"]
print(a)

import platform
print(platform.python_version())

x = dir(platform)  # List all the defined names belonging to the platform module.
print(x)


from mymodule import person  # You can choose to import only parts from a module, by using the from keyword.
print(person["age"])

