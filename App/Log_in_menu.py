import customtkinter as ctk
from PIL import Image
from Database_manager import DatabaseManager
from Sign_up_menu import SignUpMenu
from Introductory_quiz_menu import IntroductoryQuizMenu
from Users_assigned_statistician import UsersAssignedStatistician
from Forgot_password_menu import ForgotPasswordMenu


fontname = "Lithos Pro Regular"
other_resources_path = "Other_Resources"


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class LogInMenu:
    def __init__(self, root, launch_immediately=True):
        self.database_manager = DatabaseManager("Confidential/database_file.json")
        self.menu_frame = None
        self.login_entry = None
        self.password_entry = None
        self.error_label = None
        self.__prepare_menu(root)
        if launch_immediately:
            root.mainloop()


    def __forgot_password (self):
        self.menu_frame.pack_forget()
        forgot_password_menu = ForgotPasswordMenu(root=self.menu_frame.winfo_toplevel(), launch_immediately=True,
                                                  database_manager=self.database_manager)
        set_root_specs(self.menu_frame.winfo_toplevel(), 612, 331)
        self.menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame.winfo_toplevel().mainloop()


    def __log_in (self):
        username = self.login_entry.get()
        password = self.password_entry.get()
        if self.database_manager.see_if_user_can_be_logged_in(username, password):
            self.error_label.configure(text="")
            self.login_entry.delete(0, ctk.END)
            self.password_entry.delete(0, ctk.END)
            users_assigned_statistician = UsersAssignedStatistician(username, self.database_manager)
            self.menu_frame.pack_forget()
            introductory_menu = IntroductoryQuizMenu(root=self.menu_frame.winfo_toplevel(), launch_immediately=True,
                                                     statistician=users_assigned_statistician)
            set_root_specs(self.menu_frame.winfo_toplevel(), 612, 331)
            self.menu_frame.pack(fill=ctk.BOTH)
            self.menu_frame.winfo_toplevel().mainloop()
        else:
            if not self.database_manager.see_if_username_exists(username):
                self.error_label.configure(text="No such user has ever been registered")
            else:
                self.error_label.configure(text="Incorrect password and/or login")


    def __sign_up (self):
        self.menu_frame.pack_forget()
        sign_up_menu = SignUpMenu(root=self.menu_frame.winfo_toplevel(),
                                  database_manager=self.database_manager, launch_immediately=True)
        set_root_specs(self.menu_frame.winfo_toplevel(), 612, 331)
        self.menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame.winfo_toplevel().mainloop()


    def __enter_as_guest (self):
        self.error_label.configure(text="")
        self.login_entry.delete(0, ctk.END)
        self.password_entry.delete(0, ctk.END)
        self.menu_frame.pack_forget()
        introductory_menu = IntroductoryQuizMenu(root=self.menu_frame.winfo_toplevel(), launch_immediately=True,
                                                 statistician=None)
        set_root_specs(self.menu_frame.winfo_toplevel(), 612, 331)
        self.menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame.winfo_toplevel().mainloop()


    def __prepare_menu (self, root):
        width = 612
        height = 331
        entry_width = 200
        set_root_specs(root, width, height)

        menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(
            f"{other_resources_path}/lim_bg.png"), size=(width, height))
        bg_image_label = ctk.CTkLabel(
            master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        top = 0.15
        padding = 0.09

        upper_text_label = ctk.CTkLabel(master=menu_frame, text_color="black", font=(fontname, 32, 'bold'),
                                        text="Log in onto\n your account", fg_color="white", bg_color="white")
        upper_text_label.place(relx=0.5, rely=top, anchor=ctk.CENTER)

        top = 0.2

        login_label = ctk.CTkLabel(master=menu_frame, text_color="black", text="Login:", font=(fontname, 14),
                                   fg_color="white", bg_color="white")
        login_label.place(relx=0.5, rely=top+padding, anchor=ctk.CENTER)

        login_entry = ctk.CTkEntry(master=menu_frame, border_width=2, border_color="black", placeholder_text="",
                                   placeholder_text_color="black", font=(fontname, 14), text_color="black",
                                   width=entry_width)
        login_entry.place(relx=0.5, rely=top+2*padding, anchor=ctk.CENTER)
        self.login_entry = login_entry

        password_label = ctk.CTkLabel(master=menu_frame, text_color="black", text="Password:", font=(fontname, 14),
                                      fg_color="white", bg_color="white")
        password_label.place(relx=0.5, rely=top + 3*padding, anchor=ctk.CENTER)

        password_entry = ctk.CTkEntry(master=menu_frame, border_width=2, border_color="black", placeholder_text="",
                                      placeholder_text_color="black", font=(fontname, 14), text_color="black", show="*",
                                      width=entry_width)
        password_entry.place(relx=0.5, rely=top+4*padding, anchor=ctk.CENTER)
        self.password_entry = password_entry

        forgot_password_button = ctk.CTkButton(master=menu_frame, text_color="black", font=(fontname, 11),
                                               text="Forgot password", corner_radius=8, fg_color="white",
                                               hover_color="grey", border_color="black", border_width=1,
                                               width=12, height=8,
                                               command=self.__forgot_password)
        forgot_password_button.place(relx=0.5, rely=top+5*padding, anchor=ctk.CENTER)

        log_in_button = ctk.CTkButton(master=menu_frame, text_color="black", font=(fontname, 14),
                                      text="Log in", corner_radius=8, fg_color="white",
                                      hover_color="grey", bg_color="white",
                                      border_color="black", border_width=2,
                                      width=100, height=10,
                                      command=self.__log_in)
        log_in_button.place(relx=0.5, rely=top+6*padding, anchor=ctk.CENTER)

        sign_up_button = ctk.CTkButton(master=menu_frame, text_color="black", font=(fontname, 14),
                                       text="Sign up", corner_radius=8, hover_color="grey",
                                       fg_color="white", bg_color="white",
                                       border_color="black", border_width=2,
                                       width=100, height=10,
                                       command=self.__sign_up)
        sign_up_button.place(relx=0.4, rely=top + 7 * padding, anchor=ctk.CENTER)

        enter_as_guest_button = ctk.CTkButton(master=menu_frame, text_color="black", font=(fontname, 14),
                                              text="Enter as guest", corner_radius=8, hover_color="grey",
                                              fg_color="white", bg_color="white",
                                              border_color="black", border_width=2,
                                              width=100, height=10,
                                              command=self.__enter_as_guest)
        enter_as_guest_button.place(relx=0.6, rely=top+7*padding, anchor=ctk.CENTER)

        error_label = ctk.CTkLabel(master=menu_frame, text_color="red", font=(fontname, 10), text="",
                                   fg_color="white", bg_color="white")
        error_label.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        self.error_label = error_label


log_in_window = LogInMenu(root=ctk.CTk(), launch_immediately=True)







