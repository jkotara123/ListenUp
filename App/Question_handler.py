from Music_Components.Interval import Interval
from Music_Components.Chord import Chord

modes = {"Interval": Interval, "Chord": Chord}


class QuestionHandler:
    def __init__(self, prompt, octaves, lowest_octave):
        self.octaves = octaves
        self.lowest_octave = lowest_octave
        self.prompt = prompt
        self.question = None
        self.index = 0

    def create_new_question(self):
        if self.prompt == "Chord":
            self.question = modes[self.prompt](
                self.octaves, self.lowest_octave, create_random=True, major=True, major=True, major_rev=True, minor=True, minor=True, minor_rev=True, diminished=True)
        else:
            self.question = modes[self.prompt](
                self.octaves, self.lowest_octave, create_random=True)
        print(self.question.get_sequence())
        self.index = 0

    def get_expected(self):
        return self.question.get_expected(self.index)

    def get_previously_expected(self):
        return self.question.get_expected(self.index-1)

    def get_question_start(self):
        return self.question.get_to_show()

    def get_question(self):
        return self.question.get_sequence()

    def get_time_gaps(self):
        return self.question.get_time_gaps()

    def one_left(self):
        return self.index+1 == self.question.size()

    def check_answer(self, note_name):
        # print(self.get_expected(), self.index)
        if self.get_expected() == note_name:
            self.index += 1
            if self.index < self.question.size():
                return "So far correct"
            else:
                return "Fully correct"
        else:
            return "Incorrect"
