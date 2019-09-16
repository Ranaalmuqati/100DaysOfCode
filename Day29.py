fruits = ["apple", "banana", "cherry", "orange", "mango"]
for x in fruits:
    print(x)
for x in "banana":  # Loop through the letters in the word "banana"
    print(x)
print("The break Statement:")
for x in fruits:
    print(x)
    if x == "banana":
        break  # With the break statement we can stop the loop before it has looped through all the items
print("The continue Statement:")
for x in fruits:
    if x == "banana":
        continue  # With the continue statement we can stop the current iteration of the loop, and continue with the next
    print(x)


