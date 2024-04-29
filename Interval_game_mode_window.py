import tkinter as tk
from PIL import ImageTk, Image
import other_resources
from time import sleep
from music_components.Piano import Piano
from quizManager import QuizManager, max_listens
from gameModes.IntervalMode import IntervalMode

class IntervalGameModeMenu:
    def __init__ (self,launch_immediately=True,octaves=2,lowest_octave=2):
        self.interval_gamemode_menu_window = None
        self.piano = None
        self.play_progress_bar = 0
        self.question_counter = 1
        self.play_image = None
        self.quiz_manager = None
        self.listens_left_label = None
        self.question_counter_label = None
        self.question_pass_label = None

        self.__prepare_interval_game_mode_menu()
        self.__prepare_piano(octaves,lowest_octave)
        if launch_immediately:
            self.interval_gamemode_menu_window.mainloop()

    def launch_manually (self):
        self.interval_gamemode_menu_window.mainloop()


    def __animate_play_image (self):
        if self.play_progress_bar != 0:
            return None
        else:
            try:
                self.quiz_manager.play_question()
            except Exception:
                play_sound_image = Image.open(f"other_resources/play_sound/play_sound_grey.png")
                play_sound_image = play_sound_image.resize((240,60))
                play_sound_image = ImageTk.PhotoImage(play_sound_image)
                self.play_image.configure(image=play_sound_image)
                self.play_image.image = play_sound_image
                self.interval_gamemode_menu_window.update()
                return None


            self.listens_left_label.configure(text=f"Listens left: {self.quiz_manager.get_remaining_listens()} ")
            sleep_time = self.quiz_manager.get_question_duration() / 10
            for i in range (1,11):
                self.play_progress_bar = i
                play_sound_image = Image.open(f"other_resources/play_sound/play_sound{i}.png")
                play_sound_image = play_sound_image.resize((240, 60))
                play_sound_image = ImageTk.PhotoImage(play_sound_image)
                self.play_image.configure(image=play_sound_image)
                self.play_image.image = play_sound_image
                self.interval_gamemode_menu_window.update()
                sleep(sleep_time)

            if self.quiz_manager.listen_cap_met():
                play_sound_image_path = f"other_resources/play_sound/play_sound_grey.png"
            else:
                play_sound_image_path = f"other_resources/play_sound/play_sound{0}.png"

            play_sound_image = Image.open(play_sound_image_path)
            play_sound_image = play_sound_image.resize((240, 60))
            play_sound_image = ImageTk.PhotoImage(play_sound_image)
            self.play_image.configure(image=play_sound_image)
            self.play_image.image = play_sound_image
            self.play_progress_bar = 0
            self.interval_gamemode_menu_window.update()


    def display_tick (self):
        if self.question_pass_label is not None:
            self.question_pass_label.destroy()
        tick_image = Image.open("other_resources/green_tick.png")
        tick_image = tick_image.resize((50,50))
        tick_image = ImageTk.PhotoImage(tick_image)
        bg_image_label = tk.Label(self.interval_gamemode_menu_window, image=tick_image)
        bg_image_label.place(x=0,y=self.interval_gamemode_menu_window.winfo_width())
        bg_image_label.image = tick_image
        self.question_pass_label = bg_image_label

    def display_cross (self):
        if self.question_pass_label is not None:
            self.question_pass_label.destroy()
        tick_image = Image.open("other_resources/red_cross.png")
        tick_image = tick_image.resize((50, 50))
        tick_image = ImageTk.PhotoImage(tick_image)
        bg_image_label = tk.Label(self.interval_gamemode_menu_window, image=tick_image)
        bg_image_label.place(x=0, y=self.interval_gamemode_menu_window.winfo_width())
        bg_image_label.image = tick_image
        self.question_pass_label = bg_image_label


    def __next_question_clicked (self):
        play_sound_image = Image.open(f"other_resources/play_sound/play_sound{0}.png")
        play_sound_image = play_sound_image.resize((240, 60))
        play_sound_image = ImageTk.PhotoImage(play_sound_image)
        self.play_image.configure(image=play_sound_image)
        self.play_image.image = play_sound_image
        self.play_progress_bar = 0
        self.interval_gamemode_menu_window.update()
        self.quiz_manager.next_question()
        self.question_counter += 1
        self.question_counter_label.configure(text=f"Question {self.question_counter}")
        self.listens_left_label.configure(text=f"Listens left: {max_listens}")
        self.interval_gamemode_menu_window.update()
        if self.question_pass_label is not None:
            self.question_pass_label.destroy()


    def __skip_question_clicked (self):
        ...


    def __prepare_piano (self,octaves,lowest_octave):
        # height = 140
        # width = 260*octaves
        piano_window = self.interval_gamemode_menu_window
        # piano_window.geometry(f"{width}x{height}")
        # piano_window.attributes('-fullscreen',False)
        # piano_window.resizable(False,False)
        # piano_window.geometry("-200-200")
        self.piano = Piano(piano_window,octaves,lowest_octave)
        # piano_window.mainloop()

        game_mode = IntervalMode(self.piano)

        self.quiz_manager = QuizManager(game_mode,self.piano,self)


    def __prepare_interval_game_mode_menu (self):
        width = 612
        height = 662
        button_width = 26
        button_height = 1
        vertical_spacing = 35

        menu_window = tk.Tk()
        menu_window.geometry(f"{width}x{height}")
        menu_window.resizable(False, False)
        menu_window.attributes('-fullscreen', False)
        menu_icon = ImageTk.PhotoImage(Image.open("other_resources/kluczwiolinowy.png"))
        menu_window.iconphoto(False, menu_icon)

        menu_bg_image = Image.open("other_resources/gm_bg.png")
        menu_bg_image = menu_bg_image.resize((width, 0.5*height))
        menu_bg_image = ImageTk.PhotoImage(menu_bg_image)
        bg_image_label = tk.Label(menu_window, image=menu_bg_image)
        bg_image_label.place(x=0,y=0,relwidth=1,relheight=0.5)
        bg_image_label.image = menu_bg_image

        menu_bg_image = Image.open("other_resources/gm_bg_rev.png")
        menu_bg_image = menu_bg_image.resize((width, 0.5*height))
        menu_bg_image = ImageTk.PhotoImage(menu_bg_image)
        bg_image_label = tk.Label(menu_window, image=menu_bg_image)
        bg_image_label.place(x=0,rely=0.5,relwidth=1,relheight=0.5)
        bg_image_label.image = menu_bg_image

        play_sound_image = Image.open("other_resources/play_sound/play_sound0.png")
        play_sound_image = play_sound_image.resize((240,60))
        play_sound_image = ImageTk.PhotoImage(play_sound_image)
        play_sound_label = tk.Label(menu_window, image=play_sound_image)
        play_sound_label.bind("<Button-1>", lambda event: self.__animate_play_image())
        play_sound_label.place(relx=0.5,rely=0.25,anchor=tk.CENTER)
        play_sound_label.image = play_sound_image

        main_menu_text = f"Question 1"
        main_menu_text_label = tk.Label(menu_window,text=main_menu_text,font=("Times New Roman",25,"bold"),
                                        foreground="black",justify="center",anchor="n",bg="white")
        self.question_counter_label = main_menu_text_label
        main_menu_text_label.place(relx=0,rely=0,x=0,y=2,relwidth=1)

        relistens_left_text = f"Listens left: {max_listens}"
        # relistens_left_text = f"Relistens left: {3}"
        main_menu_text_label = tk.Label(menu_window,text=relistens_left_text,font=("Times New Roman",14,"bold"),
                                        foreground="black",justify="center",anchor="n",bg="white")
        self.listens_left_label = main_menu_text_label
        main_menu_text_label.place(relx=0.5,rely=0.125,x=0,anchor=tk.CENTER)

        next_question_button = tk.Button(menu_window, text="Next Question", font=("Times New Roman",12,"bold"), foreground="black",
                                  highlightbackground="black",highlightthickness=1,bd=1,background="white",
                                  width=button_width, height=button_height,
                                  command=self.__next_question_clicked)

        skip_question_button = tk.Button(menu_window, text="Skip Question", font=("Times New Roman",12,"bold"), foreground="black",
                                         highlightbackground="black",highlightthickness=1,bd=1,background="white",
                                         width=button_width,height=button_height,
                                         command=self.__next_question_clicked)

        next_question_button.place(relx=0.5,anchor=tk.CENTER,rely=0.325)
        skip_question_button.place(relx=0.5,anchor=tk.CENTER,rely=0.325+(vertical_spacing/height))
        # skip_question_button.place(relx=0.5, anchor=tk.CENTER, rely=0.325)

        self.play_image = play_sound_label
        self.interval_gamemode_menu_window = menu_window


# IntervalGameModeMenu(launch_immediately=True)
