"""
Author: Chad Bell
Assignment: Week 01 Prove
1/12/21
"""

def main():
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
        if board[0:3]==board[0:3][::-1]:
            is_finished = True
        elif board[3:6]==board[3:6][::-1]:
            is_finished = True
        elif board[6:9]==board[6:9][::-1]:
            is_finished = True
        elif board[0]==board[3]==board[6]:
            is_finished = True
        elif board[1]==board[4]==board[7]:
            is_finished = True
        elif board[2]==board[5]==board[8]:
            is_finished = True
        elif board[0]==board[4]==board[8]:
            is_finished = True
        elif board[2]==board[4]==board[6]:
            is_finished = True
        else:
            next
    print(f"You Won!")
            

def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def user_move():
    return int(input("Where would you like to move?: "))


if __name__== '__main__':
    main()