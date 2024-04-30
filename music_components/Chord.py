from music_components.Key import Key
from music_components.Piano import Piano
import threading
import random
from time import sleep


class Chord:
    Major = [[0, 4, 7]]
    Major_rev = [[0, 3, 8], [0, 5, 9]]
    Minor = [[0, 3, 7]]
    Minor_rev = [[0, 4, 9], [0, 5, 8]]
    Major7 = [[0, 4, 7, 10], [0, 4, 7, 11]]
    Minor7 = [[0, 3, 7, 10]]
    Diminished = [[0, 3, 6, 9]]

    def __init__(self, base_note: int, intervals: list[int], piano: Piano) -> None:
        self.base_key: Key = piano.keys[base_note]
        self.keys: list[Key] = [piano.keys[base_note+i] for i in intervals]

    def play_chord(self, color1='blue', color2=None, time_gap=0.5):
        def play(time_gap):
            for i, key in enumerate(self.keys):
                if i == 0:
                    key.play_key(color1, 3)
                else:
                    key.play_key(color2)
                sleep(time_gap)
        # thread = threading.Thread(target=play, args=(time_gap,)) # nie jestem pewny czy ten thread jest potrzebny
        # thread.start()
        play(time_gap)

    def random_chord(piano: Piano, **kwargs):
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
        if not chord_list:
            raise ValueError("At least one chord type must be selected.")
        intervals = random.choice(chord_list)
        chord_len = intervals[-1]
        base_note = random.randint(0, piano.key_num-chord_len-1)
        print(base_note, intervals)
        return Chord(base_note, intervals, piano)
