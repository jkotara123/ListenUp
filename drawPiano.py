import tkinter as tk
from Key import Key
from Note import get_notes
from Note import Note
from checkAnswer import check_answer
from time import sleep


def clicked(button: tk.Button, ans):
    basic = button["background"]
    print(basic)
    if ans:
        button.configure(bg='green')
    else:
        button.configure(bg='red')
    button.configure(bg=basic)


def drawPiano(root: tk, octaves=2):
    def sortButtons(whites, blacks):
        sorted_buttons = []
        i = j = 0
        for note in notes:
            if note.corresponds_to_black_key():
                sorted_buttons.append(blacks[i])
                i += 1
            else:
                sorted_buttons.append(whites[j])
                j += 1
        return sorted_buttons
    notes = get_notes(octaves)
    white_num = 7
    black = [1, 1, 0, 1, 1, 1, 0] * octaves
    white_buttons = []
    black_buttons = []
    for i in range(octaves*white_num):
        new_button = tk.Button(root, bg='white', activebackground='green')
        new_button.configure(
            command=lambda but=new_button: clicked(but, check_answer()))
        new_button.grid(row=0, column=i*3, rowspan=2,
                        columnspan=3, sticky='nsew')
        white_buttons.append(new_button)

    for i in range(octaves*white_num * 3):
        root.columnconfigure(i, weight=1)

    for i in range(2):
        root.rowconfigure(i, weight=1)

    for i in range(octaves*white_num-1):
        if black[i]:
            new_button = tk.Button(root, bg='black', activebackground='red')
            new_button.configure(
                command=lambda but=new_button: clicked(but, check_answer()))
            new_button.grid(row=0, column=(i*3)+2, rowspan=1,
                            columnspan=2, sticky='nsew')
            black_buttons.append(new_button)
    buttons = sortButtons(white_buttons, black_buttons)
    return [Key(note, button) for note, button in zip(notes, buttons)]
