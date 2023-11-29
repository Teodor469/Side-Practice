class MusicCollection:
    def __init__(self) -> None:
        self.collection = {}

    def add_piece(self, piece, composer, key, print_message = True):
        if piece in self.collection:
            print(f"{piece} is already in the collection!")
        else:
            self.collection[piece] = {"compser": composer, "key": key}
            if print_message:
                print(f"{piece} by {composer} in {key} added to the collection!")