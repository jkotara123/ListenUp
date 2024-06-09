from Database_manager import DatabaseManager


class UsersAssignedStatistician:
    def __init__(self, user, database_manager):
        self.database_manager = database_manager
        self.user = user
        self.current_mode = None


    def set_current_mode (self, mode):
        self.current_mode = mode


    def increment_correct (self):
        old_correct = self.database_manager.see_correct_ans_for_user_and_mode(self.user, self.current_mode)
        new_correct = old_correct+1
        self.database_manager.update_correct_ans(self.user, self.current_mode, new_correct)


    def increment_incorrect (self):
        old_incorrect = self.database_manager.see_incorrect_ans_for_user_and_mode(self.user, self.current_mode)
        new_incorrect = old_incorrect+1
        self.database_manager.update_incorrect_ans(self.user, self.current_mode, new_incorrect)
