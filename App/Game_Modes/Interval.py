from time import sleep
from .Quizable import Quizable
from .Game_mode_specs import Game_mode_specs
from .Creating_random_note import create_notes
import random


class Interval(Quizable):
    def __init__(self, octaves, lowest_octave, specs: Game_mode_specs, first=None, second=None, time_gaps=[0.6]):

        if first != None and second != None:
            self.sound_sequence = [first, second]
        else:
            interval = random.choice(specs.get_types())
            self.sound_sequence = create_notes(
                octaves, lowest_octave, interval, first)
        if random.randint(0, 2) > 0:
            self.to_show = [0]
            self.expected = [1]
        else:
            self.to_show = [1]
            self.expected = [0]

        self.time_gaps = time_gaps

    def set_time_gaps(self, time_gaps):
        self.time_gaps = time_gaps

    def get_time_gaps(self):
        return self.time_gaps

    def get_to_show(self):
        return self.to_show

    def get_expected(self, i):
        return self.sound_sequence[self.expected[i]]

    def get_sequence(self):
        return self.sound_sequence

    def size(self):
        return 1

    def get(self, i):
        return self.sound_sequence[i]
