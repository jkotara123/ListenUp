from music_components.Interval import Interval
from music_components.Piano import Piano
from gameModes.abstractMode import abstractMode


class IntervalMode(abstractMode):
    def __init__(self, piano) -> None:
        self.interval: Interval = None
        self.piano: Piano = piano
        self.correct = 0
        self.wrong = 0

    def get_new_question(self):
        self.interval: Interval = Interval.random_interval(self.piano)
        return {self.interval.second}

    def play_question(self):
        self.interval.play_interval('darkblue')
