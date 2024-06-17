import firebase_admin
from firebase_admin import credentials, firestore
import hashlib


class DatabaseManager:
    def __init__(self, certificate_file: str) -> None:
        cred = credentials.Certificate(certificate_file)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def see_if_username_exists(self, username: str) -> bool:
        registered_user = self.db.collection("users").document(username)
        return registered_user.get().exists

    def add_user(self, username: str, mail: str, password: str) -> None:
        if not self.see_if_username_exists(username):
            users = self.db.collection("users")
            hash_object = hashlib.sha256()
            hash_object.update(password.encode('utf-8'))
            hashed_hex_password = hash_object.hexdigest()
            users.document(username).set({"mail": mail, "password": hashed_hex_password})
            interval_answers = self.db.collection("interval")
            interval_answers.document(username).set({"correct": 0, "incorrect": 0})
            chord_answers = self.db.collection("chord")
            chord_answers.document(username).set({"correct": 0, "incorrect": 0})

    def see_if_user_can_be_logged_in(self, username: str, password: str) -> bool:
        user = self.db.collection("users").document(username)
        if not user.get().exists:
            return False
        else:
            hash_object = hashlib.sha256()
            hash_object.update(password.encode('utf-8'))
            hashed_hex_password = hash_object.hexdigest()
            user_data = user.get().to_dict()
            if user_data["password"] == hashed_hex_password:
                return True
            else:
                return False

    def get_users_mail_address(self, username: str) -> str:
        user = self.db.collection("users").document(username)
        if not user.get().exists:
            return None
        else:
            return user.get().to_dict()["mail"]

    def check_users_password(self, username: str, password: str) -> bool:
        user = self.db.collection("users").document(username)
        hash_object = hashlib.sha256()
        hash_object.update(password.encode('utf-8'))
        hashed_hex_password = hash_object.hexdigest()
        if not user.get().exists:
            return False
        elif user.get().to_dict()["password"] != hashed_hex_password:
            return False
        else:
            return True

    def reset_users_password(self, username: str, new_password: str) -> None:
        user = self.db.collection("users").document(username)
        if user.get().exists:
            new_user_data = user.get().to_dict()
            hash_object = hashlib.sha256()
            hash_object.update(new_password.encode('utf-8'))
            hashed_hex_new_password = hash_object.hexdigest()
            new_user_data["password"] = hashed_hex_new_password
            user.set(new_user_data)

    def see_correct_ans_for_user_and_mode(self, username: str, mode: str) -> int:
        user_mode = self.db.collection(mode).document(username)
        user_mode_data = user_mode.get().to_dict()
        return user_mode_data["correct"]

    def see_incorrect_ans_for_user_and_mode(self, username: str, mode: str) -> int:
        user_mode = self.db.collection(mode).document(username)
        user_mode_data = user_mode.get().to_dict()
        return user_mode_data["incorrect"]

    def update_correct_ans(self, username: str, mode: str, new_correct: int) -> int:
        user_mode = self.db.collection(mode).document(username)
        new_user_mode_data = user_mode.get().to_dict()
        new_user_mode_data["correct"] = new_correct
        user_mode.update(new_user_mode_data)

    def update_incorrect_ans(self, username: str, mode: str, new_incorrect: int) -> int:
        user_mode = self.db.collection(mode).document(username)
        new_user_mode_data = user_mode.get().to_dict()
        new_user_mode_data["incorrect"] = new_incorrect
        user_mode.update(new_user_mode_data)

