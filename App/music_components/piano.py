import customtkinter as ctk
import json
from .key import Key
from .note import get_black_notes, get_white_notes

with open('resources/music_data.json', 'r') as f:
    data = json.load(f)
note_names = data["note_names"]


class Piano:
    def __init__(self, root=None, octaves=2, lowest_octave=2, piano_manager=None):
        self.piano_frame = None
        self.piano_manager = piano_manager
        self.lowest_octave = lowest_octave
        self.keys = {}
        self.key_color_prompts = {}
        self.last_green = None
        self.enabled = True
        self.__prepare_piano(root, octaves, lowest_octave)

    def is_enabled(self):
        return self.enabled

    def get_key_color(self, note_name):
        return self.key_color_prompts[note_name]

    def set_key_color(self, note_name, color):
        self.key_color_prompts[note_name] = color
        if color == "green":
            self.last_green = note_name

    def set_all_reds(self):
        for key in self.key_color_prompts:
            self.key_color_prompts[key] = "red"

    def unset_last_green(self):
        self.key_color_prompts[self.last_green] = "red"

    def play_key(self, note_name):
        self.keys[note_name].play_key()

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def get_number_of_octaves(self):
        return int(len(self.keys)//len(note_names))

    def get_lowest_octave(self):
        return self.lowest_octave

    def set_piano_manager(self, piano_manager):
        self.piano_manager = piano_manager

    def key_was_clicked(self, note_name):
        self.piano_manager.key_was_clicked(note_name)

    def __prepare_piano(self, root, octaves, lowest_octave):
        frame_width = min(root.winfo_width()*0.8, root.winfo_width()-20)
        frame_height = root.winfo_height()*0.4
        white_num = 7

        piano_frame = ctk.CTkFrame(
            master=root, width=frame_width, height=frame_height, bg_color="white")
        piano_frame.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        for i in range(0, 3*white_num*octaves):
            piano_frame.columnconfigure(
                i, minsize=frame_width/(3*white_num*octaves))

        piano_frame.rowconfigure(0, minsize=frame_height/2)
        piano_frame.rowconfigure(1, minsize=frame_height/2)

        def create_white_keys():
            white_notes = get_white_notes(octaves, lowest_octave)
            for i in range(octaves*white_num):
                # new_key = Key(master=piano_frame, note=white_notes[i], parent_piano=self, bg_color="white", fg_color="white", text="", border_width=2)
                new_key = Key(
                    master=piano_frame, note=white_notes[i], parent_piano=self, bg="white", text="", borderwidth=2)
                new_key.configure(command=new_key.clicked)
                new_key.grid(row=0, column=i*3, rowspan=2,
                             columnspan=3, sticky='nsew')
                self.keys[white_notes[i].get_name()] = new_key
                self.key_color_prompts[white_notes[i].get_name()] = "red"

        def create_black_keys():
            black_notes = get_black_notes(octaves, lowest_octave)
            black = [1, 1, 0, 1, 1, 1, 0] * octaves
            name_ix = 0
            for i in range(octaves*white_num-1):
                if black[i]:
                    # new_key = Key(master=piano_frame, note=black_notes[name_ix], parent_piano=self, bg_color="black", fg_color="black", text="", border_width=2)
                    new_key = Key(
                        master=piano_frame, note=black_notes[name_ix], parent_piano=self, bg="black", text="", borderwidth=2)
                    new_key.configure(command=new_key.clicked)
                    new_key.grid(row=0, column=(i*3)+2, rowspan=1,
                                 columnspan=2, sticky='nsew')
                    self.keys[black_notes[name_ix].get_name()] = new_key
                    self.key_color_prompts[black_notes[name_ix].get_name(
                    )] = "red"
                    name_ix += 1

        create_white_keys()
        create_black_keys()
        self.piano_frame = piano_frame

    def destroy_piano(self):
        for key_name in self.keys.keys():
            self.keys[key_name].destroy()
        self.piano_frame.destroy()
