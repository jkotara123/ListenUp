from time import sleep
from .Creating_random_note import create_random_note


class Interval:
    def __init__ (self, octaves, lowest_octave, create_random=True, first=None, second=None, time_gaps=None):
        self.sound_sequence = []
        if create_random:
            first = create_random_note(octaves, lowest_octave)
            second = create_random_note(octaves, lowest_octave, first, 11)

        self.sound_sequence.append(first)
        self.sound_sequence.append(second)
        self.time_gaps = None
        if time_gaps is None:
            self.time_gaps = [0.6]


    def set_time_gaps (self, time_gaps):
        self.time_gaps = time_gaps


    def get_time_gaps (self):
        return self.time_gaps


    def get_to_show (self):
        return [0]


    def get (self, i):
        return self.sound_sequence[i]


    def get_sequence (self):
        return self.sound_sequence


    def size (self):
        return len(self.sound_sequence)
