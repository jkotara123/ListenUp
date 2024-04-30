from gameModes.AbstractMode import AbstractMode


class questionHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self.__initialized:
            return
        self.answer = []
        self.answer_index = 0
        self.expected = []
        self.gameMode: AbstractMode = None
        self.__initialized = True
        self.question_count = 0

    def set_mode(self, gameMode: AbstractMode):
        self.gameMode: AbstractMode = gameMode

    def next_question(self):
        self.question_count += 1
        self.expected = self.gameMode.get_new_question()
        self.__clear_answer_buff()
        print("New question!\n")
        self.play_question()
        print(self.expected, self.answer)

    def check_answer(self, key):
        if len(self.expected) == 0:
            return 2
        self.answer.append(key)
        if self.answer == self.expected:  # calkowicie poprawna odpowiedz -> klawisz na zielono
            print("Correct!")
            return 1
        # zla odpowiedz -> klawisz na czerwono
        if key != self.expected[self.answer_index]:
            print("Incorrect!")
            return 0
        self.answer_index += 1
        return -1  # dobra odpowiedz -> klawisz na zielono

    def play_question(self):
        self.gameMode.play_question()

    def __clear_answer_buff(self):
        self.answer.clear()
        self.answer_index = 0
