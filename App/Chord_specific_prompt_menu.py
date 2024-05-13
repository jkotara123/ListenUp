from Specific_quiz_prompts import SpecificQuizPrompts
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


other_resources_path = "Other_Resources"
fontname = "Lithos Pro Regular"


checkbox_specs = [["major7", "major", "major_rev"],
                  ["minor7", "minor", "minor_rev"],
                  [None, "diminished", None]]


def get_ch_box_max_col ():
    sought = 0
    for row in checkbox_specs:
        sought = max(sought, len(row))

    return sought



def set_root_specs (root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class SpecificChordPromptMenu:
    def __int__(self, root, launch_immediately=True):
        if get_ch_box_max_col() > 4:
            raise Exception("Jak dasz więcej niż cztery kolumny to będzie brzydko wyglądać")
        self.menu_frame = None
        self.specific_quiz_prompts = SpecificQuizPrompts()
        self.checkbox_values = {}
        self.__prepare_menu(root)
        if launch_immediately:
            self.menu_frame.winfo_toplevel().mainloop()


    def __go_back (self):
        self.menu_frame.winfo_toplevel().quit()


    def __start_quiz (self):
        ...


    def __prepare_menu (self, root):
        window_width = 300
        window_height = 300
        button_width = 30
        button_height = 10

        set_root_specs(root, 300, 300)
        menu_frame = ctk.CTkFrame(master=root, width=window_width, height=window_height)
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(f"{other_resources_path}/mm_background.png"), size=(window_width, window_height))
        bg_image_label = ctk.CTkLabel(master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        go_back_button = ctk.CTkButton(master=menu_frame, text="Go back", font=(fontname, 14),
                                       width=button_width, height=button_height, fg_color="white",
                                       hover_color="grey", text_color="black", corner_radius=32,
                                       border_width=2, command=self.__go_back)
        go_back_button.place(relx=0.02, rely=0.02, anchor=ctk.CENTER)

        start_quiz_button = ctk.CTkButton(master=menu_frame, text="Go back", font=(fontname, 14),
                                          width=button_width, height=button_height, fg_color="white",
                                          hover_color="grey", text_color="black", corner_radius=32,
                                          border_width=2, command=self.__start_quiz)
        start_quiz_button.place(relx=0.02, rely=0.02, anchor=ctk.CENTER)


