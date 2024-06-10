import customtkinter as ctk
from menus import LogInMenu


def main():
    root = ctk.CTk()
    LogInMenu(root=root, launch_immediately=True)
    root.mainloop()


if __name__ == "__main__":
    main()
