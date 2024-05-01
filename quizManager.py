from questionHandler import questionHandler
from music_components.Piano import Piano
from gameModes.IntervalMode import IntervalMode
from gameModes.AbstractMode import AbstractMode
from gameModes.ChordMode import ChordMode


class quizManager: # for gamemode showcase
    def __init__(self, root, mode=0, time_gap=0.5, octaves=2, lowest_octave=3) -> None:
        self.handler = questionHandler()
        self.piano = Piano(root, octaves, lowest_octave)
        if mode == 0:
            self.gameMode: AbstractMode = IntervalMode(
                self.piano, time_gap=time_gap)
        elif mode == 1:
            self.gameMode: AbstractMode = ChordMode(
                self.piano, time_gap=time_gap, major=True, minor=True, major_rev=True, minor_rev=True, major7=True, minor7=True, diminished=True)
        self.handler.set_mode(self.gameMode)

    def play(self):
        self.handler.next_question()

max_listens = 3


class QuizManager: # for frontend
    def __init__ (self,game_mode_prompt,gamemode_menu_class):
        game_mode = None
        if game_mode_prompt == "Interval":
            game_mode = IntervalMode()
        self.question_handler = questionHandler(game_mode)
        self.piano = Piano(gamemode_menu_class.get_window(),2,2,self.question_handler)
        if game_mode is not None:
            game_mode.set_piano(self.piano)
        # self.question_handler.set_mode(game_mode)
        self.question_handler.set_current_quiz_manager(self)
        self.current_question = None
        self.gamemode_menu_class = gamemode_menu_class
        self.listens = 0
        self.__initialize_quiz_manager()


    def __initialize_quiz_manager (self):
        self.question_handler.next_question()


    def play_question (self):
        if self.listens < max_listens:
            self.question_handler.play_question()
            self.listens += 1
        else:
            raise Exception("You've listened enough times!")


    def get_question_duration (self):
        return self.question_handler.get_question_duration()


    def next_question (self):
        self.listens = 0
        self.question_handler.activate()
        self.question_handler.next_question()


    def listen_cap_met (self):
        return self.listens >= max_listens


    def get_remaining_listens (self):
        return max_listens - self.listens


    def question_passed (self):
        print(":)")
        self.question_handler.temporarily_deactivate()
        self.gamemode_menu_class.answered_correctly()


    def question_failed (self):
        print(":(")
        self.question_handler.temporarily_deactivate()
        self.gamemode_menu_class.answered_incorrectly()


    def update_window_after_new_question (self):
        self.listens = 0
        self.question_handler.activate()
        self.gamemode_menu_class.next_question_called_external()

