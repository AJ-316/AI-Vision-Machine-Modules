import customtkinter as ck
from AppConfigs import *

class CustomTabView(ck.CTkBaseClass):
    _special_tab_key = "AI_VISION"
    _top_spacing: int = 10  # px on top of the buttons
    _top_button_overhang: int = 8  # px

    def __init__(self, master: any, width: int = 800, height: int = 250):
        super().__init__(master=master, bg_color="transparent", width=width, height=height)

        # shape
        self._canvas = ck.CTkCanvas(master=self,
                                    bg=self._apply_appearance_mode(self._bg_color),
                                    highlightthickness=0,
                                    width=self._apply_widget_scaling(self._desired_width),
                                    height=self._apply_widget_scaling(
                                        self._desired_height - self._top_spacing - self._top_button_overhang))
        self._draw_engine = ck.DrawEngine(self._canvas)

        # elements
        self.buttons_frame = None
        self._dict_tabs = {}
        self.current_tab = None

        tab0 = self._add_tab(self._special_tab_key, ICONS[self._special_tab_key], border_width=0,
                             corner_radius=100,
                             fg_color=LOGO_BG, hover_color=LOGO_BG)
        h0 = ck.CTkLabel(tab0, text="Home", font=FONTS["JetBrains Mono_24"])
        h0.pack()

        tab1 = self._add_tab("Desktop Mouse Input", ICONS["mouse"])
        h1 = ck.CTkLabel(tab1, text="Desktop Mouse Input", font=FONTS["JetBrains Mono_24"])
        h1.pack()

        tab2 = self._add_tab("Desktop Keyboard Input", ICONS["keyboard"])
        h2 = ck.CTkLabel(tab2, text="Desktop Keyboard Input", font=FONTS["JetBrains Mono_24"])
        h2.pack()

        tab3 = self._add_tab("Workout Reader", ICONS["gym"])
        h3 = ck.CTkLabel(tab3, text="Workout Reader", font=FONTS["JetBrains Mono_24"])
        h3.pack()

        tab4 = self._add_tab("Sign Language to Letters", ICONS["sign_lang_letter"])
        h4 = ck.CTkLabel(tab4, text="Sign Language to Letters", font=FONTS["JetBrains Mono_24"])
        h4.pack()

        tab5 = self._add_tab("Sign Language to Words", ICONS["sign_lang_word"])
        h5 = ck.CTkLabel(tab5, text="Sign Language to Words", font=FONTS["JetBrains Mono_24"])
        h5.pack()

        self.init_tabs()

    def cget(self, attribute_name: str) -> any:
        if attribute_name == "fg_color":
            return "transparent"
        else:
            return super().cget(attribute_name)

    def init_tabs(self):
        for name in self._dict_tabs.keys():
            self.select_tab(name)

        self.select_tab(list(self._dict_tabs.keys())[0])

    def _add_tab(self, name, image, text="", corner_radius=10, border_width=2, fg_color=TAB_BTN_BG,
                 hover_color=TAB_BTN_HOVER_BG):
        # Create Frame to Store tab Buttons
        self._initialize_buttons_frame()

        # Create Button for tab
        tab_button = ck.CTkButton(self.buttons_frame, text=text, image=image,
                                  width=TAB_BTN_WIDTH, compound="bottom", fg_color=fg_color,
                                  hover_color=hover_color, corner_radius=corner_radius)
        tab_button.configure(compound="top", border_color=TAB_BTN_BORDER_BG,
                             border_width=border_width, command=lambda n=name: self.select_tab(n))
        tab_button.pack(side="left", padx=8, pady=4)

        # Create Frame for tab
        tab_frame = ck.CTkFrame(self, fg_color=FRAME_BG, border_width=2, border_color=FRAME_BORDER_BG,
                                width=WIN_WIDTH - SIDE_FRAME_WIDTH - SIDE_FRAME_PADDING * 4,
                                height=WIN_HEIGHT - SIDE_FRAME_PADDING * 6)
        tab_frame.propagate(False)

        # Add Tab using button and frame
        self._dict_tabs.update({name: [tab_button, tab_frame, fg_color, hover_color]})
        if len(self._dict_tabs) == 1: self.select_tab(name)

        return tab_frame

    def select_tab(self, name: str):
        tab_button = self._dict_tabs[name][0]
        tab_button._state = "disabled"

        if name == self._special_tab_key:
            tab_button.configure(image=ICONS[self._special_tab_key])
        else:
            tab_button.configure(fg_color=self._dict_tabs[name][3],
                                 border_width=2.5, border_color=TAB_HOVER_BTN_BORDER_BG)

        self._dict_tabs[name][1].pack(fill="both", expand=True)
        self._unset_tabs(name)

    def _unset_tabs(self, except_name: str = ""):
        for name, values in self._dict_tabs.items():
            if name == except_name:
                continue
            tab_button = values[0]
            tab_button._state = "normal"

            if name == self._special_tab_key:
                tab_button.configure(image=ICONS[f"{self._special_tab_key}_normal"])
            else:
                tab_button.configure(fg_color=self._dict_tabs[name][2], border_width=2,
                                     border_color=TAB_BTN_BORDER_BG)
            values[1].pack_forget()

    def _initialize_buttons_frame(self):
        if self.buttons_frame is None:
            self.buttons_frame = ck.CTkFrame(self, fg_color="transparent",
                                             width=WIN_WIDTH - SIDE_FRAME_WIDTH - SIDE_FRAME_PADDING * 4)
            self.buttons_frame.pack(side="top", fill="x")
