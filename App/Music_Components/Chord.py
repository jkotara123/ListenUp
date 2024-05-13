import random
from .Creating_random_note import create_notes
from .Quizable import Quizable


class Chord(Quizable):

    Major = [[0, 4, 7]]
    Major_rev = [[0, 3, 8], [0, 5, 9]]
    Minor = [[0, 3, 7]]
    Minor_rev = [[0, 4, 9], [0, 5, 8]]
    Major7 = [[0, 4, 7, 10], [0, 4, 7, 11]]
    Minor7 = [[0, 3, 7, 10]]
    Diminished = [[0, 3, 6, 9]]

    def __init__(self, octaves, lowest_octave, create_random=True, base: str = None, intervals: list[int] = None, time_gaps=None,  notes_to_show=None, number_of_notes_to_show=1, **kwargs) -> None:
        self.sound_sequence = []
        self.base_note = base
        self.intervals = intervals
        if base != None and intervals != None:
            self.sound_sequence = create_notes(
                octaves, lowest_octave, intervals, base)
        self.to_show = notes_to_show if notes_to_show != None else [0]
        if create_random:
            chord_list = []
            if kwargs.get("major", False):
                chord_list += Chord.Major
            if kwargs.get("major_rev", False):
                chord_list += Chord.Major_rev
            if kwargs.get("minor", False):
                chord_list += Chord.Minor
            if kwargs.get("minor_rev", False):
                chord_list += Chord.Minor_rev
            if kwargs.get("major7", False):
                chord_list += Chord.Major7
            if kwargs.get("minor7", False):
                chord_list += Chord.Minor7
            if kwargs.get("diminished", False):
                chord_list += Chord.Diminished
            if len(chord_list) == 0:  # Brak zaznaczenia -> blad
                raise ValueError("At least one chord type must be selected.")

            self.intervals = random.choice(chord_list)
            self.sound_sequence = create_notes(
                octaves, lowest_octave, self.intervals)

            self.base_note = self.sound_sequence[0]
            self.to_show = [0]
            choose_to_show = [i+1 for i in range(len(self.intervals)-1)]
            self.to_show += random.sample(
                choose_to_show, number_of_notes_to_show-1)

        self.time_gaps = time_gaps if time_gaps != None else [
            0.2 for _ in range(len(self.intervals)-1)]
        self.expected = [
            i for i in range(len(self.intervals)) if i not in self.to_show]
        print(self.sound_sequence)
        print(self.to_show, " --- ", self.expected)

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
