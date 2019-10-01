class Person:  # Create a Parent Class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):   # Create a Child Class
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)


x = Student("Rana", "AlMuqati", 2019)
x.printname()
print(x.graduationyear)
x.welcome()