from music_components.Interval import Interval
from music_components.Piano import Piano
from gameModes.AbstractMode import AbstractMode


class IntervalMode(AbstractMode):
    def __init__(self, piano = None, time_gap=0.5) -> None:
        self.interval: Interval = None
        self.time_gap = time_gap
        self.piano: Piano = piano
        self.correct = 0
        self.wrong = 0


    def set_piano (self,piano):
        self.piano = piano

    def get_new_question(self):
        self.interval: Interval = Interval.random_interval(self.piano)
        return [self.interval.second]

    def play_question(self):
        self.interval.play_interval('darkblue', time_gap=self.time_gap)

    def show_question(self):
        self.interval.play_interval(
            'darkblue', 'darkgreen', time_gap=self.time_gap)
