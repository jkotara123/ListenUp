from music_components.Interval import Interval
from music_components.Piano import Piano


class IntervalMode:
    def __init__(self, piano = None) -> None:
        self.interval: Interval = None
        self.piano: Piano = piano
        self.correct = 0
        self.wrong = 0


    def set_piano (self,piano):
        self.piano = piano

    def get_new_question(self):
        self.interval = Interval.random_interval(self.piano)
        return {self.interval.second}

    def play_question(self):
        self.interval.play_interval('darkblue')
