from .sound import Sound
import json

with open("resources/music_data.json", "r") as f:
    data = json.load(f)
note_names = data["note_names"]
white_names = data["white_names"]
black_names = data["black_names"]


class Note:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.sound: Sound = Sound(name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name

    def corresponds_to_black_key(self) -> bool:
        return "b" in self.name

    def play_sound(self) -> None:
        self.sound.play()


def get_notes(octaves=2, lowest_octave=3) -> list[Note]:
    notes = []
    for i in range(lowest_octave, octaves + lowest_octave):
        for name in note_names:
            note = Note(str(i) + name)
            notes.append(note)
    return notes


def get_black_notes(octaves=2, lowest_octave=3) -> list[Note]:
    black_notes = []
    for i in range(lowest_octave, lowest_octave + octaves):
        for name in black_names:
            note = Note(name + str(i))
            black_notes.append(note)
    return black_notes


def get_white_notes(octaves=2, lowest_octave=3) -> list[Note]:
    white_notes = []
    for i in range(lowest_octave, lowest_octave + octaves):
        for name in white_names:
            note = Note(name + str(i))
            white_notes.append(note)
    return white_notes
