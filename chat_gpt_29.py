class Movies:
    def __init__(self) -> None:
        self.database_movies = {}

    def add_movie(self, title, director, release_year, genre, rating):
        if title not in self.database_movies:
            self.database_movies[title] = {'director': director, 'release_year': release_year, 'genre': genre, 'rating': rating}
            print(f"Movie {title} added to the database.")
        else:
            print("Movie already in database.")

    def information(self, title):
        if title in self.database_movies:
            print(self.database_movies[title])
        else:
            print("Movie does not exist in database.")

    def update_rating(self, title, new_rating):
        if title in self.database_movies:
            self.database_movies[title]['rating'] = new_rating
            print(f"Movie {title} has a new rating of {new_rating}")
        else:
            print("Movie does not exist in database.")

    def remove_movie(self, title):
        if title in self.database_movies:
            del self.database_movies[title]
            print(f"Movie {title} has been removed.")
        else:
            print("Movie does not exist in database.")

    def top_rated(self):
        if self.database_movies:
            top_movie = max(self.database_movies, key=lambda x: self.database_movies[x]['rating'])
            print(f"The top-rated movie is '{top_movie}' with a rating of {self.database_movies[top_movie]['rating']}")
        else:
            print("No movies in the database.")


movie_database = Movies()

while True:
    command = input().split(': ')

    if not command or not command[0]:
        continue  # Ignore empty or incomplete commands

    action = command[0]

    if action == "END":
        break

    if len(command) > 1:
        title = command[1]
    else:
        title = None

    if action == "AddMovie":
        movie_database.add_movie(title, command[2], command[3], command[4], command[5])
    elif action == "information":
        movie_database.information(title)
    elif action == "UpdateRating":
        movie_database.update_rating(title, command[2])
    elif action == "RemoveMovie":
        movie_database.remove_movie(title)
    elif action == "Top":
        movie_database.top_rated()