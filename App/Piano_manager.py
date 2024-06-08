from time import sleep
import threading


class PianoManager:
    def __init__ (self, piano, parent=None):
        self.piano = piano
        piano.set_piano_manager(self)
        self.parent = parent


    def enable (self):
        self.piano.enable()


    def disable (self):
        self.piano.disable()


    def set_parent (self, parent):
        self.parent = parent


    def set_key_color (self, note_name, color):
        self.piano.set_key_color(note_name, color)


    def set_all_reds (self):
        self.piano.set_all_reds()


    def key_was_clicked (self, note_name):
        self.parent.check_answer(note_name)


    def play_sequence (self, sequence, to_show, expected, one_left, time_gaps, add_greens=None):

        def internal_play_sequence ():
            j = 0
            k = 0
            for i in range (0, len(sequence)):
                note_name = sequence[i]
                if j < len(to_show) and to_show[j] == i:
                    self.set_key_color(note_name, "blue")
                    j += 1
                elif add_greens is None:
                    self.set_key_color(note_name, None)
                else:
                    if k < len(add_greens) and add_greens[k] == i:
                        self.set_key_color(note_name, "green")
                        k += 1
                    if i == len(sequence)-1:
                        self.set_key_color(note_name, "gold")
                self.piano.play_key(note_name)

                if i != len(sequence)-1:
                    sleep(time_gaps[i])

            for note_name in sequence:
                self.set_key_color(note_name, "red")
            if expected is not None:
                if one_left:
                    self.set_key_color(expected, "gold")
                else:
                    self.set_key_color(expected, "green")

        play_thread = threading.Thread(target=internal_play_sequence)
        play_thread.start()


    def destroy_piano (self):
        self.piano.destroy_piano()

