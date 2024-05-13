import random


class SpecificQuizPrompts:
    def __int__(self):
        self.interval_spans = set()
        self.interval_skeletons = set()

        self.chord_skeletons = set()


    def add_interval_span (self, span):
        self.interval_spans.add(span)


    def remove_interval_span (self, span):
        self.interval_spans.remove(span)


    def contains_interval_span (self, span):
        return span in self.interval_spans


    def get_random_interval_span (self):
        try:
            random_span = random.choice(self.interval_spans)
        except IndexError:
            random_span = None
        return random_span


    def add_interval_skeleton (self, skeleton):
        self.interval_skeletons.add(skeleton)


    def remove_interval_skeleton (self, skeleton):
        self.remove_interval_skeleton(skeleton)


    def contains_interval_skeleton (self, skeleton):
        return skeleton in self.interval_skeletons


    def get_random_interval_skeleton (self):
        try:
            random_span = random.choice(self.interval_skeletons)
        except IndexError:
            random_span = None
        return random_span


    def add_chord_skeleton (self, skeleton):
        self.chord_skeletons.add(skeleton)


    def remove_chord_skeleton (self, skeleton):
        self.chord_skeletons.remove(skeleton)


    def contains_chord_skeleton (self, skeleton):
        return skeleton in self.chord_skeletons
