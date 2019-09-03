fruits = ["apple", "banana", "cherry", "orange", "mango"]
print(len(fruits))
fruits.append("Kiwi")  # Method to append an item
print(fruits)
fruits.insert(2, "melon")  # To add an item at the specified index
print(fruits)
fruits.remove("banana")  # Method removes the specified item
print(fruits)
mylist = fruits.copy()   # one way to  make a copy  of list
mylist2 = list(fruits)  # Another way to  make a copy  of list
fruits.pop()  # Method removes the specified index or the last item if index is not specified
print(mylist)
print(mylist2)
print(fruits)
fruits.pop(0)
print(fruits)
fruits.clear()  # Method empties the list
print(fruits)

