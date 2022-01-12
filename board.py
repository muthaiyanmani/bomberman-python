from config import global_arr
from input import map_size

class Board:
    global_arr=[]
    def __init__(self, size):
        self.row = size
        self.col = size

    def make_board(self):
        # board layout
        for x in range(self.row):
            global_arr.append([])
            for y in range(self.col):
                global_arr[x].append(' ')
        for x in range(0,1):
            for y in range(self.col):
                global_arr[x][y] = chr(ord('A')+(y-1))+" "
        
        global_arr[0][0] = '  '

        for x in range(1,2):
            for y in range(self.col):
                if(y==0):
                    global_arr[x][y] = chr(ord('A')+(x-1))+" "
                else:
                    global_arr[x][y] ="* "

        for x in range(2,self.row-1):
            for y in range(self.col):
                if(y==0):
                    global_arr[x][y] = chr(ord('A')+(x-1))+" "
                elif(y==1 or y==self.col-1):
                    global_arr[x][y] ="* "
                else:
                    global_arr[x][y] ="  "
        for x in range(self.row-1,self.row):
          for y in range(self.col):
              if(y==0):
                  global_arr[x][y] = chr(ord('A')+(x-1))+" "
              else:
                  global_arr[x][y] ="* "
        
        # fixed walls inside board
        for x in range(3,self.row-2):
            for y in range(3,self.col-2):
                if(x%2!=0 and y%2!=0):
                    global_arr[x][y] = "* "

    
    def set_pos(self, x,y, val):
        global_arr[x][y] = val

bp = Board(map_size())
