import tkinter as tk
from drawPiano import drawPiano


def clicked(color, num):
    print(color + ': ' + str(num))


root = tk.Tk()
root.geometry('1000x400')

Keys = drawPiano(root)


root.mainloop()
