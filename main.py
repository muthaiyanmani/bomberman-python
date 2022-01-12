from board import bp
from config import global_arr, user_location
from player import player
from villian import villian
from input import villian_input, brick_input, user_position, key_position


def display_board():
    for x in range(bp.row):
        for y in range(bp.col):
            print(global_arr[x][y], end="")
        print()
    print()

bp.make_board()
user_position()
key_position()
villian_input()
brick_input()
display_board()


while(1):
    print("\nW - Move up\nS - Move down\nA - Move left\nD - Move right\nQ - Move diagonally up left\nZ - Move diagonally down left\nE - Move diagonally up right\nC - Move diagonally down right\nX - Exit\n")

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
        print("Exiting...")
        break
    else:
        print("Invalid move")
    display_board()
