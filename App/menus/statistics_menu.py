import customtkinter as ctk
import json
from PIL import Image
from utils import DatabaseManager

with open("resources/config.json", "r") as f:
    config = json.load(f)
fontname = config["fontname"]
images_path = config["paths"]["images_path"]


def set_root_specs(root, width, height):
    menu_window = root
    menu_window.geometry(f"{width}x{height}")
    menu_window.resizable(False, False)
    menu_window.attributes("-fullscreen", False)


class StatisticsMenu:
    def __init__(
        self,
        root,
        user: str,
        database_manager: DatabaseManager,
        launch_immediately=True,
    ) -> None:
        self.menu_frame = None
        self.user = user
        self.database_manager = database_manager
        self.__prepare_menu(root)
        if launch_immediately:
            root.mainloop()

    def __go_back(self) -> None:
        self.menu_frame.pack_forget()
        self.menu_frame.winfo_toplevel().quit()

    def __prepare_menu(self, root) -> None:
        width = 600
        height = 600
        set_root_specs(root, width, height)
        menu_frame = ctk.CTkFrame(
            master=root, width=width, height=height, fg_color="white"
        )
        menu_frame.pack(fill=ctk.BOTH)
        self.menu_frame = menu_frame

        menu_bg_image = ctk.CTkImage(
            light_image=Image.open(f"{images_path}/mm_background.png"),
            size=(width, height),
        )
        bg_image_label = ctk.CTkLabel(master=menu_frame, image=menu_bg_image, text="")
        bg_image_label.pack(fill=ctk.BOTH, expand=True)
        bg_image_label.image = menu_bg_image

        title_label = ctk.CTkLabel(
            master=menu_frame, text="All time statistics", font=(fontname, 35)
        )
        title_label.place(relx=0.5, rely=0.1, anchor="center")
        for i, mode in enumerate(["Interval", "Chord"]):
            mode_label = ctk.CTkLabel(
                master=menu_frame, text=mode + ":", font=(fontname, 30)
            )
            mode_label.place(relx=0.5, rely=0.23 + i * 0.35, anchor="center")

            correct_ans = self.database_manager.see_correct_ans_for_user_and_mode(
                self.user, mode.lower()
            )
            incorrect_ans = self.database_manager.see_incorrect_ans_for_user_and_mode(
                self.user, mode.lower()
            )
            total_ans = correct_ans + incorrect_ans
            if total_ans > 0:
                correct_percentage = (correct_ans / total_ans) * 100
            else:
                correct_percentage = 0
            correct_label = ctk.CTkLabel(
                master=menu_frame,
                text="Correct: " + str(correct_ans),
                font=(fontname, 20),
            )
            correct_label.place(relx=0.3, rely=0.33 + i * 0.35, anchor="center")

            incorrect_label = ctk.CTkLabel(
                master=menu_frame,
                text="Incorrect: " + str(incorrect_ans),
                font=(fontname, 20),
            )
            incorrect_label.place(relx=0.3, rely=0.43 + i * 0.35, anchor="center")
            percentage_label = ctk.CTkLabel(
                master=menu_frame,
                text=f"Correct %:\n {correct_percentage:.2f}%",
                font=(fontname, 20),
            )
            percentage_label.place(relx=0.6, rely=0.33 + i * 0.35)

        go_back_button = ctk.CTkButton(
            master=menu_frame,
            width=width * 0.1,
            height=10,
            border_width=2,
            border_color="black",
            fg_color="white",
            text_color="black",
            text="Go back",
            font=(fontname, 14),
            hover_color="grey",
            command=self.__go_back,
        )
        go_back_button.place(relx=0.15, rely=0.05, anchor=ctk.CENTER)

        self.menu_frame = menu_frame


#
