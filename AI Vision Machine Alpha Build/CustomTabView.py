from customtkinter.windows.widgets.appearance_mode import appearance_mode_tracker

from AppConfigs import *
from Tab import Tab


class CustomTabView(ck.CTkFrame):
    _special_tab_key = "AI_VISION"
    _top_spacing: int = 10  # px on top of the buttons
    _top_button_overhang: int = 8  # px

    def __init__(self, master: any):
        super().__init__(master=master, fg_color=WIN_BG)

        self.buttons_frame = None
        self._dict_tabs = {}
        self.current_tab = None
        self._initialize_buttons_frame()

    def cget(self, attribute_name: str) -> any:
        if attribute_name == "fg_color":
            return "transparent"
        else:
            return super().cget(attribute_name)

    def init_tabs(self):
        for tab in self._dict_tabs.values():
            tab.select(self)

        list(self._dict_tabs.values())[0].select(self)

    def add_tab(self, tab):
        self._dict_tabs.update({tab.name: tab})

    def deselect_tabs(self, except_tab: Tab = None):
        for tab in self._dict_tabs.values():
            if tab != except_tab:
                tab.deselect()

    def _initialize_buttons_frame(self):
        if self.buttons_frame is None:
            self.buttons_frame = ck.CTkFrame(self, fg_color=TAB_BUTTONS_FRAME_BG,
                                             width=WIN_WIDTH - SIDE_FRAME_WIDTH - SIDE_FRAME_PADDING * 4)
            self.buttons_frame.pack(side="top", anchor="w", padx=8, pady=8)
            self.buttons_frame.propagate(True)


