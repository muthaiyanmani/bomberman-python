from config import global_arr,user_location,bomb_location

class Player:

    def set_pos(self,x,y):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = 'P '
        else:
            print("Already occupied")

    def moveUp(self,x,y):
        if(global_arr[x-1][y] == '  ' or  global_arr[x-1][y] == '1 ' or global_arr[x-1][y] == '2 ' or global_arr[x-1][y] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x-1][y] = 'P '
            user_location[0] = x-1
            user_location[1] = y      
        elif( global_arr[x-1][y] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x-1][y] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x-1][y] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x-1][y] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("\nAlready occupied\n")

        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '
        
    def moveDown(self,x,y):
        if(global_arr[x+1][y] == '  ' or global_arr[x+1][y] == '1 ' or global_arr[x+1][y] == '2 ' or global_arr[x+1][y] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x+1][y] = 'P '
            user_location[0] = x+1
            user_location[1] = y
        elif( global_arr[x+1][y] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x+1][y] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x+1][y] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x+1][y] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("\nAlready occupied.\n")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveLeft(self,x,y):
        if(global_arr[x][y-1] == '  ' or global_arr[x][y-1] == '1 ' or global_arr[x][y-1] == '2 ' or global_arr[x][y-1] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x][y-1] = 'P '
            user_location[0] = x
            user_location[1] = y-1
          
        elif( global_arr[x][y-1] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x][y-1] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x][y-1] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x][y-1] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("\nAlready occupied\n")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveRight(self,x,y):
        if(global_arr[x][y+1] == '  ' or global_arr[x][y+1] == '1 ' or global_arr[x][y+1] == '2 ' or global_arr[x][y+1] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x][y+1] = 'P '
            user_location[0] = x
            user_location[1] = y+1
          
        elif( global_arr[x][y+1] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x][y+1] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x][y+1] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x][y+1] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("\nAlready occupied\n")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveUpLeft(self,x,y):
        if(global_arr[x-1][y-1] == '  ' or global_arr[x-1][y-1] == '1 ' or global_arr[x-1][y-1] == '2 ' or global_arr[x-1][y-1] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x-1][y-1] = 'P '
            user_location[0] = x-1
            user_location[1] = y-1
           
        elif( global_arr[x-1][y-1] == 'V '):
           global_arr[x][y] = '  '
           global_arr[x-1][y-1] = 'P '
           print("You lost the game...")
           exit(1)
        elif(global_arr[x-1][y-1] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x-1][y-1] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("\nAlready occupied\n")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveUpRight(self,x,y):
        if(global_arr[x-1][y+1] == '  ' or global_arr[x-1][y+1] == '1 ' or global_arr[x-1][y+1] == '2 ' or global_arr[x-1][y+1] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x-1][y+1] = 'P '
            user_location[0] = x-1
            user_location[1] = y+1
          
        elif( global_arr[x-1][y+1] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x-1][y+1] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x-1][y+1] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x-1][y+1] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("\nAlready occupied\n")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '
    
    def moveDownLeft(self,x,y):
        if(global_arr[x+1][y-1] == '  ' or global_arr[x+1][y-1] == '1 ' or global_arr[x+1][y-1] == '2 ' or global_arr[x+1][y-1] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x+1][y-1] = 'P '
            user_location[0] = x+1
            user_location[1] = y-1
          
        elif( global_arr[x+1][y-1] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x+1][y-1] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x+1][y-1] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x+1][y-1] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveDownRight(self,x,y):
        if(global_arr[x+1][y+1] == '  ' or global_arr[x+1][y+1] == '1 ' or global_arr[x+1][y+1] == '2 ' or global_arr[x+1][y+1] == '3 '):
            global_arr[x][y] = '  '
            global_arr[x+1][y+1] = 'P '
            user_location[0] = x+1
            user_location[1] = y+1
        
        elif( global_arr[x+1][y+1] == 'V '):
            global_arr[x][y] = '  '
            global_arr[x+1][y+1] = 'P '
            print("You lost the game...")
            exit(1)
        elif(global_arr[x+1][y+1] == 'K '):
            global_arr[x][y] = '  '
            global_arr[x+1][y+1] = 'P '
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

player = Player()