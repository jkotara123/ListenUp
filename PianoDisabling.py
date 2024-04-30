class PianoDisabler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self.__initialized:
            return
        self.currently_enabled = True
        self.piano = None


    def set_piano (self,piano):
        self.piano = piano


    def disable_piano (self):
        self.currently_enabled = False
        # if self.piano is not None:
        #     self.piano.temporarily_disable_piano()


    def enable_piano (self):
        self.currently_enabled = True
        # if self.piano is not None:
        #     self.piano.enable_piano_again()



    def is_enabled (self):
        return self.currently_enabled
