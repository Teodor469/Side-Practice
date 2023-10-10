def display_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def get_player_input():
    row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
    return row, col



board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]