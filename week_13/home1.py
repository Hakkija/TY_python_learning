class Book:
    def __init__(self, title, author, num_pages, book_type):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.book_type = book_type

    def print_info(self):
        print("{}, {}, {}, {}".format(self.title,
              self.author, self.num_pages, self.book_type))


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        print("Books in the library:")
        for book in self.books:
            book.print_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return book
        return None


# Create an empty library object
lib = Library()

# Read the books from the file
with open("books.txt", "r") as f:
    for line in f:
        values = line.strip().split(",")
        if len(values) != 4:
            print("Error: invalid format in line '{}'".format(line.strip()))
        else:
            book = Book(*values)
            lib.add_book(book)

# Print the books in the library
lib.print_books()

# Ask the user to borrow a book
while True:
    title = input("Enter the title of the book you want to borrow: ")
    book = lib.borrow_book(title)
    if book is not None:
        print("The book {} successfully borrowed!".format(book.title))
        lib.print_books()
        break
    else:
        print("Cannot find such book, try again!")
