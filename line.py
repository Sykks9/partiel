from tkinter import *
from block import *

class Line():
    def __init__(self,posx,posy,number,sizex,sizey,canvas,window):
        self.canvas=canvas
        self.window=window
        self.posx=posx
        self.posy=posy
        self.number=number
        self.sizex=sizex
        self.sizey=sizey
        self.blocks=[]
        for i in range(number):
            self.blocks.append(Block(self.posx,i,self.posy,self.sizex,self.sizey,self.canvas))
    def get_blocks(self):
        return self.blocks
    def delete(self,block:Block):
        block.delete()
        self.blocks.remove(block)