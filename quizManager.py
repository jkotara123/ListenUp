from questionHandler import questionHandler
from music_components.Piano import Piano
from gameModes.IntervalMode import IntervalMode
from gameModes.AbstractMode import AbstractMode
from gameModes.ChordMode import ChordMode


class quizManager:
    def __init__(self, root, mode=0, time_gap=0.5, octaves=2, lowest_octave=3) -> None:
        self.handler = questionHandler()
        self.piano = Piano(root, octaves, lowest_octave)
        if mode == 0:
            self.gameMode: AbstractMode = IntervalMode(
                self.piano, time_gap=time_gap)
        elif mode == 1:
            self.gameMode: AbstractMode = ChordMode(
                self.piano, time_gap=time_gap, major=True, minor=True, major_rev=True, minor_rev=True, major7=True, minor7=True, diminished=True)
        self.handler.set_mode(self.gameMode)

    def play(self):
        self.handler.next_question()
