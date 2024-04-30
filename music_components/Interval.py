from music_components.Key import Key
from music_components.Piano import Piano
import threading
import random
from time import sleep


class Interval:
    def __init__(self, base: int, interval, piano: Piano) -> None:
        self.base: Key = piano.keys[base]
        self.second: Key = piano.keys[base+interval]

    def play_interval(self, color1='blue', color2=None, time_gap=0.5):
        def play(time_gap):
            self.base.play_key(color1, 3)
            sleep(time_gap)
            self.second.play_key(color2)
        # thread = threading.Thread(target=play, args=(time_gap,))      # nie jestem pewny czy ten thread jest potrzebny
        # thread.start()
        play(time_gap)

    def random_interval(piano: Piano):
        interval = random.randint(-11, 11)
        base_note = random.randint(
            0, piano.key_num-interval-1) if interval >= 0 else random.randint(interval, piano.key_num-1)
        print(base_note, interval)
        return Interval(base_note, interval, piano)
