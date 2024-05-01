from abc import ABC, abstractmethod


class AbstractMode(ABC):
    @abstractmethod
    def play_question(self):
        pass

    @abstractmethod
    def get_new_question(self):
        pass

    @abstractmethod
    def show_question(self):
        pass
