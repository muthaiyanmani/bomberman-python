from config import global_arr

class Bricks():
    def set_pos(self,x,y):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = 'B '
        else:
            print("Already occupied")
    
    def get_pos(self,x,y):
        return global_arr[x,y]

bricks = Bricks()