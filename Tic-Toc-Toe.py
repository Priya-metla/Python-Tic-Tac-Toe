def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def play_game():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("\nWelcome to Tic-Tac-Toe!")
    print("Choose a position from 1 to 9.")
    print("Player 1: X | Player 2: O")

    while True:
        display_board(board)

        choice = input(
            f"Player {current_player}, enter position (1-9): "
        )

        if not choice.isdigit() or choice not in board:
            print("Invalid move! Choose an available position.")
            continue

        position = int(choice) - 1
        board[position] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if all(cell in ["X", "O"] for cell in board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").lower().strip()

    if again != "yes":
        print("Thanks for playing!")
        break
