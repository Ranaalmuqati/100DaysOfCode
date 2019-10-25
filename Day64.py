try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello!!")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("The'try except' is finished")
