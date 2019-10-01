class Person:  # Create a Parent Class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("john", "Doe")
x.printname()


class Student(Person):   # Create a Child Class
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("miki", "olsen")
x.printname()



