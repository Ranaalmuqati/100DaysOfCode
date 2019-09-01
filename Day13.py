this_list = ["apple", "banana", "cherry"]
print(this_list)


numbers = [12, 15, 18, 20]
print("The List of 'numbers' is:", numbers)

print("The list item in index number 1 is:", this_list[1])

for x in numbers:
    print(x)

this_list[1] = "blackcurrant"
print(this_list)

del this_list[0]
print(this_list)
