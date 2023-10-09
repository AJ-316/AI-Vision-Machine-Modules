from AppConfigs import *


class Tab:

    def __init__(self, name, button, frame, tab_view):
        self.name = name
        self._button = button
        self._frame = frame
        self.normal_config = self.on_normal_config
        self.selected_config = self.on_selected_config
        tab_view.add_tab(self)

    def select(self, tab_view):
        self._button._state = "disabled"
        self.selected_config()
        tab_view.deselect_tabs(self)
        self._frame.pack(fill="both", expand=True)

    def deselect(self):
        self._button._state = "normal"
        self.normal_config()
        self._frame.pack_forget()

    def on_normal_config(self):
        self._button.configure(fg_color=TAB_BTN_BG, border_width=2, border_color=TAB_BTN_BORDER_BG)

    def on_selected_config(self):
        self._button.configure(fg_color=TAB_BTN_HOVER_BG, border_width=2.5, border_color=TAB_HOVER_BTN_BORDER_BG)

    def _create_frame(self, master):
        frame = ck.CTkFrame(master, fg_color=FRAME_BG, border_width=2, border_color=FRAME_BORDER_BG,
                            width=WIN_WIDTH - SIDE_FRAME_WIDTH - SIDE_FRAME_PADDING * 4,
                            height=WIN_HEIGHT - SIDE_FRAME_PADDING * 6)
        frame.propagate(False)
        return frame

    def _create_button(self, tab_view, image, fg_color=TAB_BTN_BG, hover_color=TAB_BTN_HOVER_BG, text="",
                       corner_radius=10, border_width=2):
        button = ck.CTkButton(tab_view.buttons_frame, text=text, image=image,
                              width=TAB_BTN_WIDTH, compound="bottom", fg_color=fg_color,
                              hover_color=hover_color, corner_radius=corner_radius)
        button.configure(compound="top", border_color=TAB_BTN_BORDER_BG,
                         border_width=border_width, command=lambda tv=tab_view: self.select(tv))
        button.pack(side="left", padx=8, pady=4)

        return button
