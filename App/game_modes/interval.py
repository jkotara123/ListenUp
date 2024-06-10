from .quizzable import Quizzable
from .game_mode_specs import GameModeSpecs
from .creating_random_note import create_notes
import random
import json

with open("resources/music_data.json", "r") as f:
    music_data = json.load(f)
interval_types: dict = music_data["interval_types"]


class Interval(Quizzable):
    def __init__(self, octaves: int, lowest_octave: int, specs: GameModeSpecs) -> None:
        interval_list = []
        if specs.is_empty():
            raise ValueError("At least one interval must be selected.")
        for interval in specs.get_types():
            x = interval_types.get(interval)
            if x != None:
                interval_list.append(x)
        self.interval: list[int] = random.choice(interval_list)
        self.sound_sequence: list[str] = create_notes(
            octaves, lowest_octave, self.interval
        )
        if random.randint(0, 2) == 0:
            self.sound_sequence.reverse()
        self.to_show = [0]
        self.expected = [1]
        self.time_gaps = [0.6]

    def set_time_gaps(self, time_gaps: list[float]) -> None:
        self.time_gaps = time_gaps

    def get_time_gaps(self) -> list[float]:
        return self.time_gaps

    def get_to_show(self) -> list[int]:
        return self.to_show

    def get_expected(self, i: int) -> str:
        return self.sound_sequence[self.expected[i]]

    def get_sequence(self) -> list[str]:
        return self.sound_sequence

    def size(self) -> int:
        return 1

    def get(self, i: int) -> str:
        return self.sound_sequence[i]
