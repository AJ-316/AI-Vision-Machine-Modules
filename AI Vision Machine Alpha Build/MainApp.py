from typing import Literal

import customtkinter

from CustomTabView import CustomTabView
from TabClasses import *


class SideFrame(ck.CTkFrame):
    SIDE = Literal['left', 'right']

    def __init__(self, main_frame, width, side: SIDE):
        super().__init__(main_frame, width=width, fg_color=FRAME_BG,
                         border_width=2, border_color=FRAME_BORDER_BG)
        self.pack_propagate(False)
        self.pack(ipadx=0, padx=SIDE_FRAME_PADDING, pady=SIDE_FRAME_PADDING, side=side, fill="y")

    def create_button(self, text, pady, command: callable(None) = None):
        button = ck.CTkButton(self, text=text, border_width=1, border_color=BTN_BORDER_BG,
                              font=FONTS["JetBrains Mono_16"], text_color=BUTTON_TEXT_BG,
                              fg_color=BTN_BG, hover_color=BTN_HOVER_BG)
        if command is not None:
            button.configure(command=lambda btn=button: command(btn))
        button.pack(pady=pady)
        return button


class AppearanceOptionMenu(ck.CTkFrame):
    _values = ["Light", "Dark", "System"]

    def __init__(self, master):
        super().__init__(master, fg_color=FRAME_BG)
        self.label = ck.CTkLabel(self, text="Theme:", fg_color=FRAME_BG, font=FONTS["JetBrains Mono_16"])
        self.label.pack(side="left", padx=20, pady=20)
        self.option_menu = ck.CTkOptionMenu(self, dropdown_font=FONTS["Verdana_12"],
                                            font=FONTS["JetBrains Mono_16"], values=self._values,
                                            command=self.change_appearance)
        self.option_menu.pack(side="left")
        self.option_menu.set(self._values[2])
        self.change_appearance(self._values[2])

    def change_appearance(self, choice):
        customtkinter.set_appearance_mode(choice)


class MainFrame(ck.CTk):

    def __init__(self, title):
        super().__init__(fg_color=WIN_BG)
        self.title(title)
        self.minsize(WIN_WIDTH / 1.2, WIN_HEIGHT / 1.2)
        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        load_configs()


class MainApp:
    def __init__(self):
        main = MainFrame("AI Vision Machine Modules Application v0.01")
        tabs = CustomTabView(main)

        side_frame = SideFrame(main, SIDE_FRAME_WIDTH, "left")
        side_frame.create_button("Click11", pady=25)
        side_frame.create_button("Click22", pady=0)
        side_frame.create_button("Click33", pady=25)

        AppearanceOptionMenu(side_frame).pack(side="bottom")

        AIVisionMachineHome(tabs)
        DesktopMouseInputTab(tabs)
        DesktopKeyboardInputTab(tabs)
        WorkoutTrainerTab(tabs)
        PresentationControllerTab(tabs)
        SignLanguageTab(tabs)
        tabs.init_tabs()

        tabs.pack(fill="both", expand=True, padx=24, pady=24)

        try:
            main.mainloop()
        except KeyboardInterrupt as e:
            print(f"Keyboard Interrupt{e}")


if __name__ == "__main__":
    MainApp()
