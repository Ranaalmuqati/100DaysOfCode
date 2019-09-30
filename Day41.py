class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Rana", 23)
print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print("Hello my name is " + self.name)


p1 = Person("Rana", 23)
p1.fun()





