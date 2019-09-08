fruits = {"apple", "banana", "cherry", "orange", "mango"}
print(len(fruits))  # using len() to know how many item in set

fruits.remove("mango")  # Remove item by using the remove() method
print(fruits)

fruits.discard("cherry")  # Remove item by using the discard() method
print(fruits)

fruits.pop()  # Remove the last item by using the pop() method
print(fruits)

fruits.clear()  # The clear() method empties the set
print(fruits)

fruits = set(("apple", "banana", "cherry", "orange", "mango"))
print(fruits)




