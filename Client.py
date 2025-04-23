import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
import othello
import threading
import time
import math

class Client():
    
    def __init__(self, game:othello.Othello):
        self.copy1 = [[i for i in range(10)] for j in range(10)]
        self.copy2 = [[i for i in range(10)] for j in range(10)]
        self.copy3 = [[i for i in range(10)] for j in range(10)]
        self.copy4 = [[i for i in range(10)] for j in range(10)]
        self.copy = [[[i for i in range(10)] for j in range(10)] for k in range(10)]
        self.squarecopies = [[] for _ in range(10)]
        self.squarecopy = []
        self.squarecopy2 = []
        self.squarecopy3 = []
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
        self.level = 0
        self.flag = 0
        self.pass_conti = 0
        self.count = 2
        self.computer_wait = 0
        self.game = game
        self.player = 1
        self.decision_level()
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

    def decision_level(self):
        global root
        root = tk.Tk()
        root.title("decide level")
        root.geometry("450x400")

        label1 = Label(root, text="レベルを選んでください", font=("times, 16"))
        button_level1 = tk.Button(root, text = "level1", font=("MSゴシック", "20"), command=self.btn_click1)
        button_level2 = tk.Button(root, text = "level2", font=("MSゴシック", "20"), command=self.btn_click2)
        button_level3 = tk.Button(root, text = "level3", font=("MSゴシック", "20"), command=self.btn_click3)
        button_level4 = tk.Button(root, text = "level4", font=("MSゴシック", "20"), command=self.btn_click4)
        button_level5 = tk.Button(root, text = "level5", font=("MSゴシック", "20"), command=self.btn_click5)
        label1.place(x=150, y=10)
        button_level1.place(x=200, y=80)
        button_level2.place(x=200, y=150)
        button_level3.place(x=200, y=220)
        button_level4.place(x=200, y=290)
        button_level5.place(x=200, y=360)
        root.mainloop()


    def btn_click1(self):
        self.level = 1
        root.destroy()
    
    def btn_click2(self):
        self.level = 2
        root.destroy()
    
    def btn_click3(self):
        self.level = 3
        root.destroy()
    
    def btn_click4(self):
        self.level = 4
        root.destroy()
    
    def btn_click5(self):
        self.level = 5
        root.destroy()
        
    def panelrenew(self, now_player):
        if now_player == 1:
            for i in range(0, len(self.game.variation), 2):
                self.gameboard.delete("oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
                self.gameboard.create_oval((self.game.variation[i]-1)*90+10, (self.game.variation[i+1]-1)*90+10, self.game.variation[i]*90-10, self.game.variation[i+1]*90-10, fill="black", tags = "oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
        
        elif now_player == 2:
            for i in range(0, len(self.game.variation), 2):
                self.gameboard.delete("oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
                self.gameboard.create_oval((self.game.variation[i]-1)*90+10, (self.game.variation[i+1]-1)*90+10, self.game.variation[i]*90-10, self.game.variation[i+1]*90-10, fill="white", tags = "oval"+str(self.game.variation[i])+str(self.game.variation[i+1]))
        
        self.game.delete_var()
                        

                
                

    def putpoint(self):
        for i in range(0, len(self.game.square), 2):
            self.gameboard.create_oval((self.game.square[i]-1)*90+30, (self.game.square[i+1]-1)*90+30, self.game.square[i]*90-30, self.game.square[i+1]*90-30, fill="red", tags='ovalred')
        self.game.delete_list()

    def gamestart(self):
        player = self.game.now_player
        self.game.delete_list()
        self.game.delete_var()
        sign = 0
        while True:
            while self.computer_wait==1:
                # if self.game.turn >= 60 or self.pass_conti == 2:
                if self.pass_conti == 2:
                    sign = 1
                    break
            if sign == 1:
                break
            
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
            self.game.count_turn()
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
        mystone = self.game.count_stone(player)
        enemy = self.game.count_stone(3-player)
        if mystone > enemy:
            messagebox.showinfo("勝敗", "あなたの勝ちです")
        elif mystone == enemy:
            messagebox.showinfo("勝敗", "引き分けです")
        else:
            messagebox.showinfo("勝敗", "あなたの負けです")
        print("試合終了です")
            

    

    def alpha_beta_level1(self, now_player):
        max = -10000
        for hand in range(0, len(self.game.square), 2):
                i = self.game.square[hand]
                j = self.game.square[hand+1]
                if max < self.valuate[j-1][i-1]:
                    x = i
                    y = j
                    max = self.valuate[j-1][i-1]
        self.game.put(now_player, x, y)

    def alpha_beta_level2(self, now_player, alpha: int, beta: int, depth: int):
        true_x = 0
        true_y = 0
        if (depth==2):
            self.copy1 = self.copyboard(self.copy1, self.game.board)
            self.game.delete_list()
            # 置けないとき0を返す
            if (self.game.research(now_player)==0):
                return alpha
            self.squarecopy = self.canput_copy(self.squarecopy, self.game.square)
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                self.game.put(now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta_level2(3-now_player, alpha=-beta, beta=-alpha, depth=depth-1)
                if hand == 0:
                    beta = score
                    true_x = x
                    true_y = y
                print(f"score = {score}, beta = {beta}")
                if (beta < score):
                    beta = score
                    true_x = x
                    true_y = y
                self.game.board = self.copyboard(self.game.board, self.copy1)
                self.game.square = self.canput_copy(self.game.square, self.squarecopy)
            self.game.put(now_player, true_x, true_y)


        elif (depth==1):
            #self.copyboard(self.copy2, self.game.board)
            self.game.delete_list()
            self.copy2 = self.copyboard(self.copy2, self.game.board)
            if (self.game.research(now_player)==0):
                return
            
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                self.game.put(now_player, x, y)
                score = self.calculate_score(now_player)
                print(f"depth = {depth}, score = {score}, alpha = {alpha}, x = {x}, y = {y}")
                if (score > alpha):
                    alpha = score
                self.game.board = self.copyboard(self.game.board, self.copy2)
                
                
            self.game.delete_list()
            self.game.delete_var()
            return alpha
        
        print(f"depth = {depth}, true_x={true_x}, true_y={true_y}")

    def alpha_beta_level3(self, now_player, alpha: int, beta: int, depth: int):
        true_x = 0
        true_y = 0
        if (depth==3):
            self.copy1 = self.copyboard(self.copy1, self.game.board)
            self.game.delete_list()
            # 置けないとき0を返す
            if (self.game.research(now_player)==0):
                return alpha
            self.squarecopy.clear()
            self.squarecopy = self.canput_copy(self.squarecopy, self.game.square)
            #print(f"depth = {depth}, square = {self.game.square}")
            for hand in range(0, len(self.game.square), 2):
                #print()
                #print(f"depth = {depth}, x = {self.game.square[hand]}, y = {self.game.square[hand+1]}")
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                self.game.put(now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta_level3(3-now_player, alpha=-beta, beta=-alpha, depth=depth-1)
                if hand == 0:
                    alpha = score
                    true_x = x
                    true_y = y
                #print(f"score = {score}, alpha = {alpha}")
                if (alpha < score):
                    alpha = score
                    true_x = x
                    true_y = y
                self.game.board = self.copyboard(self.game.board, self.copy1)
                self.game.square = self.canput_copy(self.game.square, self.squarecopy)
                #print(f"depth = {depth}, square = {self.game.square}")
            #print(f"depth = {depth}, true_x = {true_x}, true_y = {true_y}")
            self.game.put(now_player, true_x, true_y)

        elif (depth==2):
            kamen_x = 0
            kamen_y = 0
            self.copy2 = self.copyboard(self.copy2, self.game.board)
            self.game.delete_list()
            if (self.game.research(now_player)==0):
                self.game.delete_list()
                return alpha
            self.squarecopy2.clear()
            self.squarecopy2 = self.canput_copy(self.squarecopy2, self.game.square)
            #print(f"depth = {depth}, square = {self.game.square}")
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                #print(f"x = {x}, y = {y}")
                self.game.put(now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta_level3(3-now_player, alpha=-beta, beta=-alpha, depth=depth-1)
                #print(f"score = {score}, depth={depth}")
                if hand == 0:
                    alpha = score
                if (alpha < score):
                    alpha = score
                self.game.board = self.copyboard(self.game.board, self.copy2)
                self.game.square = self.canput_copy(self.game.square, self.squarecopy2)
                if alpha >= beta:
                    self.game.delete_list()
                    return alpha
            self.game.delete_list()
            self.squarecopy2.clear()
            return alpha


        elif (depth==1):
            #self.copyboard(self.copy2, self.game.board)
            self.game.delete_list()
            self.copy3 = self.copyboard(self.copy3, self.game.board)
            if (self.game.research(now_player)==0):
                self.game.delete_list()
                return alpha
            
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                self.game.put(now_player, x, y)
                score = self.calculate_score(now_player)
                #print(f"depth = {depth}, score = {score}, alpha = {alpha}, x = {x}, y = {y}")
                if hand==0:
                    alpha = score

                if (score > alpha):
                    alpha = score
                self.game.board = self.copyboard(self.game.board, self.copy3)
                
                
            self.game.delete_list()
            self.game.delete_var()
            return alpha
        
        print(f"depth = {depth}, true_x={true_x}, true_y={true_y}")
        
    def alpha_beta_level4(self, now_player, alpha:int, beta:int, depth:int):
        true_x = 0
        true_y = 0
        if (depth==4):
            self.copy1 = self.copyboard(self.copy1, self.game.board)
            self.game.delete_list()
            # 置けないとき0を返す
            if (self.game.research(now_player)==0):
                return alpha
            self.squarecopy.clear()
            self.squarecopy = self.canput_copy(self.squarecopy, self.game.square)
            #print(f"depth = {depth}, square = {self.game.square}")
            for hand in range(0, len(self.game.square), 2):
                #print()
                #print(f"depth = {depth}, x = {self.game.square[hand]}, y = {self.game.square[hand+1]}")
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                self.game.put(now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta_level4(3-now_player, alpha=-beta, beta=-alpha, depth=depth-1)
                if hand == 0:
                    alpha = score
                    true_x = x
                    true_y = y
                #print(f"score = {score}, alpha = {alpha}")
                if (alpha < score):
                    alpha = score
                    true_x = x
                    true_y = y
                self.game.board = self.copyboard(self.game.board, self.copy1)
                self.game.square = self.canput_copy(self.game.square, self.squarecopy)
                #print(f"depth = {depth}, square = {self.game.square}")
            #print(f"depth = {depth}, true_x = {true_x}, true_y = {true_y}")
            self.game.put(now_player, true_x, true_y)

        elif (depth==3):
            kamen_x = 0
            kamen_y = 0
            self.copy2 = self.copyboard(self.copy2, self.game.board)
            self.game.delete_list()
            if (self.game.research(now_player)==0):
                self.game.delete_list()
                return alpha
            self.squarecopy2.clear()
            self.squarecopy2 = self.canput_copy(self.squarecopy2, self.game.square)
            #print(f"depth = {depth}, square = {self.game.square}")
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                #print(f"x = {x}, y = {y}")
                self.game.put(now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta_level4(3-now_player, alpha=-beta, beta=-alpha, depth=depth-1)
                #print(f"score = {score}, depth={depth}")
                if hand == 0:
                    alpha = score
                    kamen_x = x
                    kamen_y = y
                if (alpha < score):
                    alpha = score
                    kamen_x = x
                    kamen_y = y
                self.game.board = self.copyboard(self.game.board, self.copy2)
                self.game.square = self.canput_copy(self.game.square, self.squarecopy2)
                if alpha >= beta:
                    self.game.delete_list()
                    return alpha
            self.game.delete_list()
            self.squarecopy2.clear()
            return alpha
        
        elif (depth==2):
            kamen_x = 0
            kamen_y = 0
            self.copy3 = self.copyboard(self.copy3, self.game.board)
            self.game.delete_list()
            if (self.game.research(now_player)==0):
                self.game.delete_list()
                return alpha
            self.squarecopy3.clear()
            self.squarecopy3 = self.canput_copy(self.squarecopy3, self.game.square)
            #print(f"depth = {depth}, square = {self.game.square}")
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                #print(f"x = {x}, y = {y}")
                self.game.put(now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta_level4(3-now_player, alpha=-beta, beta=-alpha, depth=depth-1)
                #print(f"score = {score}, depth={depth}")
                if hand == 0:
                    alpha = score
                    kamen_x = x
                    kamen_y = y
                if (alpha < score):
                    alpha = score
                    kamen_x = x
                    kamen_y = y
                self.game.board = self.copyboard(self.game.board, self.copy3)
                self.game.square = self.canput_copy(self.game.square, self.squarecopy3)
                if alpha >= beta:
                    self.game.delete_list()
                    return alpha
            self.game.delete_list()
            self.squarecopy3.clear()
            return alpha

        elif (depth==1):
            #self.copyboard(self.copy2, self.game.board)
            self.game.delete_list()
            self.copy4 = self.copyboard(self.copy4, self.game.board)
            if (self.game.research(now_player)==0):
                self.game.delete_list()
                return alpha
            
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
                self.game.put(now_player, x, y)
                score = self.calculate_score(now_player)
                #print(f"depth = {depth}, score = {score}, alpha = {alpha}, x = {x}, y = {y}")
                if hand==0:
                    alpha = score

                if (score > alpha):
                    alpha = score
                self.game.board = self.copyboard(self.game.board, self.copy4)
                
                
            self.game.delete_list()
            self.game.delete_var()
            return alpha
        
        print(f"depth = {depth}, true_x={true_x}, true_y={true_y}")

    def computer2(self):
        flag = 0
        while True:
            while self.computer_wait == 0:
                if self.game.turn >= 60 or self.pass_conti==2:
                    flag = 1
                    break
                a = 3
            if (flag == 1):
                break
            time.sleep(1.2)
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
            self.game.count_turn()
            self.pass_conti = 0
            min = 1000000000
            max = 0
            self.copyboard(self.copy1, self.game.board)
            self.alpha_beta(self.game.now_player, max, min, self.level, self.level)
            """
            if self.level == 1:
                self.alpha_beta_level1(self.game.now_player)
            elif self.level == 2:
                self.alpha_beta_level2(self.game.now_player, max, min, self.level)
            elif self.level == 3:
                self.alpha_beta_level3(self.game.now_player, max, min, self.level)
            elif self.level == 4:
                self.alpha_beta_level4(self.game.now_player, max, min, self.level)
            """
            
            #for hand in range(0, len(self.game.square), 2):
                #i = self.game.square[hand]
                #j = self.game.square[hand+1]
                #if max < self.valuate[j-1][i-1]:
                    #x = i
                    #y = j
                   # max = self.valuate[j-1][i-1]
            
            #for i in range(1, 9):
              #  for j in range(1, 9):
               #     c = 0
                #    if (self.game.board[i][j]==0):
                 ##          for t in range(-1, 2):
                   #             if k!=0 or t!=0:
                    #                c += self.game.turnover_num(self.game.now_player, j, i, k, t)
                     #   if c > max:
                      #      max = c
                       #     y = i
                        #    x = j
            #self.game.put(self.game.now_player, x, y)
            self.panelrenew(self.game.now_player)
            self.game.turnchange()
            self.count = self.game.count_stone(self.game.now_player)
            self.label1 = Label(self.root, text="あなたの石の数："+str(self.count), font=("times, 16"))
            self.game.delete_list()
            self.label1.place(x=400, y=780)
            self.game.printboard()
            self.computer_wait = 0
            print("finish computer turn")
        
        print("試合終了です")

    def computer(self):
        flag = 0
        while True:
            while self.computer_wait == 0:
                if self.game.turn >= 60 or self.pass_conti==2:
                    flag = 1
                    break
                a = 3
            if (flag == 1):
                break
            time.sleep(1.2)
            print("start computer turn")
            best_move = None
            alpha = -math.inf
            self.copy[self.level] = self.copyboard(self.copy[self.level], self.game.board)
            self.game.count_turn()
            if self.game.research(self.game.now_player) == 0:
                self.game.delete_list()
                self.game.turnchange()
                self.pass_conti += 1
                print("pass computer turn")
                if (self.pass_conti == 1):
                    self.computer_wait = 0
                    continue
                else:
                    break
            self.squarecopies[self.level] = self.canput_copy(self.squarecopies[self.level], self.game.square)
            print(self.game.square)
            for hand in range(0, len(self.game.square), 2):
                x = self.game.square[hand]
                y = self.game.square[hand+1]
        
                self.game.put(self.game.now_player, x, y)
                self.game.delete_var()
                score = -self.alpha_beta(3-self.game.now_player, alpha=-math.inf, beta=-alpha, depth=self.level-1)
                if score > alpha:
                    best_move = (x, y)
                    alpha = score
                self.game.board = self.copyboard(self.game.board, self.copy[self.level])
                self.game.square = self.canput_copy(self.game.square, self.squarecopies[self.level])

            self.game.put(self.game.now_player, best_move[0], best_move[1])


            """
            if self.level == 1:
                self.alpha_beta_level1(self.game.now_player)
            elif self.level == 2:
                self.alpha_beta_level2(self.game.now_player, max, min, self.level)
            elif self.level == 3:
                self.alpha_beta_level3(self.game.now_player, max, min, self.level)
            elif self.level == 4:
                self.alpha_beta_level4(self.game.now_player, max, min, self.level)
            """
            
            #for hand in range(0, len(self.game.square), 2):
                #i = self.game.square[hand]
                #j = self.game.square[hand+1]
                #if max < self.valuate[j-1][i-1]:
                    #x = i
                    #y = j
                   # max = self.valuate[j-1][i-1]
            
            #for i in range(1, 9):
              #  for j in range(1, 9):
               #     c = 0
                #    if (self.game.board[i][j]==0):
                 ##          for t in range(-1, 2):
                   #             if k!=0 or t!=0:
                    #                c += self.game.turnover_num(self.game.now_player, j, i, k, t)
                     #   if c > max:
                      #      max = c
                       #     y = i
                        #    x = j
            #self.game.put(self.game.now_player, x, y)
            self.panelrenew(self.game.now_player)
            self.game.turnchange()
            self.count = self.game.count_stone(self.game.now_player)
            self.label1 = Label(self.root, text="あなたの石の数："+str(self.count), font=("times, 16"))
            self.game.delete_list()
            self.label1.place(x=400, y=780)
            self.game.printboard()
            self.computer_wait = 0
            print("finish computer turn")
        
        print("試合終了です")

    def alpha_beta(self, now_player, alpha: int, beta: int, depth: int):
        # self.game.delete_list()
        if depth == 0:
            return self.calculate_score(3-now_player)
        if self.game.research(now_player) == 0:
            self.game.delete_list()
            return alpha
        

        # 手を打つためのコピーを準備
        self.copy[depth] = self.copyboard(self.copy[depth], self.game.board)
        self.squarecopies[depth].clear()
        self.squarecopies[depth] = self.canput_copy(self.squarecopies[depth], self.game.square)


        for hand in range(0, len(self.game.square), 2):
            x = self.game.square[hand]
            y = self.game.square[hand + 1]

            # 次の手を打つ
            self.game.put(now_player, x, y)
            self.game.delete_var()

            score = -self.alpha_beta(3-self.game.now_player, alpha=-beta, beta=-alpha, depth=depth-1)
            if score > alpha:
                alpha = score

            self.game.board = self.copyboard(self.game.board, self.copy[depth])
            self.game.square = self.canput_copy(self.game.square, self.squarecopies[depth])

            if alpha >= beta:
                return alpha
            
        return alpha
            


    
    def alpha_beta2(self, now_player, alpha: int, beta: int, depth: int, level: int):
        true_x, true_y = 0, 0
        score = 0
        self.copy[depth] = self.copyboard(self.copy[depth], self.game.board)
        self.game.delete_list()

        
        if self.game.research(now_player) == 0:
            self.game.delete_list()
            return alpha
        
        

        # 手を打つためのコピーを準備
        self.squarecopies[depth].clear()
        self.squarecopies[depth] = self.canput_copy(self.squarecopies[depth], self.game.square)


        for hand in range(0, len(self.game.square), 2):
            x = self.game.square[hand]
            y = self.game.square[hand + 1]

            # 次の手を打つ
            self.game.put(now_player, x, y)
            self.game.delete_var()
            if depth == 1:
                score = self.calculate_score(now_player)
                if (score > alpha):
                    alpha = score
                self.game.board = self.copyboard(self.game.board, self.copy[depth])

            # 相手の番に移り、アルファベータ探索を再帰的に呼び出す
            elif depth > 1:
                score = -self.alpha_beta(3 - now_player, alpha=-beta, beta=-alpha, depth=depth - 1, level=level)
                if depth == level:
                    print(score)
                    print(x)
                    print(y)

                # 最適な手を選択
                if hand == 0:
                    alpha = score
                    true_x = x
                    true_y = y

                if score > alpha:
                    alpha = score
                    true_x = x
                    true_y = y
                self.game.board = self.copyboard(self.game.board, self.copy1)
                self.game.square = self.canput_copy(self.game.square, self.squarecopies[depth])
                if alpha >= beta:
                    self.game.delete_list()
                    return alpha

        if depth == level:
            print("unko")
            self.game.put(now_player, true_x, true_y)
            print(f"score: {score}")
            print(f"x: {true_x}")
            print(f"y: {true_y}")
            print(self.game.variation)

        return alpha
    
            
    def calculate_score(self, now_player):
        myscore=0
        enemy = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.game.board[i][j]==now_player):
                    myscore += self.valuate[i-1][j-1]
                elif (self.game.board[i][j]==3-now_player):
                    enemy += self.valuate[i-1][j-1]

        return myscore - enemy


    def copyboard(self, copy, original):
        for i in range(1, 9):
            for j in range(1, 9):
                copy[i][j] = original[i][j]
        return copy

    def canput_copy(self, copy, original):
        copy = []
        for i in range(len(original)):
            copy.append(original[i])
        return copy





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