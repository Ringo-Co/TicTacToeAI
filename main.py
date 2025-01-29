###############################################################################
# Title: TicTacToeAI
# Version: 1.0
# Date: January 28th 2024
###############################################################################
# Imports and Global Variables ------------------------------------------------
import random
import tabulate
board = [['1', '2', '3'], 
         ['4', '5', '6'], 
         ['7', '8', '9']]

def main():
    print(tabulate(board,
                   tablefmt="rounded_grid",
                   stralign='center',
                   rowalign='center'))


# Main ------------------------------------------------------------------------
main()