from tkinter import *
from player import *
from line import *
from ball import *
from math import *

class Game():
    def __init__(self,window):
        self.window=window
        self.canvas=Canvas(self.window,width=600,height=600,background="#114")
        self.canvas.place(x=200,y=100)
        self.score=Label(self.window,text="Score : 0", font="Helvetic 14 bold", foreground="#A33", background="#EED")
        self.score.place(x=500,y=25)
        self.start_button=Button(self.window,text="START GAME",command=self.start)
        self.start_button.place(x=50,y=500)
        self.quit_button=Button(self.window,text="QUIT GAME",command=self.window.quit)
        self.quit_button.place(x=50,y=600)
        self.menu=Menu(self.window, tearoff=0)
        self.game_menu=Menu(self.menu, tearoff=0)
        self.start_menu=self.game_menu.add_command(label="Start game", command=self.start)
        self.quit_menu=self.game_menu.add_command(label="Quit game", command=self.window.quit)
        self.menu.add_cascade(label="Game",menu=self.game_menu)
        self.window.config(menu=self.menu)
    def start(self):
        self.game_menu.entryconfig("Start game", state=DISABLED)
        self.start_button.config(state=DISABLED)
        self.player=Player(self.canvas,self.window)
        self.line=Line(50,100,15,30,10,self.canvas,self.window)
        self.ball=Ball(300,535,20,20,self.canvas)
        self.window.bind("<a>",self.player.move_left)
        self.window.bind("<z>",self.player.move_right)
        self.window.after(50,self.refresh)
    def refresh(self):
        self.ball.move()
        for block in self.line.get_blocks():
            if abs(block.get_posx()-self.ball.get_posx())<=15 and abs(block.get_posy()-self.ball.get_posy())<=15:
                self.ball.impact(1,0)
                self.line.delete(block)
                self.score['text']="Score : "+str(10+int(self.score['text'].split(" : ")[1]))
        if abs(self.player.get_posx()-self.ball.get_posx())<=25 and abs(self.player.get_posy()-self.ball.get_posy())<=10:
            self.ball.impact(cos(pi*(self.player.get_posx()-self.ball.get_posx())/25),sin(pi*(self.player.get_posx()-self.ball.get_posx())/25))
        if self.ball.get_posy()>600:
            self.ball.delete()
            self.player.lose_life()
            self.ball=Ball(self.player.get_posx(),535,20,20,self.canvas)
        if self.line.get_blocks()==[] or self.player.get_life()<0:
            self.window.after(50,self.endgame)
        else:
            self.window.after(50,self.refresh)
    def endgame(self):
        self.game_menu.entryconfig("Start game", state=DISABLED)
        self.start_button.config(state=DISABLED)
        print("end game")
