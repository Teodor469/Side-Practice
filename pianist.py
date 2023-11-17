class MusicCollection:
    def __init__(self):
        self.collection = {}

    def add_piece(self, piece, composer, key, print_message=True):
        if piece in self.collection:
            if print_message:
                print(f"{piece} is already in the collection!")
        else:
            self.collection[piece] = {'composer': composer, 'key': key}
            if print_message:
                print(f"{piece} by {composer} in {key} added to the collection!")

    def remove_piece(self, piece):
        if piece not in self.collection:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del self.collection[piece]
            print(f"Successfully removed {piece}!")

    def change_key(self, piece, new_key):
        if piece in self.collection:
            self.collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

number_of_initial_pieces = int(input())

music_collection = MusicCollection()

for n_lines in range(number_of_initial_pieces):
    piece_info = input().split('|')
    music_collection.add_piece(*piece_info, print_message=False)

while True:
    command = input().split('|')

    if command[0] == 'Stop':
        break

    action, piece = command[0], command[1]

    if action =='Add':
        music_collection.add_piece(piece, command[2], command[3])
    elif action == 'Remove':
        music_collection.remove_piece(piece)
    elif action == 'ChangeKey':
        music_collection.change_key(piece, command[2])
    
for piece, info in music_collection.collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")