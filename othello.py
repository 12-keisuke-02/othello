class Othello():
    board = [[i for i in range(10)] for j in range(10)]
    black = 1
    white = 2

    count_black = 2
    count_white = 2
    square = []
    def __init__(self):
        self.now_player = 1
        self.next_player = 2
        self.turn = 1
        for i in range(10):
            for j in range(10):
                self.board[i][j] = -1

        for i in range(1,9):
            for j in range(1, 9):
                self.board[i][j] = 0

        self.board[4][4] = 1
        self.board[5][5] = 1
        self.board[4][5] = 2
        self.board[5][4] = 2
        self.printboard()
    
    def printboard(self):
        for i in range(1, 9):
            for j in range(1, 9):
                print(self.board[i][j], end='')
            print()

    def turnchange(self):
        swap = self.next_player
        self.next_player = self.now_player
        self.now_player = swap

    def put(self, p, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i==0 and j==0: continue
                c = self.turnover_num(p, x, y, i, j)
                for put in range(1, c):
                    self.board[y+put*j][x+put*i] = p
        
        self.board[y][x] = p

    def turnover_num(self, p, x, y, dir_x, dir_y):
        i = 1
        while(self.board[y+i*dir_y][x+i*dir_x]==3-p):
            i += 1
        if (self.board[y+i*dir_y][x+i*dir_x]==p):
            return i
        else :
            return 0
        

    def canput(self, p, x, y):
        if (x < 1 or x > 8 or y < 1 or y > 8):
            return 0
        if (self.board[y][x]!=0):
            return 0
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i==0 and j==0):
                    continue
                if (self.turnover_num(p, x, y, i, j)>1):
                    return 1
        return 0
    
    def research(self, p):
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.canput(p, i, j)==1):
                    self.square.append(i)
                    self.square.append(j)

        if len(self.square)>1:
            return 1
        
        return 0
    
    def delete_list(self):
        self.square = []

    def count_turn(self):
        self.turn += 1




        
def main():
    game = Othello()
    game.count_turn()
    game.turnchange()
    game.research(game.now_player)
    game.canput(game.now_player, 4, 6)
    game.put(game.now_player, 4, 6)

main()