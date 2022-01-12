
from villian import villian
from bricks import bricks
from player import player
from key import key
from config import user_location

def map_size():
    temp = int(input("Enter the size of the board: ")) 
    if(temp>=5 and temp<=26 and temp%2==0):
        return temp
    else:
        print("Invalid input! game exiting...")


def user_position():
    temp = input("Enter player position: ")
    user_location.append(ord(temp[0]) - ord('A')+1) 
    user_location.append(ord(temp[1]) - ord('A')+1  )     
    player.set_pos(user_location[0], user_location[1])

def key_position():
    temp = input("Enter key position: ")
    row = ord(temp[0]) - ord('A')+1
    col = ord(temp[1]) - ord('A')+1       
    key.set_pos(row, col)

def villian_input():
    villian_pos=[]
    nos = int(input("Enter the number of villains: "))
    for i in range(nos):
       temp = input("Enter V{v} position: ".format(v=i+1))
       row = ord(temp[0]) - ord('A')+1
       col = ord(temp[1]) - ord('A')+1       
       villian.set_pos(row, col)
    

def brick_input():
    brick_pos=[]
    nos = int(input("Enter the number of bricks: "))
    for i in range(nos):
       temp = input("Enter B{v} position: ".format(v=i+1))
       row = ord(temp[0]) - ord('A')+1
       col = ord(temp[1]) - ord('A')+1       
       bricks.set_pos(row, col)
