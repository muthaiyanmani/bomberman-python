from config import global_arr

class Bomb():
    def set_pos(self,x,y,count):
        if(global_arr[x][y] == '  '):
            global_arr[x][y] = str(count)+" "
        else:
            print("Already occupied")
            print("Exiting...")
            exit(1)
    
    def get_pos(self,x,y):
        return global_arr[x,y]

bomb = Bomb()