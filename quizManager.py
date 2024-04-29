from questionHandler import questionHandler


max_listens = 3


class QuizManager:
    def __init__ (self,game_mode,piano,gamemode_menu_class):
        self.piano = piano
        self.question_handler = questionHandler()
        self.question_handler.set_mode(game_mode)
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
        self.question_handler.next_question()


    def listen_cap_met (self):
        return self.listens >= max_listens


    def get_remaining_listens (self):
        return max_listens - self.listens


    def question_passed (self):
        print(":)")
        self.gamemode_menu_class.display_tick()


    def question_failed (self):
        print(":(")
        self.gamemode_menu_class.display_cross()
