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
        self.answer = set()
        self.expected = set()
        self.gameMode = None
        self.__initialized = True
        self.question_count = 0

    def set_mode(self, gameMode):
        self.gameMode = gameMode

    def next_question(self):
        if self.question_count == 5:
            print("Koniec gry!")
            self.expected.clear()
        else:
            self.question_count += 1
            self.expected = self.gameMode.get_new_question()
            self.__clear_answer_buff()
            print("New question!\n")
            print(self.expected, self.answer)
            self.play_question()

    def check_answer(self, key):
        print(self.expected)
        if len(self.expected) == 0:
            return 2
        self.answer.add(key)
        if self.answer == self.expected:  # calkowicie poprawna odpowiedz -> klawisz na zielono
            print("Correct")
            return 1
        for ans in self.answer:
            if ans not in self.expected:  # zla odpowiedz -> klawisz na czerwono
                print("Incorrect")
                return 0
        return -1  # dobra odpowiedz -> klawisz na zielono

    def play_question(self):
        self.gameMode.play_question()

    def __clear_answer_buff(self):
        self.answer = set()
