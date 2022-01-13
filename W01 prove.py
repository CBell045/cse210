"""
Author: Chad Bell
Assignment: Week 01 Prove
1/12/21
"""
# Just add comments and turn in. 
def main():
    # Initializes the board. 
    global board
    board = [i for i in range(1, 10)]
    print("\n\n\nIt's player X's turn")
    print_board(board)
    is_finished = False
    turn = "X"
    while is_finished == False:
        if turn == "X":
            board[user_move()-1] = "X"
            print("\n\n\nIt's player O's turn")
            turn = "0"
        else:
            board[user_move()-1] = "O"
            print("\n\n\nIt's player X's turn")
            turn = "X"
        print_board(board)
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
        elif len([i for i in board if isinstance(i, int)])==0:
            print("Cat's Game!")
            is_finished = True
        else:
            next
    
            

def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def user_move():
    while True:
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