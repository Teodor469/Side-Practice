class Book:
    def __init__(self, title: str, author: str, status: bool) -> None:
        self.title = title
        self.author = author
        self.status = status  # True for available, False for checked out

class Library:
    def __init__(self):
        self.books = {}  # Use a dictionary to store books with ISBN as keys

    def add_book(self, isbn, title, author):
        if isbn not in self.books:
            self.books[isbn] = {"title": title, "author": author, "status": "available"}

    def del_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def checkout(self, isbn):
        if isbn in self.books and self.books[isbn]["status"] == "available":
            self.books[isbn]["status"] = "checked out"
            return True
        else:
            return False

    def return_book(self, isbn):
        if isbn in self.books and self.books[isbn]["status"] == "checked out":
            self.books[isbn]["status"] = "available"
            return True
        else:
            return False