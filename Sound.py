# import pygame


note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

sound_file_map = {
    28: "Piano_sounds/3-c.wav",
    29: "Piano_sounds/3-cs.wav",
    30: "Piano_sounds/3-d.wav",
    31: "Piano_sounds/3-ds.wav",
    32: "Piano_sounds/3-e.wav",
    33: "Piano_sounds/3-f.wav",
    34: "Piano_sounds/3-fs.wav",
    35: "Piano_sounds/3-g.wav",
    36: "Piano_sounds/3-gs.wav",
    37: "Piano_sounds/3-a.wav",
    38: "Piano_sounds/3-as.wav",
    39: "Piano_sounds/3-b.wav",
    40: "Piano_sounds/4-c.wav",
    41: "Piano_sounds/4-cs.wav",
    42: "Piano_sounds/4-d.wav",
    43: "Piano_sounds/4-ds.wav",
    44: "Piano_sounds/4-e.wav",
    45: "Piano_sounds/4-f.wav",
    46: "Piano_sounds/4-fs.wav",
    47: "Piano_sounds/4-g.wav",
    48: "Piano_sounds/4-gs.wav",
    49: "Piano_sounds/4-a.wav",
    50: "Piano_sounds/4-as.wav",
    51: "Piano_sounds/4-b.wav",
}


class Sound:
    def __init__(self, sound_identifier):
        self.sound_identifier = sound_identifier

    def get_frequency(self):
        return self.frequency

    def play_sound(self):
        sound_path = sound_file_map[self.sound_identifier]
        # playable = pygame.mixer.Sound(sound_path)
        # playable.play()
