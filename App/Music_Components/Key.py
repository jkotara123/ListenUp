import tkinter as tk
from time import sleep
import threading


green = ["green2", "green3", "green4"]
red = ["red2", "red3", "red4"]
blue = ["DodgerBlue2", "DodgerBlue3", "DodgerBlue4"]
gold = ["goldenrod1", "goldenrod2", "goldenrod3"]



class Key(tk.Button):
    def __init__(self, master, note, parent_piano, **kwargs):
        super().__init__(master=master, **kwargs)
        self.note = note
        self.parent_piano = parent_piano


    def get_note_name (self):
        return self.note.get_name()


    def play_sound (self):
        self.note.play_sound()


    def is_black (self):
        return self.note.corresponds_to_black_key()


    def clicked (self,):
        if self.parent_piano.is_enabled():
            self.play_key()
            self.parent_piano.key_was_clicked(self.note.get_name())


    def __change_color (self, color, duration=0.4):
        print(color)

        def internal_change_color ():
            base_color = "white"
            if self.is_black():
                base_color = "black"
            color_array = None
            if color == "red":
                color_array = red
            elif color == "green":
                color_array = green
            elif color == "blue":
                color_array = blue
            elif color == "gold":
                color_array = gold
            sleep_time = duration/(2*len(color_array))

            for i in range (0, len(color_array)):
                self.configure(bg=color_array[i])
                sleep(sleep_time)
            for i in range (len(color_array)-2, -1, -1):
                self.configure(bg=color_array[i])
                sleep(sleep_time)
            self.configure(bg=base_color)

        color_change_thread = threading.Thread(target=internal_change_color)
        color_change_thread.start()


    def play_key (self):
        self.play_sound()
        color = self.parent_piano.get_key_color(self.get_note_name())
        if color is not None:
            self.__change_color(color, duration=0.8)



