import customtkinter as ctk
import pygame
from PIL import Image

from Interval_game_mode_menu import IntervalGameModeMenu
from Chord_game_mode_menu import ChordGameModeMenu
from Game_Modes.Game_mode_specs import Game_mode_specs
pygame.mixer.init()
pygame.mixer.set_num_channels(16)


fontname = "Lithos Pro Regular"
other_resources_path = "Other_Resources"

game_modes = {"Interval": IntervalGameModeMenu, "Chord": ChordGameModeMenu}


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class IntroductoryQuizMenu:
    def __init__(self, root=None, launch_immediately=True):
        self.menu_frame = root
        self.game_mode_specs = Game_mode_specs()
        self.__prepare_menu(root)
        if launch_immediately:
            self.menu_frame.winfo_toplevel().mainloop()

    def __start_quiz(self, prompt):
        self.menu_frame.pack_forget()
        game_modes[prompt](launch_immediately=True,
                           root=self.menu_frame.winfo_toplevel(), game_mode_specs=self.game_mode_specs)
        self.menu_frame.place(x=0, y=0, relx=1, rely=1)

    def launch_manually(self):
        if self.menu_frame.winfo_toplevel() is not None:
            self.menu_frame.winfo_toplevel().mainloop()

    def __update_chord_prompts(self, prompt):
        if prompt not in self.prompts_for_chord_mode:
            self.prompts_for_chord_mode.add(prompt)
        else:
            self.prompts_for_chord_mode.remove(prompt)
        print(self.prompts_for_chord_mode)

    def __prepare_menu(self, root):
        width = 600
        height = 600

        set_root_specs(root, width, height)
        menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(
            f"{other_resources_path}/mm_background.png"), size=(width, height))
        bg_image_label = ctk.CTkLabel(
            master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        text_label = ctk.CTkLabel(master=menu_frame, text="Please choose one of\nthe quiz variants", font=(
            fontname, 32, "bold"), text_color="black", bg_color="white")
        text_label.place(relx=0.5, y=width*0.25,
                         anchor=ctk.CENTER, relwidth=0.6)

        quiz_mode_sel_frame = ctk.CTkScrollableFrame(master=menu_frame, width=0.4*width, height=0.4*height, fg_color="white", bg_color="white",
                                                     scrollbar_fg_color="white", scrollbar_button_color="white", scrollbar_button_hover_color="grey60")
        quiz_mode_sel_frame.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

        for prompt in game_modes:
            lower_prompt = prompt.lower()
            quiz_button = ctk.CTkButton(master=quiz_mode_sel_frame, text=f"Play {lower_prompt} quiz", corner_radius=8,
                                        fg_color="white", hover_color="grey", text_color="black", bg_color="white",
                                        border_width=2, border_color="black", font=(fontname, 14),
                                        command=lambda prompt_=prompt: self.__start_quiz(prompt_))
            quiz_button.pack(anchor="n", expand=True, padx=10, pady=10)

        # chord_prompts = ["minor", "major", "minor7",
        #                  "major7", "diminished", "major_rev", "minor_rev"]
        # for prompt in chord_prompts:
        #     lower_prompt = prompt.lower()
        #     quiz_button = ctk.CTkButton(master=quiz_mode_sel_frame, text=f"{lower_prompt} quiz", corner_radius=8,
        #                                 fg_color="white", hover_color="grey", text_color="black", bg_color="white",
        #                                 border_width=2, border_color="black", font=(fontname, 14),
        #                                 command=lambda prompt_=prompt: self.__update_chord_prompts(prompt_))
        #     quiz_button.pack(anchor="n", expand=True, padx=10, pady=10)


x = IntroductoryQuizMenu(launch_immediately=True, root=ctk.CTk())
