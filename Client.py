import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import sys
import othello
import threading
import time

class Client():
    
    def __init__(self, game:othello.Othello):
        self.copy1 = [[i for i in range(10)] for j in range(10)]
        self.copy2 = [[i for i in range(10)] for j in range(10)]
        self.copy3 = [[i for i in range(10)] for j in range(10)]
        self.copy4 = [[i for i in range(10)] for j in range(10)]
        self.valuate = [[120, -20, 20, 5, 5, 20, -20, 120],
                        [-20, -40, -5, -5, -5, -5, -40, -20],
                        [20, -5, 15, 3, 3, 15, -5, 15, -20],
                        [5, -5, 3, 3, 3, 3, 15, -5, 5],
                        [5, -5, 3, 3, 3, 3, 15, -5, 5],
                        [20, -5, 15, 3, 3, 15, -5, 15, -20],
                        [-20, -40, -5, -5, -5, -5, -40, -20],
                        [120, -20, 20, 5, 5, 20, -20, 120]]
        self.x = 0
        self.y = 0
        self.flag = 0
        self.pass_conti = 0
        self.count = 2
        self.computer_wait = 0
        self.game = game
        self.player = 1
        self.root = tk.Tk()
        self.root.title("reversi game")
        self.root.geometry("1000x900")
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
        self.gameboard.create_oval(280, 280, 350, 350, fill="black", tags = 'oval44')
        self.gameboard.create_oval(370, 370, 440, 440, fill="black", tags = 'oval55')
        self.gameboard.create_oval(280, 370, 350, 440, fill="white", tags = 'oval45')
        self.gameboard.create_oval(370, 280, 440, 350, fill="white", tags = 'oval54')
        self.label1 = Label(self.root, text="あなたの石の数：2", font=("times, 16"))
        self.label1.place(x=400, y=780)
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
        
    def panelrenew(self, now_player):
        if now_player == 1:
            for i in range(0, len(self.game.variation), 2):
                print(self.game.variation[i], self.game.variation[i+1])
                self.gameboard.delete("oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
                self.gameboard.create_oval((self.game.variation[i]-1)*90+10, (self.game.variation[i+1]-1)*90+10, self.game.variation[i]*90-10, self.game.variation[i+1]*90-10, fill="black", tags = "oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
        
        elif now_player == 2:
            for i in range(0, len(self.game.variation), 2):
                print(self.game.variation[i], self.game.variation[i+1])
                self.gameboard.delete("oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
                self.gameboard.create_oval((self.game.variation[i]-1)*90+10, (self.game.variation[i+1]-1)*90+10, self.game.variation[i]*90-10, self.game.variation[i+1]*90-10, fill="white", tags = "oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
        
        self.game.delete_var()
                        

                
                

    def putpoint(self):
        for i in range(0, len(self.game.square), 2):
            print("unko: " ,self.game.square[i], self.game.square[i+1])
            self.gameboard.create_oval((self.game.square[i]-1)*90+30, (self.game.square[i+1]-1)*90+30, self.game.square[i]*90-30, self.game.square[i+1]*90-30, fill="red", tags='ovalred')
        self.game.delete_list()

    def gamestart(self):
        self.game.delete_list()
        self.game.delete_var()
        sign = 0
        while True:
            while self.computer_wait==1:
                if self.game.turn >= 60:
                    sign = 1
                    break
                b = 3
            if sign == 1:
                break
            self.game.count_turn()
            print("my turn")
            if (self.game.research(self.game.now_player)==0):
                self.game.turnchange()
                self.pass_conti += 1
                print("pass my turn")
                if (self.pass_conti==1):
                    self.computer_wait = 1
                    continue
                else:
                    break
            self.pass_conti = 0
            self.putpoint()
            x = 0
            y = 0
            while (self.flag == 0):
                t = 4
            flag=0
            while flag==0:
                flag = self.game.canput(self.game.now_player, self.x, self.y)

            self.flag = 0
            self.game.put(self.game.now_player, self.x, self.y)
            self.count = self.game.count_stone(self.game.now_player)
            self.label1.place_forget()
            self.label1 = Label(self.root, text="あなたの石の数："+str(self.count), font=("times, 16"))
            self.label1.place(x=400, y=780)
            self.gameboard.delete("ovalred")
            self.panelrenew(self.game.now_player)
            self.game.turnchange()
            self.game.printboard()
            self.computer_wait = 1
            print("finish my turn")
        print("試合終了です")
            

    def computer(self):
        flag = 0
        while True:
            while self.computer_wait == 0:
                if self.game.turn >= 60:
                    flag = 1
                    break
                a = 3
            time.sleep(2)
            if (flag == 1):
                break
            self.game.count_turn()
            print("start computer turn")
            if (self.game.research(self.game.now_player)==0):
                self.game.delete_list()
                self.game.turnchange()
                self.pass_conti += 1
                print("pass computer turn")
                if (self.pass_conti == 1):
                    self.computer_wait = 0
                    continue
                else:
                    break
            self.game.delete_list()
            self.pass_conti = 0
            min = 100
            max = 0
            self.copyboard(self.copy1, self.game.board)
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
            self.panelrenew(self.game.now_player)
            self.game.turnchange()
            self.count = self.game.count_stone(self.game.now_player)
            self.label1 = Label(self.root, text="あなたの石の数："+str(self.count), font=("times, 16"))
            self.label1.place(x=400, y=780)
            self.game.printboard()
            self.computer_wait = 0
            print("finish computer turn")
        print("試合終了です")


    def alpha_beta(self, now_player, alpha, beta, depth):
        self.copyboard(self.copy1, self.game.board)

        


    def copyboard(self, copy, original):
        for i in range(1, 9):
            for j in range(1, 9):
                copy[i][j] = original[i][j]





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