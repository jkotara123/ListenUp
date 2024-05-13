from .Quizable import Quizable
from .Game_mode_specs import Game_mode_specs
from .Creating_random_note import create_notes
import random


class Interval(Quizable):
    interval_types = {
        "Unison": [0, 0],
        "Minor second": [0, 1],
        "Major second": [0, 2],
        "Minor third": [0, 3],
        "Major third": [0, 4],
        "Perfect fourth": [0, 5],
        "Tritone": [0, 6],
        "Perfect fifth": [0, 7],
        "Minor sixth": [0, 8],
        "Major sixth": [0, 9],
        "Minor seventh": [0, 10],
        "Major seventh": [0, 11],
        "Octave": [0, 12]
    }

    def __init__(self, octaves, lowest_octave, specs: Game_mode_specs, first=None, second=None, time_gaps=[0.6]):
        if first != None and second != None:
            self.sound_sequence = [first, second]
            self.name = "?>?"
        else:
            interval_list = []
            if specs.is_empty():
                raise ValueError("At least one interval must be selected.")
            for interval in specs.get_types():
                x = Interval.interval_types.get(interval)
                if x != None:
                    interval_list.append(x)
            interval = random.choice(interval_list)
            self.sound_sequence = create_notes(
                octaves, lowest_octave, interval, first)
            self.name = interval
        if random.randint(0, 2) == 0:
            self.sound_sequence.reverse()
        self.to_show = [0]
        self.expected = [1]

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
