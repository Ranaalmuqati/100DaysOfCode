set = {}
print(set)
fruits = {"apple", "banana", "cherry", "orange", "mango"}
print(fruits)
set = {1, 2, 2, 3, "Hi", "Hi"}
print(set)
for x in fruits:
    print(x)
print("banana" in fruits)
fruits.add("kiwi")  # Using the add() method to add "just on item" to a set
print(fruits)
fruits.update(["grapes", "buleberry", "lemon"])  # Using the update() method to add more than one item to a set
print(fruits)

