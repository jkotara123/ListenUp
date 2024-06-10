import customtkinter as ctk
import json
from PIL import Image


with open("resources/config.json", "r") as f:
    config = json.load(f)
fontname = config["fontname"]
images_path = config["paths"]["images_path"]


def set_root_specs(root, width, height):
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)
    root.attributes("-fullscreen", False)


class SettingsMenu:
    def __init__(self, root: ctk.CTk, launch_immediately: bool = True) -> None:
        self.root: ctk.CTk = root
        self.menu_frame: ctk.CTkFrame = None
        self.measure_time: bool = False
        self.time: int = 0
        self.measure_time_checkbox: ctk.CTkCheckBox = None
        self.time_entry: ctk.CTkEntry = None
        if launch_immediately:
            self.__prepare_menu(root)
            root.mainloop()

    def get_measure_time(self) -> bool:
        return self.measure_time

    def get_time(self) -> int:
        return self.time

    def __update_measure_time(self) -> None:
        if self.measure_time_checkbox.get() == 0:
            self.measure_time = False
        else:
            self.measure_time = True

    def launch_manually(self) -> None:
        self.__prepare_menu(self.root)
        self.menu_frame.winfo_toplevel().mainloop()

    def __go_back(self) -> None:
        try:
            self.time = int(self.time_entry.get())
        except ValueError:
            return None
        self.menu_frame.pack_forget()
        self.menu_frame.winfo_toplevel().quit()

    def __prepare_menu(self, root) -> None:
        width = 500
        height = 500

        set_root_specs(root, width, height)
        menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(
            light_image=Image.open(f"{images_path}/mm_background.png"),
            size=(width, height),
        )
        bg_image_label = ctk.CTkLabel(master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        timer_label = ctk.CTkLabel(
            master=menu_frame,
            text_color="black",
            text="Please specify your\ntime restriction measurements",
            font=(fontname, 20),
            fg_color="white",
            width=width * 0.1,
            height=height * 0.1,
        )
        timer_label.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        measure_time_at_all_checkbox = ctk.CTkCheckBox(
            master=menu_frame,
            width=24,
            height=24,
            corner_radius=32,
            border_width=2,
            onvalue=1,
            offvalue=0,
            bg_color="white",
            checkmark_color="white",
            text="Do you wish for there to be a timer at all?",
            command=self.__update_measure_time,
        )
        measure_time_at_all_checkbox.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)
        self.measure_time_checkbox = measure_time_at_all_checkbox

        measure_time_text_entry = ctk.CTkEntry(
            master=menu_frame,
            width=width * 0.35,
            height=10,
            border_width=2,
            border_color="black",
            fg_color="white",
            text_color="black",
            font=(fontname, 14),
            placeholder_text="Here specify how long the timer should be",
            placeholder_text_color="black",
        )
        measure_time_text_entry.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
        self.time_entry = measure_time_text_entry

        go_back_button = ctk.CTkButton(
            master=menu_frame,
            width=width * 0.1,
            height=10,
            border_width=2,
            border_color="black",
            fg_color="white",
            text_color="black",
            text="Save and go back",
            font=(fontname, 14),
            hover_color="grey",
            command=self.__go_back,
        )
        go_back_button.place(relx=0.15, rely=0.05, anchor=ctk.CENTER)
