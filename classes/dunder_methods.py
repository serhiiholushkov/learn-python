# Magic methods (dunder methods) are special methods with double underscores at the beginning and end of their names.
# They allow you to define how your objects behave with built-in operations.
# Common dunder methods include __init__, __str__, __repr__, __add__, __


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.num_pages} pages"

    def __eq__(self, other):
        if isinstance(other, Book):
            return (
                self.title == other.title
                and self.author == other.author
                and self.num_pages == other.num_pages
            )
        return False

    def __lt__(self, other):
        """Define less than comparison based on number of pages."""
        if isinstance(other, Book):
            return self.num_pages < other.num_pages
        return NotImplemented

    def __gt__(self, other):
        """Define greater than comparison based on number of pages."""
        if isinstance(other, Book):
            return self.num_pages > other.num_pages
        return NotImplemented

    def __add__(self, other):
        """Define addition to combine two books into a collection."""
        if isinstance(other, Book):
            return [self, other]
        return NotImplemented


book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
print(book1)  # Default __repr__ from object class
print(book2)  # Default __repr__ from object class

print(book1 == book2)  # Uses __eq__ method
book3 = Book("1984", "George Orwell", 328)
print(book1 == book3)  # Uses __eq__ method

print(book1 > book2)  # Uses __gt__ method
print(book1 < book2)  # Uses __lt__ method

collection = book1 + book2  # Uses __add__ method
print("Book collection length:", len(collection))
