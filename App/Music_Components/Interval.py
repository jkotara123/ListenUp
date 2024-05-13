from time import sleep
from .Creating_random_note import create_random_note


class Interval:
    def __init__ (self, octaves, lowest_octave, create_random=True, first=None, second=None, time_gaps=None):
        self.sound_sequence = []
        if create_random:
            first = create_random_note(octaves, lowest_octave)
            second = create_random_note(octaves, lowest_octave, first, 11)
            # third = create_random(octaves, notes, second , 5)

        self.sound_sequence.append(first)
        self.sound_sequence.append(second)
        self.time_gaps = None
        if time_gaps is None:
            self.time_gaps = [0.6]


    def set_time_gaps (self, time_gaps):
        self.time_gaps = time_gaps


    def get_time_gaps (self):  # ! liste floatów o jeden mniej dźwięk
        return self.time_gaps


    def get_to_show (self):  # ! indeksy nutek ktore maja sie swiecic na niebisko
        return [0]


    def get (self, i):  # zwraca i-ty element sekwencji
        return self.sound_sequence[i]


    def get_sequence (self):  # zwraca cala liste jako liste
        return self.sound_sequence


    def size (self):  # zwraca rozmiar listy
        return len(self.sound_sequence)
