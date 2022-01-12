from config import global_arr

class Key:
    def set_pos(self,x,y):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = 'K '
        else:
            print("Already occupied")
            exit(1)
    
    def get_pos(self,x,y):
        return global_arr[x,y]

key = Key()