# write a tic tac toe game
# define main
def main():
    # create the board
    board = create_board()
    # display the board
    display_board(board)

# 1. Create a 3x3 board
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# 2. Display the board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# 3. create two players X and O
def create_players():
    return ['X', 'O']

# 4. get player input
def get_player_input(player):
    row = int(input(f"Player {player}, enter row number (0, 1, 2): "))
    col = int(input(f"Player {player}, enter column number (0, 1, 2): "))
    return row, col

if __name__ == '__main__':
    main()