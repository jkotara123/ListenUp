import customtkinter as ctk
from PIL import Image
from Database_manager import DatabaseManager
import string
import random
from Mail_sender import MailSender


fontname = "Lithos Pro Regular"
other_resources_path = "Other_Resources"


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes('-fullscreen', False)


class SignUpMenu:
    def __init__(self, root, database_manager, launch_immediately=True):
        self.database_manager = database_manager
        self.new_user_username = None
        self.new_user_mail = None
        self.new_user_password = None
        self.mail_sender = None
        self.verification_code = None
        self.__create_mail_sender()
        self.pre_mail_send_menu_frame = None
        self.post_mail_send_menu_frame = None
        self.login_entry = None
        self.mail_entry = None
        self.password_entry = None
        self.repeat_password_entry = None
        self.activation_code_entry = None
        self.pre_ms_error_label = None
        self.post_ms_error_label = None
        self.view_password_checkbox = None
        self.__prepare_menu(root)
        if launch_immediately:
            root.mainloop()


    def __sign_in_new_user (self):
        username = self.login_entry.get()
        self.new_user_username = username
        mail = self.mail_entry.get()
        self.new_user_mail = mail
        password = self.password_entry.get()
        self.new_user_password = password
        repeated_password = self.repeat_password_entry.get()
        if password != repeated_password:
            self.pre_ms_error_label.configure(text="Repeated password must be the same as password")
        else:
            self.pre_ms_error_label.configure(text="")
        username_unique = not self.database_manager.see_if_username_exists(username)
        if not username_unique:
            self.pre_ms_error_label.configure(text="Username is already in use by someone else")
        else:
            self.pre_ms_error_label.configure(text="")
            self.send_mail_with_verification_code()
            self.pre_mail_send_menu_frame.pack_forget()
            self.post_mail_send_menu_frame.pack(fill=ctk.BOTH)


    def send_mail_with_verification_code (self):
        activation_code_characters = string.ascii_letters + string.digits
        activation_code_length = 6
        activation_code = "".join(random.choices(activation_code_characters, k=activation_code_length))
        self.verification_code = activation_code

        message = (f"Hello!\n"
                   f"We are happy you decided to sign up for ListenUp!\n"
                   f"Your activation code is as follows: {activation_code}\n"
                   f"\n"
                   f"This message was generated and sent automatically, do not reply to it\n")

        self.mail_sender.send_mail(rec=self.new_user_mail, subject="Signing up for ListenUp", message=message)


    def __go_back (self):
        self.pre_mail_send_menu_frame.pack_forget()
        self.pre_mail_send_menu_frame.winfo_toplevel().quit()


    def __quit_code_verification_stage (self):
        self.post_mail_send_menu_frame.pack_forget()
        self.pre_mail_send_menu_frame.pack(fill=ctk.BOTH)


    def __create_mail_sender (self):
        with open("Confidential/mail_address.txt", 'r') as file:
            bot_address = file.read()
        with open("Confidential/mail_password.txt", 'r') as file:
            bot_password = file.read()
        mail_sender = MailSender(bot_address, bot_password)
        self.mail_sender = mail_sender


    def __finalize_registration (self):
        print(self.verification_code)
        print(self.activation_code_entry.get())
        if self.verification_code != self.activation_code_entry.get():
            self.post_ms_error_label.configure(text="Incorrect activation code")
        else:
            self.database_manager.add_user(username=self.new_user_username,
                                           mail=self.new_user_mail,
                                           password=self.new_user_password)
            self.__quit_code_verification_stage()
            self.__go_back()


    def __password_hiding_changed (self):
        if self.view_password_checkbox.get() == 1:
            self.password_entry.configure(show='')
            self.repeat_password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')
            self.repeat_password_entry.configure(show='*')


    def __prepare_menu (self, root):
        width = 400
        height = 500
        set_root_specs(root, width, height)
        entry_width = 200

        pre_mail_send_menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        pre_mail_send_menu_frame.pack(fill=ctk.BOTH)
        self.pre_mail_send_menu_frame = pre_mail_send_menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(f"{other_resources_path}/sim_bg.png"),
                                     size=(width, height))
        image_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, image=menu_bg_image, text="")
        image_label.pack(fill=ctk.BOTH, expand=True)

        top = 0.15
        padding = 0.062

        upper_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 34, "bold"),
                                   fg_color="white", bg_color="white", text="Please sign up")
        upper_label.place(relx=0.5, rely=top, anchor=ctk.CENTER)

        top = 0.18

        login_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                   fg_color="white", bg_color="white", text="Login:")
        login_label.place(relx=0.5, rely=top+padding, anchor=ctk.CENTER)

        login_entry = ctk.CTkEntry(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                   corner_radius=8, fg_color="white", bg_color="white",
                                   border_width=2, border_color="black", width=entry_width)
        self.login_entry = login_entry
        login_entry.place(relx=0.5, rely=top+2*padding, anchor=ctk.CENTER)

        mail_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                  fg_color="white", bg_color="white", text="E-mail address:")
        mail_label.place(relx=0.5, rely=top + 3*padding, anchor=ctk.CENTER)

        mail_entry = ctk.CTkEntry(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                  corner_radius=8, fg_color="white", bg_color="white",
                                  border_width=2, border_color="black", width=entry_width)
        self.mail_entry = mail_entry
        mail_entry.place(relx=0.5, rely=top + 4*padding, anchor=ctk.CENTER)

        password_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                      fg_color="white", bg_color="white", text="Password:")
        password_label.place(relx=0.5, rely=top + 5*padding, anchor=ctk.CENTER)

        password_entry = ctk.CTkEntry(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                      corner_radius=8, fg_color="white", bg_color="white",
                                      border_width=2, border_color="black", show="*", width=entry_width)
        self.password_entry = password_entry
        password_entry.place(relx=0.5, rely=top + 6*padding, anchor=ctk.CENTER)

        repeat_password_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                             fg_color="white", bg_color="white", text="Repeat password:")
        repeat_password_label.place(relx=0.5, rely=top + 7*padding, anchor=ctk.CENTER)

        repeat_password_entry = ctk.CTkEntry(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                             corner_radius=8, fg_color="white", bg_color="white",
                                             border_width=2, border_color="black", show="*", width=entry_width)
        self.repeat_password_entry = repeat_password_entry
        repeat_password_entry.place(relx=0.5, rely=top + 8*padding, anchor=ctk.CENTER)

        view_password_checkbox = ctk.CTkCheckBox(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 11),
                                                 text="Do not hide password", onvalue=1, offvalue=0,
                                                 corner_radius=32, checkmark_color="white", bg_color="white",
                                                 command=self.__password_hiding_changed, border_width=2,
                                                 checkbox_width=22, checkbox_height=22)
        self.view_password_checkbox = view_password_checkbox
        view_password_checkbox.place(relx=0.5, rely=top+9.5*padding, anchor=ctk.CENTER)

        sign_in_button = ctk.CTkButton(master=pre_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                       corner_radius=8, bg_color="white", fg_color="white",
                                       border_width=2, border_color="black", width=100,
                                       hover_color="grey", height=10, text="Sign in",
                                       command=self.__sign_in_new_user)
        sign_in_button.place(relx=0.5, rely=top + 11*padding, anchor=ctk.CENTER)

        error_label = ctk.CTkLabel(master=pre_mail_send_menu_frame, text_color="red", font=(fontname, 12),
                                   text="", fg_color="white", bg_color="white")
        error_label.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        self.pre_ms_error_label = error_label

        go_back_button = ctk.CTkButton(master=pre_mail_send_menu_frame, text_color="black", corner_radius=8,
                                       border_width=2, border_color="black", fg_color="white",
                                       bg_color="white", text="Go back", width=100, hover_color="grey",
                                       height=10, command=self.__go_back)
        go_back_button.place(relx=0.15, rely=0.05, anchor=ctk.CENTER)

        post_mail_send_menu_frame = ctk.CTkFrame(master=root, width=width, height=height)
        self.post_mail_send_menu_frame = post_mail_send_menu_frame

        menu_bg_image = ctk.CTkImage(light_image=Image.open(f"{other_resources_path}/sim_bg.png"),
                                     size=(width, height))
        image_label = ctk.CTkLabel(master=post_mail_send_menu_frame, image=menu_bg_image, text="")
        image_label.pack(fill=ctk.BOTH, expand=True)

        top = 0.2
        padding = 0.062

        upper_label = ctk.CTkLabel(master=post_mail_send_menu_frame, text_color="black", font=(fontname, 34, "bold"),
                                   text="Activation code\nhas been sent", fg_color="white", bg_color="white")
        upper_label.place(relx=0.5, rely=top, anchor=ctk.CENTER)

        top = 0.28

        activation_code_label = ctk.CTkLabel(master=post_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                             text="Activation code:", fg_color="white", bg_color="white")
        activation_code_label.place(relx=0.5, rely=top+padding, anchor=ctk.CENTER)

        activation_code_entry = ctk.CTkEntry(master=post_mail_send_menu_frame, text_color="black", font=(fontname, 14),
                                             fg_color="white", bg_color="white", corner_radius=8, border_color="black",
                                             border_width=2, width=entry_width)
        activation_code_entry.place(relx=0.5, rely=top+2*padding, anchor=ctk.CENTER)
        self.activation_code_entry = activation_code_entry

        resend_button = ctk.CTkButton(master=post_mail_send_menu_frame, text_color="black", text="Resend email",
                                      width=100, height=10, corner_radius=8, border_width=2, border_color="black",
                                      fg_color="white", bg_color="white", hover_color="grey",
                                      command=self.send_mail_with_verification_code)
        resend_button.place(relx=0.5, rely=top+3.5*padding, anchor=ctk.CENTER)

        finalize_registration_button = ctk.CTkButton(master=post_mail_send_menu_frame, text_color="black",
                                                     text="Finalize registration",
                                                     width=100, height=10, corner_radius=8, border_width=2, border_color="black",
                                                     fg_color="white", bg_color="white", hover_color="grey",
                                                     command=self.__finalize_registration)
        finalize_registration_button.place(relx=0.5, rely=top+5*padding, anchor=ctk.CENTER)

        error_label = ctk.CTkLabel(master=post_mail_send_menu_frame, text_color="red", font=(fontname, 12),
                                   text="", fg_color="white", bg_color="white")
        error_label.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        self.post_ms_error_label = error_label

        go_back_button = ctk.CTkButton(master=post_mail_send_menu_frame, text_color="black", corner_radius=8,
                                       border_width=2, border_color="black", fg_color="white",
                                       bg_color="white", text="Go back", width=100, hover_color="grey",
                                       height=10, command=self.__quit_code_verification_stage)
        go_back_button.place(relx=0.15, rely=0.05, anchor=ctk.CENTER)








