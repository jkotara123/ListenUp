import random
import json


with open("resources/music_data.json", "r") as f:
    music_data = json.load(f)
note_names = music_data["note_names"]


def create_notes(octaves: int, lowest_octave: int, intervals: list[int]):
    chord_len = intervals[-1]
    base_note = random.randint(0, octaves * 12 - chord_len - 1)
    rand_note_names = []
    for interval in intervals:
        rand_note_names.append(
            note_names[(base_note + interval) % 12]
            + str((base_note + interval) // 12 + lowest_octave)
        )
    return rand_note_names
