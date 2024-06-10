from .quizzable import Quizzable
from .game_mode_specs import GameModeSpecs
from .creating_random_note import create_notes
import random
import json

with open('resources/music_data.json', 'r') as f:
    music_data = json.load(f)
interval_types: dict = music_data["interval_types"]


class Interval(Quizzable):
    def __init__(self, octaves, lowest_octave, specs: GameModeSpecs, first=None, second=None, time_gaps=[0.6]):
        if first != None and second != None:
            self.sound_sequence = [first, second]
        else:
            interval_list = []
            if specs.is_empty():
                raise ValueError("At least one interval must be selected.")
            for interval in specs.get_types():
                x = interval_types.get(interval)
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
