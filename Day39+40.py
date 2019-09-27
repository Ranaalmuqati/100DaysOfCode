print("Task One:")


def power(x, n):
    if n == 1:
        return x
    else:
        return x*power(x, n-1)


print(power(5, 3))

print("\nTask Two:")
numbers = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("The Positive numbers is:", positive_numbers)
