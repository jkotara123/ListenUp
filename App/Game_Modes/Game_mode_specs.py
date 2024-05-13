import customtkinter as ctk

chord_names = ["Major root", "Major 1st inv.",
               "Major 2nd inv.", "Dominant 7th", "Maj7",
               "Minor root", "Minor 1st inv.",
               "Minor 2nd inv.", "Minor7", "Diminished"]

interval_names = ["Unison", "Minor second", "Major second", "Minor third", "Major third", "Perfect fourth",
                  "Tritone", "Perfect fifth", "Minor sixth", "Major sixth", "Minor seventh", "Major seventh", "Octave"]


class Game_mode_specs():
    def __init__(self, prompt=None, number_of_notes_to_show=1):
        self.prompt = prompt
        self._selected_types = set()
        self._number_of_notes_to_show = number_of_notes_to_show

    def set_prompt(self, new_prompt):
        self.prompt = new_prompt
        self.reset()

    def contain(self, arg):
        return arg in self._selected_types

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

    def interval_setting_menu(self, root):

        def all_command():
            if all_button.get() == "on":
                for i in range(len(interval_names)):
                    if interval_checkboxes[i].get() == "off":
                        interval_checkboxes[i].toggle()
            else:
                for i in range(len(interval_names)):
                    interval_checkboxes[i].toggle()

        def interval_command(i):
            if interval_checkboxes[i].get() == "on":
                self.add(interval_names[i])
            else:
                self.remove(interval_names[i])
                all_button.deselect()

        panel = ctk.CTkFrame(root)
        num_rows = [4, 5, 4]
        index = 0
        interval_checkboxes = []

        for col, rows in enumerate(num_rows):
            for row in range(rows):
                checkbox = ctk.CTkCheckBox(
                    panel, text=interval_names[index],
                    onvalue="on", offvalue="off",
                    command=lambda i=index: interval_command(i),
                    checkbox_width=25,
                    checkbox_height=25
                )
                checkbox.grid(row=row+1, column=col,
                              padx=10, pady=4, sticky="nsew")

                interval_checkboxes.append(checkbox)
                index += 1

        all_button = ctk.CTkCheckBox(
            panel, text="All", width=50,
            checkbox_height=25, checkbox_width=25,
            onvalue="on", offvalue="off",
            command=all_command)

        all_button.grid(row=0, column=0, columnspan=3, pady=10)
        return panel

    def chord_setting_menu(self, root):
        def chord_command(i):
            if checkboxes[i].get() == "on":
                self.add(chord_names[i])
            else:
                self.remove(chord_names[i])
                if i < 5:
                    major_button.deselect()
                else:
                    minor_button.deselect()

        def major_command(mode):
            if mode == "major":
                state = major_button.get()
                rng = range(5)
            else:
                state = minor_button.get()
                rng = range(5, 10)
            if state == "on":
                for i in rng:
                    if checkboxes[i].get() == "off":
                        checkboxes[i].toggle()
            else:
                for i in rng:
                    checkboxes[i].toggle()

        panel = ctk.CTkFrame(root)
        num_rows = [3, 2, 3, 2]
        index = 0
        checkboxes = []
        for col, rows in enumerate(num_rows):
            for row in range(rows):
                checkbox = ctk.CTkCheckBox(
                    panel, text=chord_names[index],
                    onvalue="on", offvalue="off",
                    command=lambda i=index: chord_command(i)
                )
                checkbox.grid(row=row+2, column=col,
                              padx=10, pady=5, sticky="nsew")
                checkboxes.append(checkbox)
                index += 1
        major_button = ctk.CTkCheckBox(
            panel, text="All major",
            onvalue="on", offvalue="off",
            command=lambda mode="major": major_command(mode))
        major_button.grid(row=1, column=0,
                          pady=5, columnspan=2, sticky="ns")

        minor_button = ctk.CTkCheckBox(
            panel, text="All minor",
            onvalue="on", offvalue="off",
            command=lambda mode="minor": major_command(mode))
        minor_button.grid(row=1, column=2,
                          pady=5, columnspan=2, sticky="ns")
        return panel


root = ctk.CTk()
root.geometry('700x450')
a = Game_mode_specs()
select_menu = a.chord_setting_menu(root)
select_menu.pack(pady=20)

root.mainloop()
