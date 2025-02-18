from .database_manager import DatabaseManager


class UsersAssignedStatistician:
    def __init__(self, user, database_manager) -> None:
        self.database_manager = database_manager
        self.user = user
        self.current_mode = None

    def set_current_mode(self, mode) -> None:
        self.current_mode = mode

    def get_user(self) -> str:
        return self.user

    def reset_password(self, new_password) -> None:
        self.database_manager.reset_users_password(self.user, new_password)

    def check_password(self, password) -> bool:
        return self.database_manager.check_users_password(self.user, password)

    def increment_correct(self) -> None:
        old_correct = self.database_manager.see_correct_ans_for_user_and_mode(
            self.user, self.current_mode
        )
        new_correct = old_correct + 1
        self.database_manager.update_correct_ans(
            self.user, self.current_mode, new_correct
        )

    def increment_incorrect(self) -> None:
        old_incorrect = self.database_manager.see_incorrect_ans_for_user_and_mode(
            self.user, self.current_mode
        )
        new_incorrect = old_incorrect + 1
        self.database_manager.update_incorrect_ans(
            self.user, self.current_mode, new_incorrect
        )
