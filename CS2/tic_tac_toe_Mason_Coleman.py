"""
Name: Mason Coleman
Description: A tic-tac-toe game for two players where you pick a spot by row and column
Bugs: None that I know of
Bonus: None
Date: 10/26/26
Log: Initial Creation: 10/13/26
     10/14/26 Finished display board, win check, and draw check
     10/19/26 Finished first player picker and tested functions
     10/21/26 Finished get player move 
     10/26/26 Added play again and full documentation to all functions
"""
import random


def display_board(board):
    """Print the board with row and column labels

    Args: board - the 3x3 list
    Returns: nothing
    """
    print("    1   2   3")
    for i in range(3):
        print(f"{i + 1}   {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("   ---+---+---")

def has_won(board, player):
    """Check if one player has three in a row.

    Args: board - the 3x3 list of lists, player - "X" or "O"
    Returns: True if that player won, otherwise False
    """
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def check_winner(board):
    """Find out who won, if anyone

    Args: board - the 3x3 list
    Returns: "X", "O", or None if nobody has won
    """
    if has_won(board, "X"):
        return "X"
    if has_won(board, "O"):
        return "O"
    return None


def is_draw(board):
    """Check if the game is a draw

    Args: board - the 3x3 list 
    Returns: True if the board is full and nobody won, otherwise False
    """
    count = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                count += 1

    if count == 0 and check_winner(board) is None:
        return True
    else:
        return False


def first_player():
    """Ask for both names and randomly pick who goes first

    Args: none
    Returns: the first player's name, then the second player's name
    """
    player_1 = input("What is your name player 1: ").strip()
    player_2 = input("What is your name player 2: ").strip()
    names = (player_1, player_2)
    first = random.choice(names)
    if first == player_1:
        second = player_2
    else:
        second = player_1
    return first, second


def get_player_move(board, player):
    """Ask for a row and column until the move is valid

    Args: board - the 3x3 list, player - "X" or "O"
    Returns: row and column as board indexes (0 to 2)
    """
    while True:
        try:
            row = int(input(f"{player}, enter row (1-3): "))
            col = int(input(f"{player}, enter column (1-3): "))
        except ValueError:
            print("Numbers only")
            continue

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Must be between 1 and 3")
            continue

        row = row - 1
        col = col - 1

        if board[row][col] != " ":
            print("That spot is taken")
            continue

        return row, col


def play_again():
    """Ask if the players want another game

    Args: none
    Returns: True for yes, False for no
    """
    while True:
        again = input("Play again? (yes/no): ").strip().lower()
        if again == "yes":
            return True
        if again == "no":
            return False
        print("Please enter yes or no")


def play_game():
    """Run the game, including restarting the game 

    Args: none
    Returns: nothing
    """
    first, second = first_player()
    print(first, "goes first, then", second)

    while True:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        current = "X"
        current_name = first

        while True:
            display_board(board)
            print(current_name, "turn:", current)
            row, col = get_player_move(board, current)
            board[row][col] = current

            if check_winner(board) is not None:
                display_board(board)
                print(current_name, "wins!")
                if play_again() == False:
                    return
                break

            if is_draw(board):
                display_board(board)
                print("It's a draw!")
                if play_again() == False:
                    return
                break

            if current == "X":
                current = "O"
                current_name = second
            else:
                current = "X"
                current_name = first




if __name__ == "__main__":
    play_game()
