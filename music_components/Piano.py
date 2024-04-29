import tkinter as tk
from music_components.Key import Key
from music_components.Note import *


class Piano:
    def __init__(self, root, octaves=2, lowest_octave=3):
        self.key_num = octaves*12
        self.keys: list[Key] = self.__createPiano(root, octaves, lowest_octave)

    # def __createPiano(self, root: tk, octaves=2, lowest_octave=3) -> list[Key]:
    #     def create_white_keys():
    #         white_notes = get_white_notes(octaves, lowest_octave)
    #         white_keys = []
    #         for i in range(octaves*white_num):
    #             new_key = Key(root, note=white_notes[i])
    #             new_key.configure(
    #                 bg='white',
    #                 command=new_key.clicked
    #             )
    #             new_key.grid(
    #                 row=0,
    #                 column=i*3,
    #                 rowspan=2,
    #                 columnspan=3,
    #                 sticky='nsew'
    #             )
    #             white_keys.append(new_key)
    #         return white_keys
    #
    #     def create_black_keys():
    #         black_notes = get_black_notes(octaves, lowest_octave)
    #         black_keys = []
    #         black = [1, 1, 0, 1, 1, 1, 0] * octaves
    #         name_ix = 0
    #         for i in range(octaves*white_num-1):
    #             if black[i]:
    #                 new_key = Key(root, note=black_notes[name_ix])
    #                 new_key.configure(
    #                     bg='black',
    #                     command=new_key.clicked
    #                 )
    #                 new_key.grid(
    #                     row=0,
    #                     column=(i*3)+2,
    #                     rowspan=1,
    #                     columnspan=2,
    #                     sticky='nsew'
    #                 )
    #                 black_keys.append(new_key)
    #                 name_ix += 1
    #         return black_keys
    #
    #     def sortButtons(whites, blacks):
    #         sorted_keys = []
    #         i = j = 0
    #         for _ in range(octaves):
    #             for note_name in note_names:
    #                 if 'b' in note_name:
    #                     sorted_keys.append(blacks[i])
    #                     i += 1
    #                 else:
    #                     sorted_keys.append(whites[j])
    #                     j += 1
    #         return sorted_keys
    #
    #     white_num = 7
    #     white_keys = create_white_keys()
    #     black_keys = create_black_keys()
    #
    #     for i in range(octaves*white_num * 3):
    #         root.columnconfigure(i, weight=1)
    #     for i in range(2):
    #         root.rowconfigure(i, weight=1)
    #
    #     return sortButtons(white_keys, black_keys)


    def __createPiano (self,root,octaves,lowest_octave):
        frame_width = root.winfo_width()*0.8
        frame_height = root.winfo_height()*0.25

        piano_frame = tk.Frame(root)
        piano_frame.place(relx=0.5,relwidth=0.8,rely=0.65,relheight=0.25, anchor=tk.CENTER)
        white_num = 7
        for i in range (0,3*white_num*octaves):
            piano_frame.columnconfigure(i,minsize=frame_width/(3*white_num*octaves))
        piano_frame.rowconfigure(0,minsize=frame_height/2)
        piano_frame.rowconfigure(1,minsize=frame_height/2)

        def create_white_keys():
            white_notes = get_white_notes(octaves, lowest_octave)
            white_keys = []
            for i in range(octaves*white_num):
                new_key = Key(piano_frame, note=white_notes[i])
                new_key.configure(
                    bg='white',
                    command=new_key.clicked
                )
                new_key.grid(
                    row=0,
                    column=i*3,
                    rowspan=2,
                    columnspan=3,
                    sticky='nsew'
                )
                white_keys.append(new_key)
            return white_keys

        def create_black_keys():
            black_notes = get_black_notes(octaves, lowest_octave)
            black_keys = []
            black = [1, 1, 0, 1, 1, 1, 0] * octaves
            name_ix = 0
            for i in range(octaves*white_num-1):
                if black[i]:
                    new_key = Key(piano_frame, note=black_notes[name_ix])
                    new_key.configure(
                        bg='black',
                        command=new_key.clicked
                    )
                    new_key.grid(
                        row=0,
                        column=(i*3)+2,
                        rowspan=1,
                        columnspan=2,
                        sticky='nsew'
                    )
                    black_keys.append(new_key)
                    name_ix += 1
            return black_keys

        def sortButtons(whites, blacks):
            sorted_keys = []
            i = j = 0
            for _ in range(octaves):
                for note_name in note_names:
                    if 'b' in note_name:
                        sorted_keys.append(blacks[i])
                        i += 1
                    else:
                        sorted_keys.append(whites[j])
                        j += 1
            return sorted_keys

        white_keys = create_white_keys()
        black_keys = create_black_keys()

        for i in range(octaves*white_num * 3):
            root.columnconfigure(i, weight=1)
        for i in range(2):
            root.rowconfigure(i, weight=1)

        # for i in range(5):
        #     button = tk.Button(piano_frame, text="Button {}".format(i + 1), command=lambda x: print("!!"))
        #     button.grid(row=0, column=i, width=40)
        #     #buttons.append(button)

        return sortButtons(white_keys, black_keys)
