from music_components.Chord import Chord
from music_components.Piano import Piano
from gameModes.AbstractMode import AbstractMode


class ChordMode(AbstractMode):
    def __init__(self, piano, time_gap=0.5, **kwargs) -> None:
        self.chord: Chord = None
        self.piano: Piano = piano
        self.time_gap = time_gap
        self.correct = 0
        self.wrong = 0
        self.args = kwargs

    def get_new_question(self):
        self.chord: Chord = Chord.random_chord(self.piano, **self.args)
        return self.chord.keys[1:]

    def play_question(self):
        self.chord.play_chord('darkblue', time_gap=self.time_gap)
