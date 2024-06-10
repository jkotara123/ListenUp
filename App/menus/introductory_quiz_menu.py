import customtkinter as ctk
import pygame
import json
from PIL import Image

from utils import UsersAssignedStatistician
# from .interval_game_mode_menu import IntervalGameModeMenu
# from .chord_game_mode_menu import ChordGameModeMenu
from game_modes import GameModeSpecs
from .settings_menu import SettingsMenu
from .specs_menu import SpecsMenu
from .reset_password_menu import ResetPasswordMenu
from .statistics_menu import StatisticsMenu
from .game_mode_menu import GameModeMenu

pygame.mixer.init()
pygame.mixer.set_num_channels(16)

with open('resources/config.json', 'r') as f:
    config = json.load(f)
fontname = config["fontname"]
images_path = config["paths"]["images_path"]

# game_modes = {"Interval": IntervalGameModeMenu, "Chord": ChordGameModeMenu}


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class IntroductoryQuizMenu:
    def __init__(self, root=None, statistician: UsersAssignedStatistician = None, launch_immediately: bool = True):
        self.menu_frame = root
        self.statistician = statistician
        self.settings = SettingsMenu(root=root, launch_immediately=False)
        self.launch_quiz_button = None
        self.specs_frame = None
        self.game_mode_specs = GameModeSpecs()
        self.specs_menu = None
        self.current_prompt = None
        self.stats_frame = None
        self.__prepare_menu(root)
        if launch_immediately:
            self.menu_frame.winfo_toplevel().mainloop()

    def __draw_exact_selection_frame(self):
        if self.specs_frame is not None:
            self.specs_frame.destroy()
        frame = self.game_mode_specs.create_setting_menu(
            root=self.menu_frame.winfo_toplevel())
        frame.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)
        self.specs_frame = frame

    def __start_quiz(self, prompt):
        self.menu_frame.pack_forget()
        self.current_prompt = prompt
        self.game_mode_specs.set_prompt(self.current_prompt)
        self.specs_menu = SpecsMenu(root=self.menu_frame.winfo_toplevel(), prompt=self.current_prompt,
                                    game_mode_specs=self.game_mode_specs, launch_immediately=True)
        if self.specs_menu.get_launch():
            if self.statistician is not None:
                self.statistician.set_current_mode(self.current_prompt)
            GameModeMenu(launch_immediately=True, statistician=self.statistician, root=self.menu_frame.winfo_toplevel(), game_mode_prompt=self.current_prompt,
                         game_mode_specs=self.game_mode_specs, measure_time=self.settings.get_measure_time(), time=self.settings.get_time())
            set_root_specs(self.menu_frame.winfo_toplevel(), 600, 600)
            self.menu_frame.pack(fill=ctk.BOTH)
        else:
            set_root_specs(self.menu_frame.winfo_toplevel(), 600, 600)
            self.menu_frame.pack(fill=ctk.BOTH)

    def __launch_quiz(self):
        if self.current_prompt is not None:
            self.menu_frame.pack_forget()
            GameModeMenu(launch_immediately=True, statistician=self.statistician, root=self.menu_frame.winfo_toplevel(), game_mode_prompt=self.current_prompt.lower(),
                         game_mode_specs=self.game_mode_specs, measure_time=self.settings.get_measure_time(), time=self.settings.get_time())
            set_root_specs(self.menu_frame.winfo_toplevel(), 600, 600)
            self.menu_frame.place(x=0, y=0, relx=1, rely=1)

    def __open_settings(self):
        self.menu_frame.pack_forget()
        self.settings.launch_manually()
        set_root_specs(self.menu_frame.winfo_toplevel(), 600, 600)
        self.menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame.winfo_toplevel().mainloop()

    def __log_out(self):
        self.menu_frame.pack_forget()
        self.menu_frame.winfo_toplevel().quit()

    def launch_manually(self):
        if self.menu_frame.winfo_toplevel() is not None:
            self.menu_frame.winfo_toplevel().mainloop()

    def __reset_password(self):
        self.menu_frame.pack_forget()
        reset_password_menu = ResetPasswordMenu(root=self.menu_frame.winfo_toplevel(),
                                                statistician=self.statistician,
                                                launch_immediately=True)
        set_root_specs(self.menu_frame.winfo_toplevel(), 600, 600)
        self.menu_frame.pack(fill=ctk.BOTH)

    def __open_stats(self, root):
        self.menu_frame.pack_forget()
        stats_menu = StatisticsMenu(self.menu_frame.winfo_toplevel(
        ), self.statistician.user, self.statistician.database_manager, launch_immediately=True)

        set_root_specs(self.menu_frame.winfo_toplevel(), 600, 600)
        self.menu_frame.pack(fill=ctk.BOTH)

    def __prepare_menu(self, root):
        width = 600
        height = 600

        set_root_specs(root, width, height)
        menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(
            f"{images_path}/mm_background.png"), size=(width, height))
        bg_image_label = ctk.CTkLabel(
            master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        if self.statistician is None:
            first_part = "Welcome to ListenUp!\n"
        else:
            first_part = f"Happy to see you {self.statistician.get_user()}!\n"

        text_label = ctk.CTkLabel(master=menu_frame, text=first_part+"Please choose one of\nthe quiz variants", font=(
            fontname, 32, "bold"), text_color="black", bg_color="white")
        text_label.place(relx=0.5, y=width*0.22,
                         anchor=ctk.CENTER, relwidth=0.6)

        quiz_mode_sel_frame = ctk.CTkFrame(master=menu_frame, width=0.4*width, height=0.25*height, fg_color="white", bg_color="white"
                                           # scrollbar_fg_color="white", scrollbar_button_color="white", scrollbar_button_hover_color="grey60"
                                           )
        quiz_mode_sel_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        for prompt in ["Interval", "Chord"]:
            lower_prompt = prompt.lower()
            quiz_button = ctk.CTkButton(master=quiz_mode_sel_frame, text=f"Play {lower_prompt} quiz", corner_radius=8,
                                        fg_color="white", hover_color="grey", text_color="black", bg_color="white",
                                        border_width=2, border_color="black", font=(fontname, 14),
                                        command=lambda prompt_=lower_prompt: self.__start_quiz(prompt_))
            quiz_button.pack(anchor="n", expand=True, padx=10, pady=10)

        open_settings_button = ctk.CTkButton(master=menu_frame, width=30, height=20, text_color="black", corner_radius=8,
                                             fg_color="white", border_color="black", border_width=2,
                                             font=(fontname, 14), text=f"Open settings", hover_color="grey",
                                             command=self.__open_settings)
        open_settings_button.place(relx=0.9, rely=0.05, anchor=ctk.CENTER)

        log_out_button = ctk.CTkButton(master=menu_frame, width=30, height=20, text_color="black", corner_radius=8,
                                       fg_color="white", border_color="black", border_width=2,
                                       font=(fontname, 14), text="Log out", hover_color="grey",
                                       command=self.__log_out)
        if self.statistician is None:
            log_out_button.configure(text="Go back")
        log_out_button.place(relx=0.1, rely=0.05, anchor=ctk.CENTER)

        if self.statistician:
            reset_password_button = ctk.CTkButton(master=menu_frame, width=100, height=10, text_color="black",
                                                  fg_color="white", bg_color="white", border_color="black",
                                                  border_width=2, corner_radius=8, text="Reset password",
                                                  hover_color="grey", command=self.__reset_password)
            reset_password_button.place(relx=0.1, rely=0.95, anchor=ctk.CENTER)

            reset_password_button = ctk.CTkButton(master=menu_frame, width=100, height=10, text_color="black",
                                                  fg_color="white", bg_color="white", border_color="black",
                                                  border_width=2, corner_radius=8, text="Statistics",
                                                  hover_color="grey", command=lambda _root=root: self.__open_stats(_root))
            reset_password_button.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

# x = IntroductoryQuizMenu(launch_immediately=True, root=ctk.CTk())
