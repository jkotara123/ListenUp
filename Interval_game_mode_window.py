import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import other_resources
from time import sleep


class IntervalGameModeMenu:
    def __init__ (self,launch_immediately=True):
        self.interval_gamemode_menu_window = None
        self.play_progress_bar = 0
        self.play_image = None
        self.__prepare_interval_game_mode_menu()
        if launch_immediately:
            self.interval_gamemode_menu_window.mainloop()

    def launch_manually (self):
        self.interval_gamemode_menu_window.mainloop()


    def __animate_play_image (self):
        if self.play_progress_bar != 0:
            return
        else:
            print(self.play_image)
            for i in range (1,11):
                self.play_progress_bar = i
                play_sound_image = Image.open(f"other_resources/play_sound/play_sound{i}.png")
                play_sound_image = play_sound_image.resize((240, 60))
                play_sound_image = ImageTk.PhotoImage(play_sound_image)
                self.play_image.configure(image=play_sound_image)
                self.play_image.image = play_sound_image
                self.interval_gamemode_menu_window.update()
                sleep(0.2)

            play_sound_image = Image.open(f"other_resources/play_sound/play_sound{0}.png")
            play_sound_image = play_sound_image.resize((240, 60))
            play_sound_image = ImageTk.PhotoImage(play_sound_image)
            self.play_image.configure(image=play_sound_image)
            self.play_image.image = play_sound_image
            self.play_progress_bar = 0
            self.interval_gamemode_menu_window.update()


    def __prepare_interval_game_mode_menu (self):
        width = 612
        height = 331

        menu_window = tk.Tk()
        menu_window.geometry(f"{width}x{height}")
        menu_window.resizable(False, False)
        menu_window.attributes('-fullscreen', False)
        menu_icon = ImageTk.PhotoImage(Image.open("other_resources/kluczwiolinowy.png"))
        menu_window.iconphoto(False, menu_icon)

        menu_bg_image = Image.open("other_resources/gm_bg.png")
        menu_bg_image = menu_bg_image.resize((width, height))
        menu_bg_image = ImageTk.PhotoImage(menu_bg_image)
        bg_image_label = tk.Label(menu_window, image=menu_bg_image)
        bg_image_label.place(x=0,y=0,relwidth=1,relheight=1)
        bg_image_label.image = menu_bg_image

        play_sound_image = Image.open("other_resources/play_sound/play_sound0.png")
        play_sound_image = play_sound_image.resize((240,60))
        play_sound_image = ImageTk.PhotoImage(play_sound_image)
        play_sound_label = tk.Label(menu_window, image=play_sound_image)
        play_sound_label.bind("<Button-1>", lambda event: self.__animate_play_image())
        play_sound_label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        play_sound_label.image = play_sound_image

        self.play_image = play_sound_label
        self.interval_gamemode_menu_window = menu_window


# IntervalGameModeMenu(launch_immediately=True)
