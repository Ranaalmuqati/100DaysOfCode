print("Passing a List as a Parameter:")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)

print("Return Values:")


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(9))

print("Keyword Arguments:")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child3="Emil", child2="Tobias", child1="Linus")

print("Arbitrary Arguments:")
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


print("Recursion:")


def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)
