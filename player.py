from tkinter import *

class Player():
    def __init__(self,canvas,window):
        self.window=window
        self.canvas=canvas
        self.posx=300
        self.posy=550
        self.speed=10
        self.display=self.canvas.create_rectangle(self.posx-25,self.posy-5,self.posx+25,self.posy+5,fill="#88E",outline="#66C")
        self.life=3
    def move_right(self,event):
        if self.posx+25+self.speed<=600:
            self.posx+=self.speed
            self.canvas.coords(self.display,self.posx-25,self.posy-5,self.posx+25,self.posy+5)
    def move_left(self,event):
        if self.posx-25-self.speed>0:
            self.posx-=self.speed
            self.canvas.coords(self.display,self.posx-25,self.posy-5,self.posx+25,self.posy+5)
    def get_posx(self):
        return self.posx
    def get_posy(self):
        return self.posy
    def lose_life(self):
        self.life-=1
    def get_life(self):
        return self.life