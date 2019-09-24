def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(2)  # n = 2
print(mydoubler(11))  # a = 11


def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(3)  # n = 3
print(mydoubler(11))  # a = 11

# use the same function definition to make both functions, in the same program


def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(2)  # n = 2
mytripler = myfunc(3)  # n = 3
print(mydoubler(11))  # a = 11
print(mytripler(11))  # a = 11



