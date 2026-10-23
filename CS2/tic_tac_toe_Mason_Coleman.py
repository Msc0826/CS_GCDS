#plan work, work plan
'''
step 1. create a 3x3 grid (3 rows, 3 columns) - 2d
step 2. 2 human players - 
step 3. determine who goes first - make it random 
step 4. let player 1 choose if their x or o 
step 5. ask player 1 where they want to go
step 6. have player 1 enter row and col or name each box (box 1 (top left)) 
step 7. check if someone has already played in that spot (check everytime)
step 8. check if someone won - if grid [0][0] == 'x' and grid[0][1] = 'x' and grid[0][2] == 'x' 
	you also have to check if someone won any other ways (8 ways to win) 
step 10. check for a tie 
step 11. ask player 2 their choice
step 12. check if someone played in that box they choose etc etc 
step 13. if someone wins ask if they want to play again
step 14. if no, quit
step 15. if yes, clear board 
'''
import random


def display_board(board):
    print("  1   2   3")    
    print("""1

             2

             3   """)
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ") 
        if i < 2:
            print("---+---+---")

def has_won(board, player):
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

def is_draw(board):
    count = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                count += 1
    
    if count == 0 and check_winner(board) is None:
        return True
    else:
        return False

def check_winner(board):                          
    if has_won(board, "X"):                       
        return "X"
    if has_won(board, "O"):                       
        return "O"
    return None        

          
def first_player():
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
    again = input("Do you want to play again (Yes/No)?: ").upper().strip()
    if again == "YES":
        play_game()
    if again == "NO":
        quit 
    else: 
        print("Please enter either Y or N")
        play_again()
    
def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    first, second = first_player()
    print(first, "goes first, then", second)

    while True:
        first_mark = input(first + ", do you want X or O? ").strip().upper()
        if first_mark == "X" or first_mark == "O":
            break
        print("Please type X or O.")

    if first_mark == "X":
        second_mark = "O"
    else:
        second_mark = "X"

    players = {first_mark: first, second_mark: second}
    current = first_mark  

    while True:
        display_board(board)
        print(players[current] + "'s turn (" + current + ")")
        row, col = get_player_move(board, current)
        board[row][col] = current

        winner = check_winner(board)
        if winner is not None:
            display_board(board)
            print(players[winner], "wins!")
            play_again()
            

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            play_again()

        if current == "X":
            current = "O"
        else:
            current = "X"

if __name__ == "__main__":
    play_game()
	display_board(board)

	
main()
