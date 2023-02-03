from tkinter import *

class Ball():
    def __init__(self,posx,posy,sizex,sizey,canvas):
        self.posx=posx
        self.posy=posy
        self.dx=0
        self.dy=-10
        self.sizex=sizex
        self.sizey=sizey
        self.canvas=canvas
        self.display=self.canvas.create_oval(self.posx-int(self.sizex/2),self.posy-int(self.sizey/2),self.posx+int(self.sizex/2),self.posy+int(self.sizey/2),fill="#A66",outline="#944")
    def move(self):
        self.posx+=self.dx
        self.posy+=self.dy
        print(self.posx,self.posy)
        if self.posx>600:
            self.impact(0,-1)
            self.move()
        if self.posx<0:
            self.impact(0,1)
            self.move()
        if self.posy<0:
            self.impact(1,0)
            self.move()
        self.canvas.coords(self.display,self.posx-int(self.sizex/2),self.posy-int(self.sizey/2),self.posx+int(self.sizex/2),self.posy+int(self.sizey/2))
    def impact(self,cos,sin):
        self.dy,self.dx=self.dx*sin-self.dy*cos,self.dx*cos+sin*self.dy
        self.move()
    def get_posx(self):
        return self.posx
    def get_posy(self):
        return self.posy
    def delete(self):
        self.canvas.delete(self.display)