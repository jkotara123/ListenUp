from abc import ABC, abstractmethod


class abstractMode(ABC):
    @abstractmethod
    def play_question(self):
        pass

    @abstractmethod
    def get_new_question(self):
        pass
