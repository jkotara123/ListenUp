import random
from .creating_random_note import create_notes
from .quizzable import Quizzable
from .game_mode_specs import GameModeSpecs
import json


with open("resources/music_data.json", "r") as f:
    music_data = json.load(f)
chord_types: dict = music_data["chord_types"]


class Chord(Quizzable):
    def __init__(self, octaves: int, lowest_octave: int, specs: GameModeSpecs) -> None:
        chord_list = []
        if specs.is_empty():
            raise ValueError("At least one chord type must be selected.")
        for type in specs.get_types():
            x = chord_types.get(type)
            if x != None:
                chord_list.append(x)
        self.intervals: list[int] = random.choice(chord_list)
        self.sound_sequence: list[str] = create_notes(
            octaves, lowest_octave, self.intervals
        )
        self.base_note: str = self.sound_sequence[0]
        choose_to_show = [i + 1 for i in range(len(self.intervals) - 1)]
        self.to_show: list[int] = [0] + random.sample(
            choose_to_show, specs.get_number_of_notes_to_show() - 1
        )
        self.time_gaps: list[float] = [0.2 for _ in range(len(self.intervals) - 1)]
        self.expected: list[int] = [
            i for i in range(len(self.intervals)) if i not in self.to_show
        ]

    def get_time_gaps(self) -> list[float]:
        return self.time_gaps

    def get_to_show(self) -> list[int]:
        return self.to_show

    def get_expected(self, i: int) -> str:
        return self.sound_sequence[self.expected[i]]

    def get_sequence(self) -> list[str]:
        return self.sound_sequence

    def size(self) -> int:
        return len(self.expected)
