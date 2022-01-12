from config import global_arr

class Villian:
    def set_pos(self,x,y):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = 'V '
        else:
            print("Already occupied")
            print("Exiting...")
            exit(1)

villian = Villian()