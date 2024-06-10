import random
from .creating_random_note import create_notes
from .quizzable import Quizzable
from .game_mode_specs import GameModeSpecs
import json


with open('resources/music_data.json', 'r') as f:
    music_data = json.load(f)
chord_types: dict = music_data["chord_types"]


class Chord(Quizzable):
    def __init__(self, octaves, lowest_octave, specs: GameModeSpecs, intervals: list[int] = None, base: str = None, time_gaps=None, notes_to_show=[0]) -> None:
        self.sound_sequence = []
        self.base_note = base
        self.intervals = intervals
        self.to_show = notes_to_show

        if base != None and intervals != None:
            self.sound_sequence = create_notes(
                octaves, lowest_octave, intervals, base)
        else:
            chord_list = []
            if specs.is_empty():
                raise ValueError("At least one chord type must be selected.")
            for type in specs.get_types():
                x = chord_types.get(type)
                if x != None:
                    chord_list.append(x)
            self.intervals = random.choice(chord_list)
            self.sound_sequence = create_notes(
                octaves, lowest_octave, self.intervals)

            self.base_note = self.sound_sequence[0]

            choose_to_show = [i+1 for i in range(len(self.intervals)-1)]
            self.to_show += random.sample(
                choose_to_show, specs.get_number_of_notes_to_show()-1)

        self.time_gaps = time_gaps if time_gaps != None else [
            0.2 for _ in range(len(self.intervals)-1)]
        self.expected = [
            i for i in range(len(self.intervals)) if i not in self.to_show]

    def get_time_gaps(self):
        return self.time_gaps

    def get_to_show(self):
        return self.to_show

    def get_expected(self, i):
        return self.sound_sequence[self.expected[i]]

    def get_sequence(self):
        return self.sound_sequence

    def size(self):
        return len(self.expected)
