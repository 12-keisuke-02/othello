import tkinter as tk
import tkinter.ttk as ttk
import sys

class Client():
    def __init__(self):
        self.player = 1

    def creategamepanel(self, row, myname, color):
        root = tk.Tk()
        root.title("reversi game")
        root.geometry("1000x800")
       
        self.start_x = tk.StringVar()
        self.start_y = tk.StringVar()
        self.stop_x = tk.StringVar()
        self.stop_y = tk.StringVar()
        gameboard = tk.Canvas(root, width=720, height=720)
        gameboard.create_rectangle(0, 0 , 720, 720, fill = 'green')
        gameboard.place(x=140, y=40)
        gameboard.create_line(0, 0, 720, 0)
        gameboard.create_line(0, 90, 720, 90)
        gameboard.create_line(0, 180, 720, 180)
        gameboard.create_line(0, 270, 720, 270)
        gameboard.create_line(0, 360, 720, 360)
        gameboard.create_line(0, 450, 720, 450)
        gameboard.create_line(0, 540, 720, 540)
        gameboard.create_line(0, 630, 720, 630)
        gameboard.create_line(0, 720, 720, 720)
        gameboard.create_line(0, 0, 0, 720)
        gameboard.create_line(90, 0, 90, 720)
        gameboard.create_line(180, 0, 180, 720)
        gameboard.create_line(270, 0, 270, 720)
        gameboard.create_line(360, 0, 360, 720)
        gameboard.create_line(450, 0, 450, 720)
        gameboard.create_line(540, 0, 540, 720)
        gameboard.create_line(630, 0, 630, 720)
        gameboard.create_line(720, 0, 720, 720)
        gameboard.create_oval(270, 270, 360, 360, fill="black")
        gameboard.create_oval(360, 360, 450, 450, fill="black")
        gameboard.create_oval(270, 360, 360, 450, fill="white")
        gameboard.create_oval(360, 270, 450, 360, fill="white")
        gameboard.bind('<ButtonPress-1>', self.start_pickup)

        root.mainloop()

        

    def start_pickup(self, event):
        self.start_x.set('x : ' + str(event.x))
        self.start_y.set('y : ' + str(event.y))
        print(str(event.x))
        print(str(event.y))




def main():
    client = Client()
    client.creategamepanel(8, "god", 1)

main()

