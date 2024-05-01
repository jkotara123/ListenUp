from music_components.Note import Note
from questionHandler import questionHandler
import tkinter as tk
import threading
from time import sleep


green = ["green2","green3","green4","darkgreen"]
red = ["red","red2","red3","red4"]
blue = ["RoyalBlue1","RoyalBlue2","RoyalBlue3","blue2","blue4","navy"]


class Key(tk.Button):
    def __init__(self, master, note: Note, handler, **kwargs):
        super().__init__(master=master, **kwargs)
        self.note: Note = note
        self.is_black: bool = 'b' in self.note.name
        self.handler = handler

    def __str__(self) -> str:
        return self.note

    def __repr__(self) -> str:
        return self.note.name

    def play_sound(self):
        self.note.play()

    def __change_color(self, color, duration=0.5):
        def change(color, duration):
            # base_color = self['background']
            base_color = "white"
            if self.is_black:
                base_color = "black"
            # self.configure(bg=color)
            # sleep(duration)
            # self.configure(bg=base_color)
            color_array = None
            if color == 'red':
                color_array = red
            elif color == 'green':
                color_array = green
            else:
                color_array = blue
            sleep_time = duration/(len(color_array)*2)
            for i in range (0,len(color_array)):
                self.configure(bg=color_array[i])
                sleep(sleep_time)
            for i in range (len(color_array)-2,-1,-1):
                self.configure(bg=color_array[i])
                sleep(sleep_time)
            self.configure(bg=base_color)

        thread = threading.Thread(
            target=change, args=(color, duration))
        thread.start()

    def clicked(self):
        handler = self.handler

        def go_next():  # jak odpalic tylko jeden watek z pytaniem jednoczesnie
            sleep(2)

            # handler.next_question() # uncomment this line if running app.py
            # if handler.current_quiz_manager is not None:
            #     handler.current_quiz_manager.update_window_after_new_question()

        if self.handler.is_active():
            response = handler.check_answer(self)
            if response == 0:
                self.play_key('red')
            elif response != 2:
                self.play_key('green')
            else:
                self.play_key()
            thread = threading.Thread(target=go_next)
            thread.start()

    def play_key(self, color=None, duration=0.5):
        self.play_sound()
        if not (color is None):
            self.__change_color(color, duration)


    def temporarily_disable_key (self):
        self.configure(bg="grey")


    def enable_key (self):
        if not self.is_black:
            self.configure(bg="white")
        else:
            self.configure(bg="black")
