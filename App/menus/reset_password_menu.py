import customtkinter as ctk
import json
from PIL import Image
from utils import UsersAssignedStatistician

with open("resources/config.json", "r") as f:
    config = json.load(f)
fontname = config["fontname"]
images_path = config["paths"]["images_path"]


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes("-fullscreen", False)


class ResetPasswordMenu:
    def __init__(
        self,
        root: ctk.CTk,
        statistician: UsersAssignedStatistician,
        launch_immediately: bool = True,
    ) -> None:
        self.menu_frame: ctk.CTkFrame = None
        self.statistician: UsersAssignedStatistician = statistician
        self.password_entry: ctk.CTkEntry = None
        self.new_password_entry: ctk.CTkEntry = None
        self.repeat_password_entry: ctk.CTkEntry = None
        self.error_label: ctk.CTkLabel = None
        self.view_password_checkbox: ctk.CTkCheckBox = None
        self.__prepare_menu(root)
        if launch_immediately:
            root.mainloop()

    def __password_hiding_changed(self) -> None:
        if self.view_password_checkbox.get() == 1:
            self.password_entry.configure(show="")
            self.new_password_entry.configure(show="")
            self.repeat_password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
            self.new_password_entry.configure(show="*")
            self.repeat_password_entry.configure(show="*")

    def __go_back(self) -> None:
        self.menu_frame.pack_forget()
        self.menu_frame.winfo_toplevel().quit()

    def __reset_password(self) -> None:
        if not self.statistician.check_password(self.password_entry.get()):
            self.error_label.configure(text="Old password was not correct")
        else:
            self.error_label.configure(text="")
            new_password = self.new_password_entry.get()
            repeat_password = self.repeat_password_entry.get()
            if new_password != repeat_password:
                self.error_label.configure(
                    text="Repeated password and password are not the same"
                )
            else:
                self.error_label.configure(text="")
                self.statistician.reset_password(new_password)
                self.__go_back()

    def __prepare_menu(self, root) -> None:
        width = 612
        height = 331
        set_root_specs(root, width, height)

        menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(
            light_image=Image.open(f"{images_path}/lim_bg.png"), size=(width, height)
        )
        bg_image_label = ctk.CTkLabel(master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        top = 0.1
        padding = 0.09

        upper_label = ctk.CTkLabel(
            master=menu_frame,
            text_color="black",
            font=(fontname, 24, "bold"),
            text="Enter new password",
            fg_color="white",
            bg_color="white",
        )
        upper_label.place(relx=0.5, rely=top, anchor=ctk.CENTER)

        top = 0.15

        password_label = ctk.CTkLabel(
            master=menu_frame,
            text_color="black",
            font=(fontname, 14),
            text="Current password:",
            fg_color="white",
            bg_color="white",
        )
        password_label.place(relx=0.5, rely=top + padding, anchor=ctk.CENTER)

        password_entry = ctk.CTkEntry(
            master=menu_frame,
            text_color="black",
            font=(fontname, 14),
            fg_color="white",
            bg_color="white",
            corner_radius=8,
            border_color="black",
            border_width=2,
            show="*",
        )
        password_entry.place(relx=0.5, rely=top + 2 * padding, anchor=ctk.CENTER)
        self.password_entry = password_entry

        new_password_label = ctk.CTkLabel(
            master=menu_frame,
            text_color="black",
            font=(fontname, 14),
            text="New password:",
            fg_color="white",
            bg_color="white",
        )
        new_password_label.place(relx=0.5, rely=top + 3 * padding, anchor=ctk.CENTER)

        new_password_entry = ctk.CTkEntry(
            master=menu_frame,
            text_color="black",
            font=(fontname, 14),
            fg_color="white",
            bg_color="white",
            corner_radius=8,
            border_color="black",
            border_width=2,
            show="*",
        )
        new_password_entry.place(relx=0.5, rely=top + 4 * padding, anchor=ctk.CENTER)
        self.new_password_entry = new_password_entry

        repeat_password_label = ctk.CTkLabel(
            master=menu_frame,
            text_color="black",
            font=(fontname, 14),
            fg_color="white",
            bg_color="white",
            text="Repeat password:",
        )
        repeat_password_label.place(relx=0.5, rely=top + 5 * padding, anchor=ctk.CENTER)

        repeat_password_entry = ctk.CTkEntry(
            master=menu_frame,
            text_color="black",
            font=(fontname, 14),
            fg_color="white",
            bg_color="white",
            corner_radius=8,
            border_color="black",
            border_width=2,
            show="*",
        )
        repeat_password_entry.place(relx=0.5, rely=top + 6 * padding, anchor=ctk.CENTER)
        self.repeat_password_entry = repeat_password_entry

        view_password_checkbox = ctk.CTkCheckBox(
            master=menu_frame,
            text_color="black",
            checkbox_width=22,
            checkbox_height=22,
            text="Do not hide password",
            onvalue=1,
            offvalue=0,
            command=self.__password_hiding_changed,
            fg_color="white",
            bg_color="white",
            corner_radius=32,
        )
        view_password_checkbox.place(
            relx=0.5, rely=top + 7 * padding, anchor=ctk.CENTER
        )
        self.view_password_checkbox = view_password_checkbox

        reset_password_button = ctk.CTkButton(
            master=menu_frame,
            text_color="black",
            corner_radius=8,
            fg_color="white",
            bg_color="white",
            border_color="black",
            border_width=2,
            width=100,
            height=10,
            text="Reset password",
            hover_color="grey",
            command=self.__reset_password,
        )
        reset_password_button.place(relx=0.5, rely=top + 8 * padding, anchor=ctk.CENTER)

        error_label = ctk.CTkLabel(
            master=menu_frame,
            text_color="red",
            fg_color="white",
            bg_color="white",
            font=(fontname, 10),
            text="",
        )
        error_label.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        self.error_label = error_label

        go_back_button = ctk.CTkButton(
            master=menu_frame,
            text_color="black",
            width=100,
            height=10,
            bg_color="white",
            fg_color="white",
            font=(fontname, 14),
            text="Go back",
            corner_radius=8,
            command=self.__go_back,
            border_width=2,
            border_color="black",
            hover_color="grey",
        )
        go_back_button.place(relx=0.1, rely=0.1, anchor=ctk.CENTER)
