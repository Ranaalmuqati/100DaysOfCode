print("Local Scope:")


def myfunc():
    x = 300  # A variable created inside a function is available inside that function
    print(x)


myfunc()

print("Function Inside Function:")


def myfunc():
    x = 300

    def myinnerfunc():  # The local variable can be accessed from a function within the function
        print(x)
    myinnerfunc()


myfunc()

print("Global Scope:")
x = 300


def myfunc():
    print(x)


myfunc()
print(x)




