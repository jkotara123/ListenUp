from Note import Note
import tkinter as tk


class Key:
    def __init__(self, note: Note, button: tk.Button = None):
        self.note = note
        self.button = button

    def __str__(self) -> str:
        return self.note

    def __repr__(self) -> str:
        return self.note.name

    def is_black(self):
        return self.note.corresponds_to_black_key()

    def collides_with(self, event) -> bool:
        return self.rect.collidepoint(event)

    def play_sound(self):
        self.note.play_sound()
