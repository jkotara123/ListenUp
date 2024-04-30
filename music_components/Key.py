from music_components.Note import Note
from questionHandler import questionHandler
import tkinter as tk
import threading
from time import sleep


class Key(tk.Button):
    def __init__(self, master, note: Note, **kwargs):
        super().__init__(master=master, **kwargs)
        self.note: Note = note
        self.is_black: bool = 'b' in self.note.name
        self.handler: questionHandler = questionHandler()

    def __str__(self) -> str:
        return self.note

    def __repr__(self) -> str:
        return self.note.name

    def play_sound(self):
        self.note.play()

    def __change_color(self, color, duration=0.5):
        def change(color, duration):
            base_color = self['background']
            self.configure(bg=color)
            sleep(duration)
            self.configure(bg=base_color)
        thread = threading.Thread(
            target=change, args=(color, duration))
        thread.start()

    def clicked(self):
        def go_next():  # jak odpalic tylko jeden watek z pytaniem jednoczesnie
            sleep(2)
            self.handler.next_question()
        response = self.handler.check_answer(self)
        if response == 0:
            self.play_key('red')
        elif response != 2:
            self.play_key('green')
        else:
            self.play_key()
        if response == 0 or response == 1:
            # odpalenie kolejnego pytania automatycznie (do zmiany w ustawieniach - 2. opcja z przyciskiem next_question)
            thread = threading.Thread(target=go_next)
            thread.start()

    def play_key(self, color=None, duration=0.5):
        self.play_sound()
        if color != None:
            self.__change_color(color, duration)
