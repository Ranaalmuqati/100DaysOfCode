x = 5
print(x > 3 or x < 4)  # returns True because " 5 is greater than 3".
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print("banana" in x)  # returns True because a sequence with the value "banana" is in the list
print("lemon" not in x)  # returns True because a sequence with the value "lemon" is not in the list

