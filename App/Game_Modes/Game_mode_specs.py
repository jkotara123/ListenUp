class Game_mode_specs():
    def __init__(self, prompt=None, number_of_notes_to_show=1):
        self.prompt = prompt
        self._selected_types = set()
        self._number_of_notes_to_show = number_of_notes_to_show

    def set_prompt(self, new_prompt):
        self.prompt = new_prompt
        self.reset()

    def add(self, arg):
        self._selected_types.add(arg)

    def remove(self, arg):
        if arg in self._selected_types:
            self._selected_types.remove(arg)

    def is_empty(self):
        return len(self._selected_types) == 0

    def reset(self):
        self._selected_types.clear()

    def get_types(self):
        return self._selected_types

    def get_number_of_notes_to_show(self):
        return self._number_of_notes_to_show
