from tkinter import *

class Block():
    def __init__(self,posx,i,posy,sizex,sizey,canvas) -> None:
        self.canvas=canvas
        self.posy=posy
        self.number=i
        self.sizex=sizex
        self.sizey=sizey
        self.posx=posx+self.sizex*self.number
        self.display=self.canvas.create_rectangle(self.posx-int(self.sizex/2),self.posy-int(self.sizey/2),self.posx+int(self.sizex/2),self.posy+int(self.sizey/2),fill="#88E",outline="#66C")
    def get_posx(self):
        return self.posx
    def get_posy(self):
        return self.posy
    def delete(self):
        self.canvas.delete(self.display)