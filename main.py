from board import bp
from config import global_arr, user_location,bomb_location
from player import player
from villian import villian
from input import villian_input, brick_input, user_position, key_position,bomb_input

def put_bomb():
    bomb_location[0] = user_location[0]
    bomb_location[1] = user_location[1]

def detonote_bomb():
    for i in range(bp.row):
        for j in range(bp.col):
            if(global_arr[i][j] == 'X '):
                global_arr[i][j] = '  '
    if(bomb_location[0] and bomb_location[1]):
        if(global_arr[bomb_location[0]-1][bomb_location[1]]=='P ' or global_arr[bomb_location[0]+1][bomb_location[1]]=='P ' or global_arr[bomb_location[0]][bomb_location[1]-1]=='P ' or global_arr[bomb_location[0]][bomb_location[1]+1]=='P '):
            print("Bom blast! You lost the game...")
            exit(1)
        if(global_arr[bomb_location[0]-1][bomb_location[1]]!='* ' and global_arr[bomb_location[0]-1][bomb_location[1]]!='K '):
            global_arr[bomb_location[0]-1][bomb_location[1]] = '  '
        if(global_arr[bomb_location[0]+1][bomb_location[1]]!='* ' and global_arr[bomb_location[0]+1][bomb_location[1]]!='K '):
            global_arr[bomb_location[0]+1][bomb_location[1]] = '  '
        if(global_arr[bomb_location[0]][bomb_location[1]-1]!='* ' and global_arr[bomb_location[0]][bomb_location[1]-1]!='K '):
            global_arr[bomb_location[0]][bomb_location[1]-1] = '  '
        if(global_arr[bomb_location[0]][bomb_location[1]+1]!='* ' and global_arr[bomb_location[0]][bomb_location[1]+1]!='K '):
            global_arr[bomb_location[0]][bomb_location[1]+1] = '  '
        global_arr[bomb_location[0]][bomb_location[1]] = '  '
        bomb_location[0] = 0
        bomb_location[1] = 0


bp.make_board()
user_position()
key_position()
villian_input()
brick_input()
bomb_input()
bp.display_board()


while(1):
    print("\nW - Move up\nS - Move down\nA - Move left\nD - Move right\nQ - Move diagonally up left\nZ - Move diagonally down left\nE - Move diagonally up right\nC - Move diagonally down right\nX - Bomb\nM - Exit\n")

    move = input("Enter your move: ")
    if(move == 'W' or move == 'w'):
        player.moveUp(user_location[0], user_location[1])
    elif(move == 'S' or move == 's'):
        player.moveDown(user_location[0], user_location[1])
    elif(move == 'A' or move == 'a'):
        player.moveLeft(user_location[0], user_location[1])
    elif(move == 'D' or move == 'd'):
        player.moveRight(user_location[0], user_location[1])
    elif(move == 'Q' or move == 'q'):
        player.moveUpLeft(user_location[0], user_location[1])
    elif(move == 'E' or move == 'e'):
        player.moveUpRight(user_location[0], user_location[1])
    elif(move == 'Z' or move == 'z'):
        player.moveDownLeft(user_location[0], user_location[1])
    elif(move == 'C' or move == 'c'):
        player.moveDownRight(user_location[0], user_location[1])
    elif(move == 'X' or move == 'x'):
        print("\n1 Plant\n2 Detonate")
        bomb = input("Enter your choice: ")
        if(bomb == '1'):
            put_bomb()
        elif(bomb == '2'):
            detonote_bomb()
        else:
            print("Invalid input")

    elif(move == 'M' or move == 'm'):
        print("Exiting...")
        break
    else:
        print("Invalid move")
    bp.display_board()

