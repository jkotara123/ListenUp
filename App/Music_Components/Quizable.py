import abc


class Quizable(abc.ABC):
    @abc.abstractmethod
    def get_time_gaps(self):
        pass

    @abc.abstractmethod
    def get_to_show(self):
        pass

    @abc.abstractmethod
    def get_expected(self, i):
        pass

    @abc.abstractmethod
    def get_sequence(self):
        pass

    @abc.abstractmethod
    def size(self):
        pass
