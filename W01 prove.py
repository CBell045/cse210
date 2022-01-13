"""
Author: Chad Bell
Assignment: Week 01 Prove
1/12/21
"""

def main():
    board = [i for i in range(1, 10)]
    print_board(board)
    is_finished = False
    turn = "X"
    while is_finished == False:
        if turn == "X":
            board[user_move()-1] = "X"
        else:
            board[user_move()-1] = "O"
        print_board(board)
        print(board[3:0])
        if board[0:3]==board[0:3].reverse():
            is_finished == True
        elif board[3:6]==board[3:6].reverse():
            is_finished == True
        elif board[6:9]==board[6:9].reverse():
            is_finished == True
        elif board[0]==board[3]==board[6]:
            is_finished == True
        elif board[1]==board[4]==board[7]:
            is_finished == True
        elif board[2]==board[5]==board[8]:
            is_finished == True
        elif board[0]==board[4]==board[8]:
            is_finished == True
        elif board[2]==board[4]==board[6]:
            is_finished == True
        else:
            next
            

def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def user_move():
    return int(input("Where would you like to move?: "))


if __name__== '__main__':
    main()