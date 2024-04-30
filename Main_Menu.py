import tkinter as tk
from PIL import ImageTk, Image
from Interval_game_mode_window import IntervalGameModeMenu
import pygame


font_name = "Calibri"

pygame.mixer.init()
pygame.mixer.set_num_channels(16)


class Menu:
    def __init__(self,username,launch_immediately=True):
        self.username = username
        self.menu_window = None
        self.__prepare_main_menu_window()
        if launch_immediately:
            self.menu_window.mainloop()


    def __interval_gamemode_chosen (self):
        self.menu_window.destroy()
        I = IntervalGameModeMenu(launch_immediately=True)
        self.__prepare_main_menu_window()

    def __melody_guessing_gamemode_chosen (self):
        self.menu_window.quit()


    def __prepare_main_menu_window (self):
        width = 612
        height = 408

        main_menu_window = tk.Tk()
        main_menu_window.geometry(f"{width}x{height}")
        main_menu_window.resizable(False,False)
        main_menu_window.attributes('-fullscreen',False)
        main_menu_icon = ImageTk.PhotoImage(Image.open("other_resources/kluczwiolinowy.png"))
        main_menu_window.iconphoto(False,main_menu_icon)

        main_menu_bg_image = Image.open("other_resources/mm_background.png")
        main_menu_bg_image = main_menu_bg_image.resize((width,height))
        main_menu_bg_image = ImageTk.PhotoImage(main_menu_bg_image)
        bg_image_label = tk.Label(main_menu_window,image=main_menu_bg_image)
        bg_image_label.place(x=0,y=0,relwidth=1,relheight=1)
        bg_image_label.image = main_menu_bg_image

        main_menu_text = f"Welcome back, {self.username}"
        main_menu_text_label = tk.Label(main_menu_window,text=main_menu_text,font=(font_name,25,"bold"),
                                        foreground="black",justify="center",anchor="n",bg="white")
        main_menu_text_label.place(relx=0,rely=0,x=0,y=2,relwidth=1)

        button_width = 26
        button_height = 1
        vertical_spacing = 35

        interval_button_rely = 0.45
        melody_button_rely = 0.45 + vertical_spacing/height


        interval_button = tk.Button(main_menu_window, text="Play interval gamemode", width=button_width, height=button_height,
                                    background="white", font=(font_name,10,"bold"), foreground="black",
                                    highlightbackground="black",highlightthickness=1,bd=1,
                                    command=self.__interval_gamemode_chosen)

        melody_button = tk.Button(main_menu_window, text="Play melody guessing gamemode", width=button_width, height=button_height,
                                  background="white", font=(font_name,10,"bold"),foreground="black",
                                  highlightbackground="black",highlightthickness=1,bd=1,
                                  command=self.__melody_guessing_gamemode_chosen)

        interval_button.place(relx=0.5, anchor=tk.CENTER, rely=interval_button_rely)
        melody_button.place(relx=0.5, anchor=tk.CENTER, rely=melody_button_rely)

        self.menu_window = main_menu_window



x = Menu(username="Jan",launch_immediately=True)



