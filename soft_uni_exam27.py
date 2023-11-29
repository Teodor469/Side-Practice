class Library:
    def __init__(self) -> None:
        self.book_collection = {}

    def add_book(self, title, author, genre):
        if title in self.book_collection:
            print(f"{title} is already in the library!")
        else:
            self.book_collection[title] = {'author': author, 'genre': genre}
            print(f"{title} by {author} in {genre} added to the library!")

    def remove_book(self, title):
        if title in self.book_collection:
            del self.book_collection[title]
            print(f"Successfully removed {title}!")
        else:
            print(f"Invalid operation! {title} does not exist in the library.")

    def change_genre(self, title, new_genre):
        if title in self.book_collection:
            self.book_collection[title]['genre'] = new_genre
            print(f"Changed the genre of {title} to {new_genre}!")
        else:
            print(f"Invalid operation! {title} does not exist in the library.")

# Read the number of initial books
number_of_initial_books = int(input())
book_collection = Library()

# Read and process each command until "Stop" is encountered
for _ in range(number_of_initial_books):
    book_info = input().split("|")
    book_collection.add_book(book_info[0], book_info[1], book_info[2])

while True:
    command = input().split("|")

    if command[0] == 'Stop':
        break

    action, title = command[0], command[1]

    if action == 'Add':
        book_collection.add_book(title, command[2], command[3])
    elif action == 'Remove':
        book_collection.remove_book(title)
    elif action == "ChangeGenre":
        book_collection.change_genre(title, command[2])

# Print the final collection
for title, info in book_collection.book_collection.items():
    print(f"{title} -> Author: {info['author']}, Genre: {info['genre']}")
