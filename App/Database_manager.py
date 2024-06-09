import firebase_admin
from firebase_admin import credentials, firestore


class DatabaseManager:
    def __init__(self, certificate_file):
        cred = credentials.Certificate(certificate_file)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()


    def see_if_username_exists (self, username):
        registered_user = self.db.collection('users').document(username)
        return registered_user.get().exists


    def add_user (self, username, mail, password):
        if self.see_if_username_exists(username):
            print("Username not unique")
        else:
            users = self.db.collection("users")
            users.document(username).set({
                "mail": mail,
                "password": password
            })
            interval_answers = self.db.collection("interval")
            interval_answers.document(username).set({
                "correct": 0,
                "incorrect": 0
            })
            chord_answers = self.db.collection("chord")
            chord_answers.document(username).set({
                "correct": 0,
                "incorrect": 0
            })


    def see_if_user_can_be_logged_in (self, username, password):
        user = self.db.collection("users").document(username)
        if not user.get().exists:
            return False
        else:
            user_data = user.get().to_dict()
            if user_data["password"] == password:
                return True
            else:
                return False


    def see_correct_ans_for_user_and_mode (self, username, mode):
        user_mode = self.db.collection(mode).document(username)
        user_mode_data = user_mode.get().to_dict()
        return user_mode_data["correct"]


    def see_incorrect_ans_for_user_and_mode (self, username, mode):
        user_mode = self.db.collection(mode).document(username)
        user_mode_data = user_mode.get().to_dict()
        return user_mode_data["incorrect"]


    def update_correct_ans (self, username, mode, new_correct):
        user_mode = self.db.collection(mode).document(username)
        new_user_mode_data = user_mode.get().to_dict()
        new_user_mode_data["correct"] = new_correct
        user_mode.update(new_user_mode_data)


    def update_incorrect_ans (self, username, mode, new_incorrect):
        user_mode = self.db.collection(mode).document(username)
        new_user_mode_data = user_mode.get().to_dict()
        new_user_mode_data["incorrect"] = new_incorrect
        user_mode.update(new_user_mode_data)





