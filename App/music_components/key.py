import tkinter as tk
from time import sleep
import threading
import json
from .note import Note

with open("resources/config.json", "r") as f:
    config = json.load(f)
green = config["key_coloring"]["green"]
red = config["key_coloring"]["red"]
blue = config["key_coloring"]["blue"]
gold = config["key_coloring"]["gold"]


class Key(tk.Button):
    def __init__(self, master, note: Note, parent_piano, **kwargs) -> None:
        super().__init__(master=master, **kwargs)
        self.note: Note = note
        self.parent_piano = parent_piano

    def get_note_name(self) -> str:
        return self.note.get_name()

    def play_sound(self) -> None:
        self.note.play_sound()

    def is_black(self) -> bool:
        return self.note.corresponds_to_black_key()

    def clicked(self) -> None:
        if self.parent_piano.is_enabled():
            self.play_key()
            self.parent_piano.key_was_clicked(self.note.get_name())

    def __change_color(self, color: str, duration=0.4) -> None:
        def internal_change_color():
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
            sleep_time = duration / (2 * len(color_array))

            for i in range(0, len(color_array)):
                self.configure(bg=color_array[i])
                sleep(sleep_time)
            for i in range(len(color_array) - 2, -1, -1):
                self.configure(bg=color_array[i])
                sleep(sleep_time)
            self.configure(bg=base_color)

        color_change_thread = threading.Thread(target=internal_change_color)
        color_change_thread.start()

    def play_key(self) -> None:
        self.play_sound()
        color = self.parent_piano.get_key_color(self.get_note_name())
        if color is not None:
            self.__change_color(color, duration=0.8)
