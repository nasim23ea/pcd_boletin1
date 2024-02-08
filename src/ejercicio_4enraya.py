def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (len(board) * 2 - 1))


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + 3 - i][col + i] == player for i in range(4)):
                return True

    return False


def is_valid_move(board, column):
    return column >= 0 and column < len(board[0]) and board[0][column] == " "


def drop_piece(board, column, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            break


def main():
    rows = 6
    cols = 7
    board = [[" "] * cols for _ in range(rows)]
    player = "X"

    while True:
        print_board(board)
        column = int(input(f"Player {player}, choose a column (0-{cols - 1}): "))
        
        if is_valid_move(board, column):
            drop_piece(board, column, player)
            
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if all(board[0][i] != " " for i in range(cols)):
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("Invalid move! Try again.")


