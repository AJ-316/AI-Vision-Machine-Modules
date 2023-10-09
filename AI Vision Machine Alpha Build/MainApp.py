from CustomTabView import CustomTabView
from typing import Literal
from AppConfigs import *


class SideFrame(ck.CTkFrame):
    SIDE = Literal['left', 'right']

    def __init__(self, main_frame, width, side: SIDE):
        super().__init__(main_frame, width=width, fg_color=FRAME_BG,
                         border_width=2, border_color=FRAME_BORDER_BG)
        self.pack_propagate(False)
        self.pack(ipadx=0, padx=SIDE_FRAME_PADDING, pady=SIDE_FRAME_PADDING, side=side, fill="y")

    def create_button(self, text, pady, command: callable(None) = None):
        button = ck.CTkButton(self, text=text, border_width=2, border_color=BTN_BORDER_BG,
                              font=FONTS["JetBrains Mono_16"], text_color=BUTTON_TEXT_BG,
                              fg_color=BTN_BG, hover_color=BTN_HOVER_BG)
        if command is not None:
            button.configure(command=lambda btn=button: command(btn))
        button.pack(pady=pady)
        return button


class MainFrame(ck.CTk):

    def __init__(self, title, geometry):
        super().__init__(fg_color=WIN_BG)
        self.title(title)
        self.geometry(geometry)
        load_configs()


class MainApp:
    def __init__(self):
        main = MainFrame("AI Vision Machine Modules Application v0.01",
                         f"{WIN_WIDTH}x{WIN_HEIGHT}")
        side_frame = SideFrame(main, SIDE_FRAME_WIDTH, "right")
        side_frame.create_button("Click11", pady=25)
        side_frame.create_button("Click22", pady=0)
        side_frame.create_button("Click33", pady=25)

        tabs = CustomTabView(main)
        tabs.pack(fill="both", expand=True, padx=24, pady=24)

        try:
            main.mainloop()
        except KeyboardInterrupt as e:
            print(f"Keyboard Interrupt{e}")


if __name__ == "__main__":
    MainApp()
