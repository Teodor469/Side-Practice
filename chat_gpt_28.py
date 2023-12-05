class Library:
    def __init__(self) -> None:
        self.library_database = {}

    def add_book(self, title, author, genre, isbn):
        if isbn not in self.library_database:
            self.library_database[isbn] = {'title': title, 'author': author, 'genre': genre}
            print(f"Book '{title}' added to the library.")
        else:
            print("Book already in the library.")

    def display_info(self, isbn):
        if isbn in self.library_database:
            print(self.library_database[isbn])
        else:
            print("Book not found.")

    def update_genre(self, isbn, new_genre):
        if isbn in self.library_database:
            self.library_database[isbn]['genre'] = new_genre
            print(f"Changed the genre of '{self.library_database[isbn]['title']}' to {new_genre}.")
        else:
            print("ISBN not found.")

    def remove_book(self, isbn):
        if isbn in self.library_database:
            title = self.library_database[isbn]['title']
            del self.library_database[isbn]
            print(f"Book '{title}' successfully removed.")
        else:
            print("Book not found.")


library_database = Library()

while True:
    command = input().split(':')
    if command[0] == 'End':
        break

    action, isbn = command[0], command[1]

    if action == "AddBook":
        library_database.add_book(command[2], command[3], command[4], isbn)
    elif action == "DisplayInfo":
        library_database.display_info(isbn)
    elif action == "Update":
        library_database.update_genre(isbn, command[2])
    elif action == "Remove":
        library_database.remove_book(isbn)
