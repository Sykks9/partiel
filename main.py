from tkinter import *
from game import *

window=Tk()
window.geometry("1000x700")
window.title("Casse-briques")
window.config(background="#EED")

game=Game(window)

window.mainloop()