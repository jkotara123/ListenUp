import customtkinter as ctk
import json

with open("resources/music_data.json", "r") as f:
    music_data = json.load(f)
chord_names = music_data["chord_names"]
interval_names = music_data["interval_names"]


class GameModeSpecs:
    def __init__(self, prompt: str = None, number_of_notes_to_show: int = 1) -> None:
        self.prompt: str = prompt
        self._selected_types: set[str] = set()
        self._number_of_notes_to_show: ctk.IntVar = ctk.IntVar(
            value=number_of_notes_to_show
        )
        if self.prompt == "interval":
            self._time_gap = ctk.DoubleVar(value=0.4)
        else:
            self._time_gap = ctk.DoubleVar(value=0.2)
        self._time_gap_label: ctk.CTkLabel = None

    def set_prompt(self, new_prompt: str) -> None:
        self.prompt = new_prompt
        if self.prompt == "interval":
            self._time_gap = ctk.DoubleVar(value=0.4)
        else:
            self._time_gap = ctk.DoubleVar(value=0.2)
        self.reset()

    def contain(self, arg: str) -> bool:
        return arg in self._selected_types

    def add(self, arg: str) -> None:
        self._selected_types.add(arg)

    def remove(self, arg: str) -> None:
        if arg in self._selected_types:
            self._selected_types.remove(arg)

    def is_empty(self) -> bool:
        return len(self._selected_types) == 0

    def reset(self) -> None:
        self._selected_types.clear()

    def get_types(self) -> set[str]:
        return self._selected_types

    def get_number_of_notes_to_show(self) -> int:
        return self._number_of_notes_to_show.get()

    def get_time_gap(self) -> float:
        return self._time_gap.get()

    def time_gap_slider(self, root: ctk.CTk) -> ctk.CTkFrame:
        def update_time_gap_label(value):
            self._time_gap_label.configure(
                text=f"Inter-note interval: {self._time_gap.get():.2f}s"
            )

        panel = ctk.CTkFrame(master=root, fg_color="white")
        self._time_gap_label = ctk.CTkLabel(
            master=panel, text=f"Inter-note interval: {self._time_gap.get():.2f}s"
        )
        self._time_gap_label.grid(row=1, column=0, columnspan=4, pady=10)

        slider = ctk.CTkSlider(
            master=panel,
            from_=0.0,
            to=0.6,
            variable=self._time_gap,
            command=update_time_gap_label,
        )
        slider.grid(row=0, column=0, columnspan=4, pady=10)
        return panel

    def interval_setting_menu(self, root: ctk.CTk) -> ctk.CTkFrame:

        def all_command() -> None:
            if all_button.get() == "on":
                for i in range(len(interval_names)):
                    if interval_checkboxes[i].get() == "off":
                        interval_checkboxes[i].toggle()
            else:
                for i in range(len(interval_names)):
                    interval_checkboxes[i].toggle()

        def interval_command(i) -> None:
            if interval_checkboxes[i].get() == "on":
                self.add(interval_names[i])
            else:
                self.remove(interval_names[i])
                all_button.deselect()

        panel = ctk.CTkFrame(master=root, fg_color="white")
        num_rows = [4, 5, 4]
        index = 0
        interval_checkboxes = []

        for col, rows in enumerate(num_rows):
            for row in range(rows):
                checkbox = ctk.CTkCheckBox(
                    master=panel,
                    text=interval_names[index],
                    onvalue="on",
                    offvalue="off",
                    command=lambda i=index: interval_command(i),
                    checkbox_width=25,
                    checkbox_height=25,
                )
                checkbox.grid(row=row + 1, column=col, padx=10, pady=4, sticky="nsew")

                interval_checkboxes.append(checkbox)
                index += 1

        all_button = ctk.CTkCheckBox(
            master=panel,
            text="All",
            width=50,
            checkbox_height=25,
            checkbox_width=25,
            onvalue="on",
            offvalue="off",
            command=all_command,
        )

        all_button.grid(row=0, column=0, columnspan=3, pady=10)

        slider = self.time_gap_slider(panel)
        slider.grid(row=7, column=0, columnspan=4, pady=10)

        return panel

    def chord_setting_menu(self, root: ctk.CTk) -> ctk.CTkFrame:
        def chord_command(i: int) -> None:
            if checkboxes[i].get() == "on":
                self.add(chord_names[i])
            else:
                self.remove(chord_names[i])
                if i < 5:
                    major_button.deselect()
                else:
                    minor_button.deselect()

        def major_command(mode: str) -> None:
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

        panel = ctk.CTkFrame(master=root, fg_color="white")
        num_rows = [3, 2, 3, 2]
        index = 0
        checkboxes = []
        for col, rows in enumerate(num_rows):
            for row in range(rows):
                checkbox = ctk.CTkCheckBox(
                    master=panel,
                    text=chord_names[index],
                    onvalue="on",
                    offvalue="off",
                    command=lambda i=index: chord_command(i),
                )
                checkbox.grid(row=row + 3, column=col, padx=10, pady=5, sticky="nsew")
                checkboxes.append(checkbox)
                index += 1
        major_button = ctk.CTkCheckBox(
            master=panel,
            text="All major",
            onvalue="on",
            offvalue="off",
            command=lambda mode="major": major_command(mode),
        )
        major_button.grid(row=2, column=0, pady=5, columnspan=2, sticky="ns")

        minor_button = ctk.CTkCheckBox(
            master=panel,
            text="All minor",
            onvalue="on",
            offvalue="off",
            command=lambda mode="minor": major_command(mode),
        )
        minor_button.grid(row=2, column=2, pady=5, columnspan=2, sticky="ns")

        options = ["1", "2", "3"]

        option_menu_label = ctk.CTkLabel(panel, text="Notes to show:")
        option_menu_label.grid(row=0, column=0, columnspan=4, pady=5, sticky="ns")
        option_menu = ctk.CTkOptionMenu(
            master=panel, values=options, variable=self._number_of_notes_to_show
        )
        option_menu.grid(row=1, column=0, columnspan=4, pady=5, sticky="ns")

        slider = self.time_gap_slider(panel)
        slider.grid(row=7, column=0, columnspan=4, pady=10)

        return panel

    def create_setting_menu(self, root: ctk.CTk) -> ctk.CTkFrame:
        if self.prompt == "chord":
            return self.chord_setting_menu(root)
        elif self.prompt == "interval":
            return self.interval_setting_menu(root)
