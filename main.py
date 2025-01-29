###############################################################################
# Title: TicTacToeAI
# Version: 1.0
# Date: January 28th 2025
###############################################################################
# Imports and Global Variables ------------------------------------------------
import random
from tabulate import tabulate
board = [['1', '2', '3'], 
         ['4', '5', '6'], 
         ['7', '8', '9']]
playing = True
player_letter = 'X'
ai_letter = 'O'


def print_board():
    print(tabulate(board,
                   tablefmt="rounded_grid",
                   stralign='center',
                   rowalign='center'))
    

def reset_board():
    global board
    board = [['1', '2', '3'], 
             ['4', '5', '6'], 
             ['7', '8', '9']]
    

def check_win(letter):
    ''' Checks if "letter" has won.'''
    for row in board:  # Horizontal
        if all(cell == letter for cell in row):
            print("Horizontal")
            return True
    for col in range(3):  # Vertical
        if all(board[row][col] == letter for row in range(3)):
            return True
        else:
            continue
    for col in range(3):  # Diagonal
        if all(board[i][i] == letter for i in range(3)):
            return True
        if all(board[i][2-i] == letter for i in range(3)):
            return True
        return False


def player_turn():
    while True:
        print_board()
        try:
            choice = int(input("Choose a space: ").strip())
        except ValueError:
            print("ERROR: Input was not a number.")
        else:
            if choice < 1 or choice > 9:
                print("ERROR: Invalid input.")
                continue
            row, col = divmod(choice - 1, 3)
            if board[row][col] not in [player_letter, ai_letter]:
                board[row][col] = player_letter
                break
            else:
                print("Spot already taken!")


def ai_turn():
    row_num = 0
    for row in board:
        space_num = 0
        for space in row:
            if space not in [player_letter, ai_letter]:
                board[row_num][space_num] = ai_letter
                return
            space_num += 1
        row_num += 1


def main():
    print(f"You are playing as {player_letter}.")
    while playing:
        player_turn()
        if check_win(player_letter):
            print("You won!")
            choice = input("Continue? (y/n) ")
            if 'y' in choice:
                reset_board()
                continue
            else:
                break
        ai_turn()
        if check_win(ai_letter):
            print("You lost!")
            choice = input("Continue? (y/n) ")
            if 'y' in choice:
                reset_board()
                continue
            else:
                break


# Main ------------------------------------------------------------------------
main()
