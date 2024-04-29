import tkinter as tk
import pygame
from quizManager import QuizManager, quizManager
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

root = tk.Tk()
root.geometry('1000x400')

game = quizManager(root, 0, 3, 2)
game.play()

root.mainloop()
