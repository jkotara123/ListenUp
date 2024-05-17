class QuizManager:
    def __init__(self, menu_comm_channel, question_handler, piano_manager, max_listens):
        self.menu_comm_channel = menu_comm_channel
        self.question_handler = question_handler
        self.piano_manager = piano_manager
        self.max_listens = max_listens
        self.listens = 0
        piano_manager.set_parent(self)
        self.create_new_question()

    def create_new_question(self):
        self.piano_manager.disable()
        self.listens = 0
        self.question_handler.create_new_question()
        self.piano_manager.set_all_reds()
        if self.question_handler.one_left():
            self.piano_manager.set_key_color(
                self.question_handler.get_expected(), "gold")
        else:
            self.piano_manager.set_key_color(
                self.question_handler.get_expected(), "green")
        self.piano_manager.enable()


    def destroy_piano (self):
        self.piano_manager.destroy_piano()


    def show_correct_answer(self):
        self.piano_manager.disable()
        to_show = self.question_handler.get_question_start()
        sequence = self.question_handler.get_question()
        # expected = self.question_handler.get_expected()
        one_left = self.question_handler.one_left()
        time_gaps = self.question_handler.get_time_gaps()
        add_greens = []
        k = 0
        for i in range(0, len(sequence)):
            if k < len(to_show) and to_show[k] == i:
                k += 1
            else:
                add_greens.append(i)
        self.piano_manager.play_sequence(
            sequence, to_show, expected=None, one_left=one_left, time_gaps=time_gaps, add_greens=add_greens)
        # self.listens += 1
        self.piano_manager.enable()

    def play_question(self):
        if self.listens < self.max_listens:
            self.piano_manager.disable()
            to_show = self.question_handler.get_question_start()
            sequence = self.question_handler.get_question()
            expected = self.question_handler.get_expected()
            one_left = self.question_handler.one_left()
            time_gaps = self.question_handler.get_time_gaps()
            self.piano_manager.play_sequence(
                sequence, to_show, expected, one_left, time_gaps)
            self.listens += 1
            self.piano_manager.enable()
        else:
            raise Exception("You listened enough times")

    def check_answer(self, note_name):
        self.piano_manager.disable()
        message = self.question_handler.check_answer(note_name)
        self.piano_manager.set_key_color(
            self.question_handler.get_previously_expected(), "red")
        if message == "So far correct":
            if self.question_handler.one_left():
                self.piano_manager.set_key_color(
                    self.question_handler.get_expected(), "gold")
            else:
                self.piano_manager.set_key_color(
                    self.question_handler.get_expected(), "green")
            self.piano_manager.enable()
        elif message == "Incorrect":
            self.piano_manager.disable()
            self.menu_comm_channel.answered_incorrectly()
        else:
            self.piano_manager.disable()
            self.menu_comm_channel.answered_correctly()
