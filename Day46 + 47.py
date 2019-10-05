class Library:
    def __init__(self, shelf, book):
        self.shelf = shelf
        self.book = book


class ScienceSection(Library):
    def __init__(self, shelf, book, name):
        super().__init__(shelf, book)
        self.name = name

    def book1(self):
        print("Number of shelf:", self.shelf, "\nNumber of books:", self.book,"\nName of book:", self.name)


x = ScienceSection(45, 300, "Physics books")
x.book1()
print("After changing the number of shelf and book in child class:")
x.book = 20
x.shelf = 4
x.book1()


