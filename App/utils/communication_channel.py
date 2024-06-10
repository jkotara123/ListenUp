from .piano_manager import PianoManager
from .question_handler import QuestionHandler
from .quiz_manager import QuizManager
from music_components import Piano
from game_modes import GameModeSpecs


class CommunicationChannel:
    def __init__(self) -> None:
        self.menu = None
        self.quiz_manager = None

    def set_menu(self, menu) -> None:
        self.menu = menu

    def create_quiz_manager(
        self,
        prompt: str,
        piano: Piano,
        max_listens: int,
        game_mode_specs: GameModeSpecs,
    ) -> None:
        piano_manager = PianoManager(piano)
        piano.set_piano_manager(piano_manager)
        question_handler = QuestionHandler(
            prompt,
            piano.get_number_of_octaves(),
            piano.get_lowest_octave(),
            game_mode_specs=game_mode_specs,
        )
        self.quiz_manager = QuizManager(
            self, question_handler, piano_manager, max_listens
        )

    def answered_correctly(self) -> None:
        self.menu.answered_correctly()

    def answered_incorrectly(self) -> None:
        self.menu.answered_incorrectly()

    def play_question(self) -> None:
        self.quiz_manager.play_question()

    def create_new_question(self) -> None:
        self.quiz_manager.create_new_question()

    def show_correct_answer(self) -> None:
        self.quiz_manager.show_correct_answer()

    def destroy_piano(self) -> None:
        self.quiz_manager.destroy_piano()
