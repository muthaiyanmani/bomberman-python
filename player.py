from config import global_arr,user_location

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

player = Player()