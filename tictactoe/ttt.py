import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def ai_move(board):
    # Check for winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"  # AI's symbol
                if check_winner(board) == "O":
                    return (i, j)
                board[i][j] = " "  # Reset the position

    # Check for blocking move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"  # Player's symbol
                if check_winner(board) == "X":
                    board[i][j] = "O"  # Block the player
                    return (i, j)
                board[i][j] = " "  # Reset the position

    # If no winning or blocking move, choose a random empty position
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_positions) if empty_positions else None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Player is X, AI is O
    for turn in range(9):
        print_board(board)
        if current_player == "X":
            while True:
                try:
                    row = int(input("Player X, enter your row (0-2): "))
                    col = int(input("Player X, enter your column (0-2): "))
                    if board[row][col] == " ":
                        break
                    else:
                        print("This position is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter numbers between 0 and 2.")
        else:
            row, col = ai_move(board)
            print(f"AI chooses position: {row}, {col}")

        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "O":
                print("AI wins!")
            else:
                print(f"Player {winner} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
