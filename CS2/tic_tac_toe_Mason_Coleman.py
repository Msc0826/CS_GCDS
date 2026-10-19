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
    return None

def is_draw(board):
    count = 0 
    for row in board: 
        for cell in row:  
            if cell == " ":
                count += 1
    
    if count == 9 and has_won(board) is None:
        return True
    else:
        False 



          
def first_player():
    player_1 = input("What is your name player 1: ").strip()
    player_2 = input("What is your name player 2: ").strip()
    names = (player_1, player_2)
    random.choice(names)


def main():
	board = [
			 [" "," "," "],
	         [" "," "," "],
	         [" "," "," "]
	]
	display_board(board)

	
main()