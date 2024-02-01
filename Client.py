import tkinter as tk
import tkinter.ttk as ttk
import sys
import othello
import threading

class Client():
    
    def __init__(self, game:othello.Othello):
        self.copy1 = [[i for i in range(10)] for j in range(10)]
        self.copy2 = [[i for i in range(10)] for j in range(10)]
        self.copy3 = [[i for i in range(10)] for j in range(10)]
        self.copy4 = [[i for i in range(10)] for j in range(10)]
        self.x = 0
        self.y = 0
        self.flag = 0
        self.computer_wait = 0
        self.game = game
        self.player = 1
        self.root = tk.Tk()
        self.root.title("reversi game")
        self.root.geometry("1000x800")
        self.start_x = tk.StringVar()
        self.start_y = tk.StringVar()
        self.gameboard = tk.Canvas(self.root, width=720, height=720)
        self.gameboard.create_rectangle(0, 0 , 720, 720, fill = 'green')
        self.gameboard.place(x=140, y=40)
        self.gameboard.create_line(0, 0, 720, 0)
        self.gameboard.create_line(0, 90, 720, 90)
        self.gameboard.create_line(0, 180, 720, 180)
        self.gameboard.create_line(0, 270, 720, 270)
        self.gameboard.create_line(0, 360, 720, 360)
        self.gameboard.create_line(0, 450, 720, 450)
        self.gameboard.create_line(0, 540, 720, 540)
        self.gameboard.create_line(0, 630, 720, 630)
        self.gameboard.create_line(0, 720, 720, 720)
        self.gameboard.create_line(0, 0, 0, 720)
        self.gameboard.create_line(90, 0, 90, 720)
        self.gameboard.create_line(180, 0, 180, 720)
        self.gameboard.create_line(270, 0, 270, 720)
        self.gameboard.create_line(360, 0, 360, 720)
        self.gameboard.create_line(450, 0, 450, 720)
        self.gameboard.create_line(540, 0, 540, 720)
        self.gameboard.create_line(630, 0, 630, 720)
        self.gameboard.create_line(720, 0, 720, 720)
        self.gameboard.create_oval(280, 280, 350, 350, fill="black", tags = 'oval')
        self.gameboard.create_oval(370, 370, 440, 440, fill="black", tags = 'oval')
        self.gameboard.create_oval(280, 370, 350, 440, fill="white", tags = 'oval')
        self.gameboard.create_oval(370, 280, 440, 350, fill="white", tags = 'oval')
        self.gameboard.bind('<ButtonPress-1>', self.start_pickup)

        thread1 = threading.Thread(target=self.gamestart)
        thread2 = threading.Thread(target=self.computer)
        thread1.start()
        thread2.start()
        self.root.mainloop()
        thread1.join()
        thread2.join()

    def boardview(self):
        self.gameboard.create_rectangle(0, 0 , 720, 720, fill = 'green')
        self.gameboard.create_line(0, 0, 720, 0)
        self.gameboard.create_line(0, 90, 720, 90)
        self.gameboard.create_line(0, 180, 720, 180)
        self.gameboard.create_line(0, 270, 720, 270)
        self.gameboard.create_line(0, 360, 720, 360)
        self.gameboard.create_line(0, 450, 720, 450)
        self.gameboard.create_line(0, 540, 720, 540)
        self.gameboard.create_line(0, 630, 720, 630)
        self.gameboard.create_line(0, 720, 720, 720)
        self.gameboard.create_line(0, 0, 0, 720)
        self.gameboard.create_line(90, 0, 90, 720)
        self.gameboard.create_line(180, 0, 180, 720)
        self.gameboard.create_line(270, 0, 270, 720)
        self.gameboard.create_line(360, 0, 360, 720)
        self.gameboard.create_line(450, 0, 450, 720)
        self.gameboard.create_line(540, 0, 540, 720)
        self.gameboard.create_line(630, 0, 630, 720)
        self.gameboard.create_line(720, 0, 720, 720)


    def gamepanel(self):
        root = tk.Tk()
        root.title("reversi game")
        root.geometry("1000x800")

    def panelrenew(self):
        self.gameboard.delete('oval')
        for i in range(1,9):
            for j in range(1, 9):
                if (self.game.board[i][j]==1):
                    self.gameboard.create_oval((j-1)*90+10, (i-1)*90+10, j*90-10, i*90-10, fill="black", tags='oval')
                elif (self.game.board[i][j]==2):
                    self.gameboard.create_oval((j-1)*90+10, (i-1)*90+10, j*90-10, i*90-10, fill="white", tags = 'oval')

    def putpoint(self):
        for i in range(0, len(self.game.square), 2):
            self.gameboard.create_oval((self.game.square[i]-1)*90+30, (self.game.square[i+1]-1)*90+30, self.game.square[i]*90-30, self.game.square[i+1]*90-30, fill="red", tags='oval')
        self.game.delete_list()

    def gamestart(self):
        self.game.delete_list()
        while True:
            while self.computer_wait==1:
                b = 3
            self.game.count_turn()
            print("my turn")
            if (self.game.research(self.game.now_player)==0):
                self.game.turnchange()
                if (self.game.research(self.game.now_player)==0):
                    break
            self.putpoint()
            x = 0
            y = 0
            while (self.flag == 0):
                t = 4
            
            self.flag = 0
            self.game.put(self.game.now_player, self.x, self.y)
            self.panelrenew()
            self.game.turnchange()
            self.game.printboard()
            self.computer_wait = 1
            print("finish my turn")
            if (self.game.turn >= 60):
                break
            

    def computer(self):
        while True:
            while self.computer_wait == 0:
                a = 3
            self.game.count_turn()
            print("start computer turn")
            min = 100
            max = 0
            self.copy()
            print("computers_turn")
            for i in range(1, 9):
                for j in range(1, 9):
                    c = 0
                    if (self.game.board[i][j]==0):
                        for k in range(-1, 2):
                            for t in range(-1, 2):
                                if k!=0 or t!=0:
                                    c += self.game.turnover_num(self.game.now_player, j, i, k, t)
                        if c > max:
                            max = c
                            y = i
                            x = j
            print(max, x, y)
            if (max > 0): self.game.put(self.game.now_player, x, y)
            self.panelrenew()
            self.game.turnchange()
            self.game.printboard()
            self.computer_wait = 0
            print("finish computer turn")
        



    def copy(self):
        for i in range(1, 9):
            for j in range(1, 9):
                self.copy1[i][j] = self.game.board[i][j]





    def start_pickup(self, event):
        self.start_x.set('x : ' + str(event.x))
        self.start_y.set('y : ' + str(event.y))
        self.x = int(event.x / 90) + 1
        self.y = int(event.y / 90) + 1
        self.flag = 1




def main():
    game = othello.Othello()
    client = Client(game)

main()