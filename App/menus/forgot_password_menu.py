import customtkinter as ctk
from PIL import Image
from utils import DatabaseManager, MailSender
import random
import string
import json

with open('resources/config.json', 'r') as f:
    config = json.load(f)
fontname = config["fontname"]
images_path = config["paths"]["images_path"]


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class ForgotPasswordMenu:
    def __init__(self, root, database_manager, launch_immediately=True):
        self.pre_reset_menu_frame = None
        self.post_reset_menu_frame = None
        self.database_manager = database_manager
        self.mail_sender = None
        self.login_entry = None
        self.reset_code_entry = None
        self.password_entry = None
        self.repeat_password_entry = None
        self.reset_code = None
        self.pre_rse_error_label = None
        self.post_rse_error_label = None
        self.view_password_checkbox = None
        self.__create_mail_sender()
        self.__prepare_menu(root)
        if launch_immediately:
            root.mainloop()

    def __send_reset_code_mail(self):
        reset_code_characters = string.ascii_letters + string.digits
        reset_code_length = 6
        reset_code = "".join(random.choices(
            reset_code_characters, k=reset_code_length))
        self.reset_code = reset_code

        username = self.login_entry.get()
        if self.database_manager.see_if_username_exists(username):
            mail = self.database_manager.get_users_mail_address(username)
            message = (f"Hello!\n"
                       f"It seems that you requested that an account tied to this email address ({
                           username} to be specific) "
                       f"has its password changed\n"
                       f"Your reset password code is as follows: {
                           reset_code}\n\n"
                       f"This message was generated and sent automatically, do not reply to it\n")
            self.mail_sender.send_mail(
                rec=mail, subject="Password reset", message=message)

    def __create_mail_sender(self):
        with open("Confidential/mail_address.txt", 'r') as file:
            bot_address = file.read()
        with open("Confidential/mail_password.txt", 'r') as file:
            bot_password = file.read()
        mail_sender = MailSender(bot_address, bot_password)
        self.mail_sender = mail_sender

    def __start_resetting_password(self):
        given_code = self.reset_code_entry.get()
        if given_code != self.reset_code:
            self.pre_rse_error_label.configure(text="Wrong reset code")
        else:
            self.pre_rse_error_label.configure(text="")
            self.pre_reset_menu_frame.pack_forget()
            self.post_reset_menu_frame.pack(fill=ctk.BOTH)

    def __reset_password(self):
        new_password = self.password_entry.get()
        repeat_password = self.repeat_password_entry.get()
        if new_password != repeat_password:
            self.post_rse_error_label.configure(
                text="Repeated password and password are not the same")
        else:
            self.post_rse_error_label.configure(text="")
            self.database_manager.reset_users_password(
                self.login_entry.get(), new_password)
            self.__quit_reset_stage()
            self.__go_back()

    def __password_hiding_changed(self):
        if self.view_password_checkbox.get() == 1:
            self.password_entry.configure(show='')
            self.repeat_password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')
            self.repeat_password_entry.configure(show='*')

    def __go_back(self):
        self.pre_reset_menu_frame.pack_forget()
        self.pre_reset_menu_frame.winfo_toplevel().quit()

    def __quit_reset_stage(self):
        self.post_reset_menu_frame.pack_forget()
        self.pre_reset_menu_frame.pack(fill=ctk.BOTH)

    def __prepare_menu(self, root):
        width = 612
        height = 331
        set_root_specs(root, width, height)

        pre_reset_menu_frame = ctk.CTkFrame(
            master=root, width=width, height=height)
        pre_reset_menu_frame.pack(fill=ctk.BOTH)
        self.pre_reset_menu_frame = pre_reset_menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(
            f"{images_path}/lim_bg.png"), size=(width, height))
        bg_image_label = ctk.CTkLabel(
            master=pre_reset_menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        top = 0.15
        padding = 0.1

        upper_label = ctk.CTkLabel(master=pre_reset_menu_frame, text_color="black", font=(fontname, 24, "bold"),
                                   text="We will send reset code\nto the email address\ntied to the login", fg_color="white",
                                   bg_color="white")
        upper_label.place(relx=0.5, rely=top, anchor=ctk.CENTER)

        top = 0.25

        login_label = ctk.CTkLabel(master=pre_reset_menu_frame, text_color="black", font=(fontname, 14),
                                   text="Login:", fg_color="white", bg_color="white")
        login_label.place(relx=0.5, rely=top+padding, anchor=ctk.CENTER)

        login_entry = ctk.CTkEntry(master=pre_reset_menu_frame, text_color="black", font=(fontname, 14),
                                   fg_color="white", bg_color="white", corner_radius=8, border_color="black",
                                   border_width=2)
        login_entry.place(relx=0.5, rely=top+2*padding, anchor=ctk.CENTER)
        self.login_entry = login_entry

        send_reset_code_button = ctk.CTkButton(master=pre_reset_menu_frame, text_color="black", font=(fontname, 14),
                                               fg_color="white", bg_color="white", hover_color="grey", corner_radius=8,
                                               border_width=2, border_color="black",
                                               command=self.__send_reset_code_mail,
                                               text="Set email with reset code",
                                               width=100, height=10)
        send_reset_code_button.place(
            relx=0.5, rely=top+3*padding, anchor=ctk.CENTER)

        reset_code_label = ctk.CTkLabel(master=pre_reset_menu_frame, text_color="black", font=(fontname, 14),
                                        fg_color="white", bg_color="white", text="Reset code:")
        reset_code_label.place(relx=0.5, rely=top+4*padding, anchor=ctk.CENTER)

        reset_code_entry = ctk.CTkEntry(master=pre_reset_menu_frame, text_color="black", font=(fontname, 14),
                                        fg_color="white", bg_color="white", corner_radius=8, border_color="black",
                                        border_width=2)
        reset_code_entry.place(relx=0.5, rely=top+5*padding, anchor=ctk.CENTER)
        self.reset_code_entry = reset_code_entry

        reset_code_button = ctk.CTkButton(master=pre_reset_menu_frame, text_color="black", corner_radius=8,
                                          fg_color="white", bg_color="white", border_color="black",
                                          border_width=2, width=100, height=10,
                                          text="Apply reset code and reset password", hover_color="grey",
                                          command=self.__start_resetting_password)
        reset_code_button.place(relx=0.5, rely=top+6 *
                                padding, anchor=ctk.CENTER)

        error_label = ctk.CTkLabel(master=pre_reset_menu_frame, text_color="red", fg_color="white",
                                   bg_color="white", font=(fontname, 10), text="")
        error_label.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        self.pre_rse_error_label = error_label

        go_back_button = ctk.CTkButton(master=pre_reset_menu_frame, text_color="black", width=100, height=10,
                                       bg_color="white", fg_color="white", font=(fontname, 14), text="Go back",
                                       corner_radius=8, command=self.__go_back, hover_color="grey",
                                       border_width=2, border_color="black")
        go_back_button.place(relx=0.1, rely=0.1, anchor=ctk.CENTER)

        post_reset_menu_frame = ctk.CTkFrame(
            master=root, width=width, height=height)
        self.post_reset_menu_frame = post_reset_menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(
            f"{images_path}/lim_bg.png"), size=(width, height))
        bg_image_label = ctk.CTkLabel(
            master=post_reset_menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        top = 0.15
        padding = 0.1

        upper_label = ctk.CTkLabel(master=post_reset_menu_frame, text_color="black", font=(fontname, 24, "bold"),
                                   text="Enter new password", fg_color="white",
                                   bg_color="white")
        upper_label.place(relx=0.5, rely=top, anchor=ctk.CENTER)

        top = 0.2

        password_label = ctk.CTkLabel(master=post_reset_menu_frame, text_color="black", font=(fontname, 14),
                                      text="New password:", fg_color="white", bg_color="white")
        password_label.place(relx=0.5, rely=top+padding, anchor=ctk.CENTER)

        password_entry = ctk.CTkEntry(master=post_reset_menu_frame, text_color="black", font=(fontname, 14),
                                      fg_color="white", bg_color="white", corner_radius=8, border_color="black",
                                      border_width=2, show='*')
        password_entry.place(relx=0.5, rely=top+2*padding, anchor=ctk.CENTER)
        self.password_entry = password_entry

        repeat_password_label = ctk.CTkLabel(master=post_reset_menu_frame, text_color="black", font=(fontname, 14),
                                             fg_color="white", bg_color="white", text="Repeat password:")
        repeat_password_label.place(
            relx=0.5, rely=top+3*padding, anchor=ctk.CENTER)

        repeat_password_entry = ctk.CTkEntry(master=post_reset_menu_frame, text_color="black", font=(fontname, 14),
                                             fg_color="white", bg_color="white", corner_radius=8, border_color="black",
                                             border_width=2, show='*')
        repeat_password_entry.place(
            relx=0.5, rely=top+4*padding, anchor=ctk.CENTER)
        self.repeat_password_entry = repeat_password_entry

        view_password_checkbox = ctk.CTkCheckBox(master=post_reset_menu_frame, text_color="black", checkbox_width=22,
                                                 checkbox_height=22, text="Do not hide password", onvalue=1, offvalue=0,
                                                 command=self.__password_hiding_changed, fg_color="white", bg_color="white",
                                                 corner_radius=32)
        view_password_checkbox.place(
            relx=0.5, rely=top+5*padding, anchor=ctk.CENTER)
        self.view_password_checkbox = view_password_checkbox

        reset_password_button = ctk.CTkButton(master=post_reset_menu_frame, text_color="black", corner_radius=8,
                                              fg_color="white", bg_color="white", border_color="black",
                                              border_width=2, width=100, height=10,
                                              text="Reset password", hover_color="grey",
                                              command=self.__reset_password)
        reset_password_button.place(
            relx=0.5, rely=top+6*padding, anchor=ctk.CENTER)

        error_label = ctk.CTkLabel(master=post_reset_menu_frame, text_color="red", fg_color="white",
                                   bg_color="white", font=(fontname, 10), text="")
        error_label.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        self.post_rse_error_label = error_label

        go_back_button = ctk.CTkButton(master=post_reset_menu_frame, text_color="black", width=100, height=10,
                                       bg_color="white", fg_color="white", font=(fontname, 14), text="Go back",
                                       corner_radius=8, command=self.__quit_reset_stage, border_width=2,
                                       border_color="black", hover_color="grey")
        go_back_button.place(relx=0.1, rely=0.1, anchor=ctk.CENTER)
