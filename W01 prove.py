"""
Author: Chad Bell
Assignment: Week 01 Prove
1/12/21
"""
 
# Main code. 
def main():
    # Initializes the board. 
    global board
    board = [i for i in range(1, 10)]
    print("\n\n\nIt's player X's turn")
    print_board(board)

    # Tells when the game is finished
    is_finished = False
    turn = "X"
    while is_finished == False:
        # Player X's turn
        if turn == "X":
            board[user_move()-1] = "X"
            print("\n\n\nIt's player O's turn")
            turn = "0"
        # Player O's turn
        else:
            board[user_move()-1] = "O"
            print("\n\n\nIt's player X's turn")
            turn = "X"

        # Prints the board
        print_board(board)

        # Cases for 3 in a row. 
        if board[0]==board[1]==board[2]:
            is_finished = True
            print(f"You Won!")
        elif board[3]==board[4]==board[5]:
            is_finished = True
            print(f"You Won!")
        elif board[6]==board[7]==board[8]:
            is_finished = True
            print(f"You Won!")
        elif board[0]==board[3]==board[6]:
            is_finished = True
            print(f"You Won!")
        elif board[1]==board[4]==board[7]:
            is_finished = True
            print(f"You Won!")
        elif board[2]==board[5]==board[8]:
            is_finished = True
            print(f"You Won!")
        elif board[0]==board[4]==board[8]:
            is_finished = True
            print(f"You Won!")
        elif board[2]==board[4]==board[6]:
            is_finished = True
            print(f"You Won!")
        # If there are no numbers left on the board it is a cat's game. 
        elif len([i for i in board if isinstance(i, int)])==0:
            print("Cat's Game!")
            is_finished = True
        else:
            next
    
            
# Prints the board. 
def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

# Asks the user for their move. 
def user_move():
    while True:
        # Only returns the move if the spot has not been taken. 
        try:
            move = int(input("Where would you like to move?: "))
            if move in range(1, 10) and isinstance(board[move-1], int):
                return move
            else:
                print("That is not a valid input. please try again")
        except:
            print("that is not a valid input. please try again")


if __name__== '__main__':
    main()