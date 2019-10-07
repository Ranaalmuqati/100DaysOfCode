x = 300


def myfunc():
    x = 200
    print(x)


# The function will print the local x, and then the code will print the global x
myfunc()
print(x)


def myfunc():
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
    global x
    x = 300


myfunc()
print(x)


x = 300


def myfunc():
    global x  # Also, use the global keyword if you want to make a change to a global variable inside a function.
    x = 200


myfunc()
print(x)
