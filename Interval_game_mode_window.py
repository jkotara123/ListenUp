import tkinter as tk
from PIL import ImageTk, Image
import threading
from time import sleep
from quizManager import QuizManager, max_listens


fontname = ""

correct_answer_colors = ["green2","green3","green4","darkgreen"]
incorrect_answer_colors = ["red","red2","red3","red4"]


class IntervalGameModeMenu:
    def __init__ (self,launch_immediately=True,octaves=2,lowest_octave=2):
        self.interval_gamemode_menu_window = None
        self.quiz_manager = None

        self.play_progress_bar = 0
        self.question_counter = 1
        self.correct_ans_counter = 0
        self.incorrect_ans_counter = 0
        self.play_image = None
        self.listens_left_label = None
        self.question_counter_label = None
        self.question_pass_label = None
        self.correct_ans_counter_label = None
        self.incorrect_ans_counter_label = None
        self.next_question_button = None
        self.next_question_button_grey = True

        self.__prepare_interval_game_mode_menu()
        self.__prepare_piano(octaves,lowest_octave)
        if launch_immediately:
            self.interval_gamemode_menu_window.mainloop()


    def get_window (self):
        return self.interval_gamemode_menu_window


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


    def answered_correctly (self):
        self.correct_ans_counter += 1
        self.correct_ans_counter_label.configure(text=f"{self.correct_ans_counter}")
        self.next_question_button_grey = False
        self.next_question_button.config(fg="black")
        self.interval_gamemode_menu_window.update()

        def pulse ():
            sleep_time = 0.3
            current_question_number = self.question_counter

            for i in range (1,len(correct_answer_colors)):
                if current_question_number != self.question_counter:
                    self.incorrect_ans_counter_label.config(fg=incorrect_answer_colors[0])
                    self.interval_gamemode_menu_window.update()
                    return None
                self.correct_ans_counter_label.config(fg=correct_answer_colors[i])
                sleep(sleep_time)
                self.interval_gamemode_menu_window.update()
            for i in range (len(correct_answer_colors)-1,-1,-1):
                if current_question_number != self.question_counter:
                    self.incorrect_ans_counter_label.config(fg=incorrect_answer_colors[0])
                    self.interval_gamemode_menu_window.update()
                    return None
                self.correct_ans_counter_label.config(fg=correct_answer_colors[i])
                sleep(sleep_time)
                self.interval_gamemode_menu_window.update()

        pulse_thread = threading.Thread(target=pulse,args=())
        pulse_thread.start()


    def answered_incorrectly (self):
        self.incorrect_ans_counter += 1
        self.incorrect_ans_counter_label.configure(text=f"{self.incorrect_ans_counter}")
        self.next_question_button_grey = False
        self.next_question_button.config(fg="black")
        self.interval_gamemode_menu_window.update()

        def pulse():
            sleep_time = 0.3
            current_question_number = self.question_counter

            for i in range(1, len(correct_answer_colors)):
                if current_question_number != self.question_counter:
                    self.incorrect_ans_counter_label.config(fg=incorrect_answer_colors[0])
                    self.interval_gamemode_menu_window.update()
                    return None
                self.incorrect_ans_counter_label.config(fg=incorrect_answer_colors[i])
                self.interval_gamemode_menu_window.update()
                sleep(sleep_time)
            for i in range(len(correct_answer_colors)-1,-1,-1):
                if current_question_number != self.question_counter:
                    self.incorrect_ans_counter_label.config(fg=incorrect_answer_colors[0])
                    self.interval_gamemode_menu_window.update()
                    return None
                self.incorrect_ans_counter_label.config(fg=incorrect_answer_colors[i])
                sleep(sleep_time)
                self.interval_gamemode_menu_window.update()

        pulse_thread = threading.Thread(target=pulse, args=())
        pulse_thread.start()


    def __next_question_clicked (self):
        if not self.next_question_button_grey:
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
            self.next_question_button_grey = True
            self.next_question_button.config(fg="grey")
            self.interval_gamemode_menu_window.update()
            if self.question_pass_label is not None:
                self.question_pass_label.destroy()


    def next_question_called_external (self):
        play_sound_image = Image.open(f"other_resources/play_sound/play_sound{0}.png")
        play_sound_image = play_sound_image.resize((240, 60))
        play_sound_image = ImageTk.PhotoImage(play_sound_image)
        self.play_image.configure(image=play_sound_image)
        self.play_image.image = play_sound_image
        self.play_progress_bar = 0
        self.interval_gamemode_menu_window.update()
        # self.quiz_manager.next_question()
        self.question_counter += 1
        self.question_counter_label.configure(text=f"Question {self.question_counter}")
        self.listens_left_label.configure(text=f"Listens left: {max_listens}")
        self.next_question_button_grey = True
        self.next_question_button.config(fg="grey")
        self.interval_gamemode_menu_window.update()
        if self.question_pass_label is not None:
            self.question_pass_label.destroy()


    def __skip_question_clicked (self):
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
        self.next_question_button_grey = True
        self.next_question_button.config(fg="grey")
        self.interval_gamemode_menu_window.update()
        if self.question_pass_label is not None:
            self.question_pass_label.destroy()


    def __prepare_piano (self,octaves,lowest_octave):
        # piano_window = self.interval_gamemode_menu_window
        # self.piano = Piano(piano_window,octaves,lowest_octave)

        # game_mode_prompt = IntervalMode(self.piano)
        game_mode_prompt = "Interval"
        self.quiz_manager = QuizManager(game_mode_prompt,self)


    # def another_question (self):
    #     self.question_counter += 1
    #     self.question_counter_label.configure(text=f"Question {self.question_counter}")
    #     self.listens_left_label.configure(text=f"Listens left: {max_listens}")
    #     self.next_question_button_grey = True
    #     self.next_question_button.config(fg="grey")
    #     self.interval_gamemode_menu_window.update()


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
        main_menu_text_label = tk.Label(menu_window,text=main_menu_text,font=(fontname,25,"bold"),
                                        foreground="black",justify="center",anchor="n",bg="white")
        self.question_counter_label = main_menu_text_label
        main_menu_text_label.place(relx=0,rely=0,x=0,y=2,relwidth=1)

        relistens_left_text = f"Listens left: {max_listens}"
        # relistens_left_text = f"Relistens left: {3}"
        main_menu_text_label = tk.Label(menu_window,text=relistens_left_text,font=(fontname,14,"bold"),
                                        foreground="black",justify="center",anchor="n",bg="white")
        self.listens_left_label = main_menu_text_label
        main_menu_text_label.place(relx=0.5,rely=0.125,x=0,anchor=tk.CENTER)

        next_question_button = tk.Button(menu_window, text="Next Question", font=(fontname,10), foreground="grey",
                                  highlightbackground="grey",highlightthickness=1,bd=1,background="white",
                                  width=button_width, height=button_height,
                                  command=self.__next_question_clicked)
        self.next_question_button = next_question_button

        skip_question_button = tk.Button(menu_window, text="Skip Question", font=(fontname,10), foreground="black",
                                         highlightbackground="black",highlightthickness=1,bd=1,background="white",
                                         width=button_width,height=button_height,
                                         command=self.__skip_question_clicked)

        next_question_button.place(relx=0.5,anchor=tk.CENTER,rely=0.325)
        skip_question_button.place(relx=0.5,anchor=tk.CENTER,rely=0.325+(vertical_spacing/height))
        # skip_question_button.place(relx=0.5, anchor=tk.CENTER, rely=0.325)

        correct_ans_label = tk.Label(menu_window, text=f"{self.correct_ans_counter}", font=(fontname,16,"bold"), background="white")
        correct_ans_label.config(fg="green2")
        incorrect_ans_label = tk.Label(menu_window, text=f"{self.incorrect_ans_counter}", font=(fontname,16,"bold"), background="white")
        incorrect_ans_label.config(fg="red")
        correct_ans_label.place(x=36,anchor=tk.CENTER,y=height-80)
        incorrect_ans_label.place(x=width-36,anchor=tk.CENTER,y=height-80)

        self.correct_ans_counter_label = correct_ans_label
        self.incorrect_ans_counter_label = incorrect_ans_label

        self.play_image = play_sound_label
        self.interval_gamemode_menu_window = menu_window


