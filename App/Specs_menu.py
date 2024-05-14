import customtkinter as ctk
from PIL import Image


fontname = "Lithos Pro Regular"
other_resources_path = "Other_Resources"


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class SpecsMenu:
    def __init__(self, root, prompt, game_mode_specs, launch_immediately=True):
        self.menu_frame = None
        self.game_mode_specs = game_mode_specs
        self.prompt = prompt
        self.launch = False
        self.exact_sel_frame = None
        self.__prepare_menu(root)
        if launch_immediately:
            root.mainloop()


    def get_launch (self):
        return self.launch


    def __go_back (self):
        # if not self.game_mode_specs.is_empty():
        self.launch = False
        self.exact_sel_frame.destroy()
        self.menu_frame.pack_forget()
        self.menu_frame.winfo_toplevel().quit()


    def __launch_quiz (self):
        if not self.game_mode_specs.is_empty():
            self.launch = True
            self.exact_sel_frame.destroy()
            self.menu_frame.pack_forget()
            self.menu_frame.winfo_toplevel().quit()


    def __prepare_menu (self, root):
        width = 600
        height = 600

        set_root_specs(root, width, height)
        menu_frame = ctk.CTkFrame(master=root, width=width, height=height, fg_color="white")
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(
            f"{other_resources_path}/mm_background.png"), size=(width, height))
        bg_image_label = ctk.CTkLabel(
            master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        exact_sel_frame = self.game_mode_specs.create_setting_menu(root=self.menu_frame.winfo_toplevel())
        exact_sel_frame.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
        self.exact_sel_frame = exact_sel_frame

        instruction_label = ctk.CTkLabel(master=menu_frame, text_color="black", text="Please specify how\nthe question should be\ngenerated",
                                         font=(fontname, 20))
        instruction_label.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        go_back_button = ctk.CTkButton(master=menu_frame, width=width*0.1, height=10, border_width=2, border_color="black",
                                       fg_color="white", text_color="black", text="Save and go back", font=(fontname, 14),
                                       hover_color="grey",
                                       command=self.__go_back)
        go_back_button.place(relx=0.15, rely=0.05, anchor=ctk.CENTER)

        start_quiz_button = ctk.CTkButton(master=menu_frame, width=20, height=20, text_color="black", corner_radius=8,
                                          fg_color="white", border_width=2, hover_color="grey", font=(fontname, 14), text=f"Start quiz",
                                          command=self.__launch_quiz, border_color="black")
        start_quiz_button.place(relx=0.92, rely=0.95, anchor=ctk.CENTER)

        self.menu_frame = menu_frame