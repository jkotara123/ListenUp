# from pygame import mixer
import pygame


class Note:
    def __init__(self, name: str, sound: pygame.mixer.Sound):
        self.name = name
        self.sound = sound
        self.black = True if '#' in name else False

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Key:
    def __init__(self, note: Note, rect: pygame.Rect):
        self.note = note
        self.rect = rect
        self.black = note.black

    def __str__(self) -> str:
        return self.note

    def __repr__(self) -> str:
        return self.note.name
