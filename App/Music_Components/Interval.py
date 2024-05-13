from time import sleep
from .Quizable import Quizable
from .Creating_random_note import create_random_note


class Interval(Quizable):
    def __init__(self, octaves, lowest_octave, create_random=True, first=None, second=None, time_gaps=None):
        self.sound_sequence = []
        self.expected = [1]
        if create_random:
            first = create_random_note(octaves, lowest_octave)
            second = create_random_note(octaves, lowest_octave, first, 11)
            # third = create_random(octaves, notes, second , 5)

        self.sound_sequence.append(first)
        self.sound_sequence.append(second)
        self.time_gaps = None
        if time_gaps is None:
            self.time_gaps = [0.6]

    def set_time_gaps(self, time_gaps):
        self.time_gaps = time_gaps

    def get_time_gaps(self):
        return self.time_gaps

    def get_to_show(self):
        return [0]

    def get_expected(self, i):
        # print(self.expected, self.sound_sequence, i)
        # print(self.sound_sequence[self.expected[i]])
        return self.sound_sequence[self.expected[i]]

    def get_sequence(self):
        return self.sound_sequence

    def size(self):
        return 1
      
    def get (self, i):  # zwraca i-ty element sekwencji
        return self.sound_sequence[i]
