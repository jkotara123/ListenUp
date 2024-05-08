import random


note_names = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


def corresponds_to_base (note_name, base):
    return note_name == base[:-1]


def create_random_note (octaves, lowest_octave, base=None, span=None):
    if base is None:
        random_name = random.choice(note_names)
        random_octave = random.randint(lowest_octave, lowest_octave+octaves-1)
        random_note_name = random_name+str(random_octave)
    else:
        i = 0
        base_octave = int(base[-1])
        for i in range (0, len(note_names)):
            if corresponds_to_base(note_names[i], base):
                break
            i += 1
        x = random.randint(-span, span)
        random_octave = base_octave + int((i+x)//len(note_names))
        if random_octave < lowest_octave:
            random_name = note_names[0]
            random_octave = lowest_octave
        elif random_octave >= lowest_octave+octaves:
            random_name = note_names[-1]
            random_octave = lowest_octave+octaves-1
        else:
            random_name = note_names[(i+x) % len(note_names)]
        random_note_name = random_name+str(random_octave)

    return random_note_name

