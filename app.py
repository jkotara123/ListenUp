from music_components.Chord import Chord
import tkinter as tk
import pygame
from quizManager import quizManager
pygame.mixer.init()
pygame.mixer.set_num_channels(16)
root = tk.Tk()
root.geometry('1000x400')

game = quizManager(root, 1, 3, 2)

game.play()

root.mainloop()
