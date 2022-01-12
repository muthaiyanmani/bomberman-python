from config import global_arr

class Villian:
    def set_pos(self,x,y):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = 'V '
        else:
            print("Already occupied")
    
    def get_pos(self,x,y):
        return global_arr[x,y]

villian = Villian()