from questionHandler import questionHandler
from music_components.Piano import Piano
from gameModes.IntervalMode import IntervalMode


class quizManager:
    def __init__(self, root, mode, octaves=2, lowest_octave=3) -> None:
        self.piano = Piano(root, octaves, lowest_octave)
        self.gameMode = IntervalMode(self.piano)
        self.handler = questionHandler()
        self.handler.set_mode(self.gameMode)

    def play(self):
        self.handler.next_question()
