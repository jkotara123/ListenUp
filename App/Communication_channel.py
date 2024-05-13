from Piano_manager import PianoManager
from Question_handler import QuestionHandler
from Quiz_manager import QuizManager


class CommunicationChannel:
    def __init__(self):
        self.menu = None
        self.quiz_manager = None

    def set_menu(self, menu):
        self.menu = menu

    def create_quiz_manager(self, prompt, piano, max_listens, game_mode_specs):
        piano_manager = PianoManager(piano)
        piano.set_piano_manager(piano_manager)
        question_handler = QuestionHandler(prompt, piano.get_number_of_octaves(
        ), piano.get_lowest_octave(), game_mode_specs=game_mode_specs)
        self.quiz_manager = QuizManager(
            self, question_handler, piano_manager, max_listens)

    def answered_correctly(self):
        self.menu.answered_correctly()

    def answered_incorrectly(self):
        self.menu.answered_incorrectly()

    def play_question(self):
        self.quiz_manager.play_question()

    def create_new_question(self):
        self.quiz_manager.create_new_question()

    def show_correct_answer(self):
        self.quiz_manager.show_correct_answer()
