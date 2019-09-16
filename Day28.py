i = 1
while i < 6:
    print(i)
    i += 1
print("The break Statement:")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # With the break statement we can stop the loop even if the while condition is true
    i += 1
print("The continue Statement:")
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue  # With the continue statement we can stop the current iteration, and continue with the next
    print(i)
print("The else Statement")
i = 1
while i < 6:
    print(i)
    i += 1
else:  # With the else statement we can run a block of code once when the condition no longer is true
    print("i is no longer less than 6")

