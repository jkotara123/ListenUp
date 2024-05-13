import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Communication_channel import CommunicationChannel
from Music_Components.Piano import Piano
from time import sleep
import threading


other_resources_path = "Other_Resources"


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)
    menu_window.configure(bg="white")


green = ["green2", "green3", "green4"]
red = ["red", "red2", "red3"]


fontname = "Lithos Pro Regular"


max_listens = 3
listening_steps = 10


class GameModeMenu:
    def __init__(self, root=None, launch_immediately=True, octaves=2, lowest_octave=2, game_mode_prompt=None):
        self.menu_frame = None
        self.piano = None
        self.quiz_manager_comm_channel = None
        self.correct_ans_button = None
        self.incorrect_ans_button = None
        self.play_label = None
        self.question_counter_label = None
        self.listens_left_label = None
        self.next_question_button = None
        self.show_answer_button = None

        self.correct_ans_count = 0
        self.incorrect_ans_count = 0
        self.question_counter = 1
        self.listens_left = max_listens
        self.listening_in_progress = False
        self.answer_given = False

        self.__prepare_menu(root, octaves)
        self.__prepare_piano(root, octaves, lowest_octave)
        self.__prepare_quiz_manager(game_mode_prompt)
        if launch_immediately:
            self.menu_frame.winfo_toplevel().mainloop()

    def __prepare_quiz_manager(self, game_mode_prompt):
        if game_mode_prompt is not None:
            if game_mode_prompt == "Interval":
                self.quiz_manager_comm_channel = CommunicationChannel()
                self.quiz_manager_comm_channel.set_menu(self)
                self.quiz_manager_comm_channel.create_quiz_manager(
                    "Interval", self.piano, max_listens)
            elif game_mode_prompt == "Chord":
                self.quiz_manager_comm_channel = CommunicationChannel()
                self.quiz_manager_comm_channel.set_menu(self)
                self.quiz_manager_comm_channel.create_quiz_manager(
                    "Chord", self.piano, max_listens)

    def __prepare_piano(self, root, octaves, lowest_octave):
        self.piano = Piano(root, octaves=octaves, lowest_octave=lowest_octave)

    def play_question(self, unused):
        play_label_width = 288
        play_label_height = 72

        def internal_play_question():
            try:
                self.quiz_manager_comm_channel.play_question()
            except Exception:
                play_image = ctk.CTkImage(light_image=Image.open(f"{other_resources_path}/play_sound/play_sound_grey.png"),
                                          size=(play_label_width, play_label_height))
                self.play_label.configure(image=play_image)
                self.menu_frame.winfo_toplevel().update()
                return None

            duration = 1
            sleep_time = duration/listening_steps
            self.listening_in_progress = True
            self.listens_left -= 1
            if self.listens_left == 0:
                self.listens_left_label.configure(
                    text=f"You cannot listen listen to the question anymore")
            elif self.listens_left == 1:
                self.listens_left_label.configure(text=f"You can listen to the question {
                                                  self.listens_left} more time")
            else:
                self.listens_left_label.configure(text=f"You can listen to the question {
                                                  self.listens_left} more times")

            for i in range(1, listening_steps+1):
                play_image = Image.open(
                    f"{other_resources_path}/play_sound/play_sound{i}.png")
                play_image = play_image.resize(
                    (play_label_width, play_label_height))
                play_image = ImageTk.PhotoImage(play_image)
                self.play_label.configure(image=play_image)
                # self.menu_frame.winfo_toplevel().update()
                sleep(sleep_time)

            if self.listens_left == 0:
                play_image = Image.open(
                    f"{other_resources_path}/play_sound/play_sound_grey.png")
                play_image = play_image.resize(
                    (play_label_width, play_label_height))
                play_image = ImageTk.PhotoImage(play_image)
                self.play_label.configure(image=play_image)
                # self.menu_frame.winfo_toplevel().update()
            else:
                play_image = Image.open(
                    f"{other_resources_path}/play_sound/play_sound{0}.png")
                play_image = play_image.resize(
                    (play_label_width, play_label_height))
                play_image = ImageTk.PhotoImage(play_image)
                self.play_label.configure(image=play_image)
                # self.menu_frame.winfo_toplevel().update()

            self.listening_in_progress = False

        if not self.listening_in_progress:
            listening_thread = threading.Thread(target=internal_play_question)
            listening_thread.start()

    def answered_correctly(self):

        def update():
            self.correct_ans_count += 1
            self.correct_ans_button.configure(text=f"{self.correct_ans_count}")
            flash_duration = 0.8
            sleep_time = flash_duration/(2*len(green))
            for i in range(1, len(green)):
                self.correct_ans_button.configure(fg_color=green[i])
                sleep(sleep_time)
                self.menu_frame.winfo_toplevel().update()
            for i in range(len(green)-2, -1, -1):
                self.correct_ans_button.configure(fg_color=green[i])
                sleep(sleep_time)
                self.menu_frame.winfo_toplevel().update()

        self.answer_given = True
        self.next_question_button.configure(
            text_color="black", hover_color="grey", border_color="black")
        self.show_answer_button.configure(
            text_color="black", hover_color="grey", border_color="black")
        flash_thread = threading.Thread(target=update)
        flash_thread.start()

    def answered_incorrectly(self):

        def update():
            self.incorrect_ans_count += 1
            self.incorrect_ans_button.configure(
                text=f"{self.incorrect_ans_count}")
            flash_duration = 0.8
            sleep_time = flash_duration/(2*len(red))
            for i in range(1, len(green)):
                self.incorrect_ans_button.configure(fg_color=red[i])
                sleep(sleep_time)
                self.menu_frame.winfo_toplevel().update()
            for i in range(len(green) - 2, -1, -1):
                self.incorrect_ans_button.configure(fg_color=red[i])
                sleep(sleep_time)
                self.menu_frame.winfo_toplevel().update()

        self.answer_given = True
        self.next_question_button.configure(
            text_color="black", hover_color="grey", border_color="black")
        self.show_answer_button.configure(
            text_color="black", hover_color="grey", border_color="black")
        flash_thread = threading.Thread(target=update)
        flash_thread.start()

    def next_question(self):
        if self.answer_given:
            self.answer_given = False
            self.question_counter += 1
            self.listens_left = max_listens
            self.next_question_button.configure(
                text_color="grey", hover_color="white", border_color="grey")
            self.show_answer_button.configure(
                text_color="grey", hover_color="white", border_color="grey")
            self.listens_left_label.configure(text=f"You can listen the question {
                                              self.listens_left} more times")
            self.question_counter_label.configure(
                text=f"Question {self.question_counter}")
            self.quiz_manager_comm_channel.create_new_question()

    def show_correct_answer(self):
        if self.answer_given and not self.listening_in_progress:
            self.listening_in_progress = True
            self.quiz_manager_comm_channel.show_correct_answer()
            self.listening_in_progress = False

    def __prepare_menu(self, root, octaves):
        width = int(400+(octaves-1)*(400*0.8))
        height = 400
        button_width = int(50*1.25)
        button_height = int(35*1.25)
        play_label_width = 288
        play_label_height = 72

        set_root_specs(root, width, height)
        menu_frame = ctk.CTkLabel(
            master=root, width=width, height=height, bg_color="white", fg_color="white", text="white")
        menu_frame.pack(fill=ctk.BOTH)

        menu_bg_image = Image.open(
            f"{other_resources_path}/gm_background_.png")
        menu_bg_image = ImageTk.PhotoImage(menu_bg_image)
        bg_image_label = tk.Label(
            menu_frame, image=menu_bg_image, text="", bg="white")
        bg_image_label.place(x=0, y=0, relheight=1)
        bg_image_label.image = menu_bg_image

        menu_bg_image = Image.open(
            f"{other_resources_path}/gm_background_rev_.png")
        menu_bg_image = ImageTk.PhotoImage(menu_bg_image)
        bg_image_label = tk.Label(
            menu_frame, image=menu_bg_image, text="", bg="white")
        bg_image_label.place(x=width-menu_bg_image.width(), y=0, relheight=1)
        bg_image_label.image = menu_bg_image

        correct_ans_image = ctk.CTkImage(light_image=Image.open(
            f"{other_resources_path}/white_tick_tbg.png"), size=(button_height//2, button_height//2))
        correct_ans_button = ctk.CTkButton(master=menu_frame, text=f"{self.correct_ans_count}",
                                           image=correct_ans_image, fg_color=green[0],
                                           text_color="white", border_width=2, hover_color=green[0],
                                           width=button_width, height=button_height,
                                           corner_radius=8, font=(fontname, 18), border_color="darkgreen")
        correct_ans_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        self.correct_ans_button = correct_ans_button

        incorrect_ans_image = ctk.CTkImage(light_image=Image.open(
            f"{other_resources_path}/white_cross_tbg.png"), size=(button_height//2, button_height//2))
        incorrect_ans_button = ctk.CTkButton(master=menu_frame, text=f"{self.correct_ans_count}",
                                             image=incorrect_ans_image, fg_color=red[0],
                                             text_color="white", border_width=2, hover_color=red[0],
                                             width=button_width, height=button_height,
                                             corner_radius=8, font=(fontname, 18), border_color="red4")
        incorrect_ans_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        self.incorrect_ans_button = incorrect_ans_button

        # play_image = ctk.CTkImage(light_image=Image.open(f"{other_resources_path}/play_sound/play_sound0.png"), size=(play_label_width, play_label_height))
        # play_button = ctk.CTkButton(master=menu_frame, text="", image=play_image, border_width=2, border_color="purple", hover_color="white",
        #                             width=play_label_width, height=play_label_height, command=self.play_question, bg_color="white", fg_color="white")
        # play_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        # self.play_button = play_button

        question_counter_label = ctk.CTkLabel(master=menu_frame, text=f"Question {self.question_counter}", font=(fontname, 22, "bold"),
                                              fg_color="transparent", bg_color="transparent", text_color="black")
        question_counter_label.place(relx=0.5, rely=0.04, anchor=ctk.CENTER)
        self.question_counter_label = question_counter_label

        listens_left_label = ctk.CTkLabel(master=menu_frame, text=f"You can listen the question {self.listens_left} more times", font=(fontname, 14, "bold"),
                                          fg_color="transparent", bg_color="transparent", text_color="black")
        listens_left_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        self.listens_left_label = listens_left_label

        play_image = ctk.CTkImage(light_image=Image.open(
            f"{other_resources_path}/play_sound/play_sound0.png"), size=(play_label_width, play_label_height))
        play_label = ctk.CTkLabel(master=menu_frame, text="", image=play_image,
                                  width=play_label_width, height=play_label_height)
        play_label.bind("<Button-1>", self.play_question)
        play_label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        self.play_label = play_label

        vertical_spacing = 35

        next_question_button = ctk.CTkButton(master=menu_frame, text=f"Next question", font=(fontname, 12), fg_color='white', bg_color="transparent",
                                             corner_radius=8, text_color="grey", command=self.next_question, hover_color="white",
                                             width=button_width//2, height=button_height//2, border_color="grey", border_width=2)
        next_question_button.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)
        self.next_question_button = next_question_button

        show_answer_button = ctk.CTkButton(master=menu_frame, text=f"Show the correct answer", font=(fontname, 12), fg_color='white', bg_color="transparent",
                                           corner_radius=8, text_color="grey", command=self.show_correct_answer, hover_color="white",
                                           width=button_width//2, height=button_height//2, border_color="grey", border_width=2)
        show_answer_button.place(
            relx=0.5, y=0.85*(vertical_spacing+height), anchor=ctk.CENTER)
        self.show_answer_button = show_answer_button

        self.menu_frame = menu_frame
