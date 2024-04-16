from Sound import Sound
from Sound import note_names


class Note:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def corresponds_to_black_key(self):
        return '#' in self.name

    def play_sound(self):
        self.sound.play_sound()


def get_notes(octaves=2) -> list[Note]:  # lista nutek
    notes = []
    for i in range(3, octaves+3):
        for name in note_names:
            note = Note(str(i)+name)
            notes.append(note)
    return notes
