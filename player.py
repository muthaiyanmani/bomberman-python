from config import global_arr,user_location,bomb_location

class Player:

    def set_pos(self,x,y):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = 'P '
        else:
            print("Already occupied")
    
    def get_pos(self,x,y):
        return global_arr[x,y]

    def moveUp(self,x,y):
        if(global_arr[x-1][y] == '  '):
            global_arr[x][y] = '  '
            global_arr[x-1][y] = 'P '
            user_location[0] = x-1
            user_location[1] = y
        
        elif( global_arr[x-1][y] == 'V '):
            print("You lost the game...")
            exit(1)
        elif(global_arr[x-1][y] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '
        
    def moveDown(self,x,y):
        if(global_arr[x+1][y] == '  '):
            global_arr[x][y] = '  '
            global_arr[x+1][y] = 'P '
            user_location[0] = x+1
            user_location[1] = y
          
        elif( global_arr[x+1][y] == 'V '):
           print("You lost the game...")
           exit(1)
        elif(global_arr[x+1][y] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied.")

        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveLeft(self,x,y):
        if(global_arr[x][y-1] == '  '):
            global_arr[x][y] = '  '
            global_arr[x][y-1] = 'P '
            user_location[0] = x
            user_location[1] = y-1
          
        elif( global_arr[x][y-1] == 'V '):
            print("You lost the game...")
            exit(1)
        elif(global_arr[x][y-1] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveRight(self,x,y):
        if(global_arr[x][y+1] == '  '):
            global_arr[x][y] = '  '
            global_arr[x][y+1] = 'P '
            user_location[0] = x
            user_location[1] = y+1
          
        elif( global_arr[x][y+1] == 'V '):
           print("You lost the game...")
           exit(1)
        elif(global_arr[x][y+1] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveUpLeft(self,x,y):
        if(global_arr[x-1][y-1] == '  '):
            global_arr[x][y] = '  '
            global_arr[x-1][y-1] = 'P '
            user_location[0] = x-1
            user_location[1] = y-1
           
        elif( global_arr[x-1][y-1] == 'V '):
           print("You lost the game...")
           exit(1)
        elif(global_arr[x-1][y-1] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveUpRight(self,x,y):
        if(global_arr[x-1][y+1] == '  '):
            global_arr[x][y] = '  '
            global_arr[x-1][y+1] = 'P '
            user_location[0] = x-1
            user_location[1] = y+1
          
        elif( global_arr[x-1][y+1] == 'V '):
           print("You lost the game...")
           exit(1)
        elif(global_arr[x-1][y+1] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '
    
    def moveDownLeft(self,x,y):
        if(global_arr[x+1][y-1] == '  '):
            global_arr[x][y] = '  '
            global_arr[x+1][y-1] = 'P '
            user_location[0] = x+1
            user_location[1] = y-1
          
        elif( global_arr[x+1][y-1] == 'V '):
           print("You lost the game...")
           exit(1)
        elif(global_arr[x+1][y-1] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

    def moveDownRight(self,x,y):
        if(global_arr[x+1][y+1] == '  '):
            global_arr[x][y] = '  '
            global_arr[x+1][y+1] = 'P '
            user_location[0] = x+1
            user_location[1] = y+1
        
        elif( global_arr[x+1][y+1] == 'V '):
           print("You lost the game...")
           exit(1)
        elif(global_arr[x+1][y+1] == 'K '):
            print("You won the game!")
            exit(1)
        else:
            print("Already occupied")
        if(bomb_location[0] and bomb_location[1]):
            global_arr[bomb_location[0]][bomb_location[1]] = 'X '

player = Player()