class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print("Hello my name is " + self.name)


p1 = Person("Rana", 23)
p1.age = 24  # Modify Object Properties
print(p1.age)


