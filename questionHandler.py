class questionHandler:
    # _instance = None
    #
    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         cls._instance.__initialized = False
    #     return cls._instance

    def __init__(self, game_mode = None) -> None:
        # if self.__initialized:
        #     return
        self.answer = set()
        self.expected = set()
        self.gameMode = game_mode
        # self.__initialized = True
        self.question_count = 0
        self.current_quiz_manager = None
        self.currently_active = True

    def set_mode(self, gameMode):
        self.gameMode = gameMode


    def temporarily_deactivate (self):
        self.currently_active= False


    def activate (self):
        self.currently_active = True


    def is_active (self):
        return self.currently_active


    def set_current_quiz_manager (self,quiz_manager):
        self.current_quiz_manager = quiz_manager


    def next_question(self):
        self.question_count += 1
        self.expected = self.gameMode.get_new_question()
        self.__clear_answer_buff()
        #self.current_quiz_manager.update_window_after_new_question()
        print("New question!\n")
        print(self.expected, self.answer)
        # self.play_question()


    def get_question_duration (self):
        return 1

    def check_answer(self, key):
        print(self.expected)
        if len(self.expected) == 0:
            return 2
        self.answer.add(key)
        if self.answer == self.expected:  # calkowicie poprawna odpowiedz -> klawisz na zielono
            print("Correct")
            if self.current_quiz_manager is not None:
                self.current_quiz_manager.question_passed()
            return 1
        for ans in self.answer:
            if ans not in self.expected:  # zla odpowiedz -> klawisz na czerwono
                print("Incorrect")
                if self.current_quiz_manager is not None:
                    self.current_quiz_manager.question_failed()
                return 0
        return -1  # dobra odpowiedz -> klawisz na zielono

    def play_question(self):
        self.gameMode.play_question()

    def __clear_answer_buff(self):
        self.answer = set()
