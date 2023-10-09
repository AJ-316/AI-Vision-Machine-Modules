import customtkinter as ck
import PIL.Image

# (light, dark)
WIN_BG = ("#F9F9F9", "#222831")
FRAME_BG = ("#EAF6F6", "#393E46")
FRAME_BORDER_BG = ("#79A8A1", FRAME_BG[1])

BUTTON_TEXT_BG = ("black", "white")
BTN_BG = ("#C8E6E6", "#0F4C75")
BTN_HOVER_BG = ("#70C8DD", "#396B8D")
BTN_BORDER_BG = ("#68A8A8", BTN_BG[1])
BTN_HOVER_BORDER_BG = (BTN_BORDER_BG[0], "#FFFFFF")

TAB_BTN_WIDTH = 64
TAB_BTN_BG = BTN_BG
TAB_BTN_HOVER_BG = BTN_HOVER_BG
TAB_BTN_DISABLE_BG = TAB_BTN_HOVER_BG
TAB_BTN_BORDER_BG = BTN_BORDER_BG
TAB_HOVER_BTN_BORDER_BG = BTN_HOVER_BORDER_BG
TAB_BTN_FRAME_BG = ("#79A8A1", "#31363E")

LOGO_BG = WIN_BG
LOGO_HOVER_BTN_BG = "#3C4149"

FONTS = {}
STYLES = {}
ICONS = {}

ICON_SIZE = (56, 56)
LOGO_SIZE = (128, 128)

WIN_HEIGHT = 720
WIN_WIDTH = 1280

SIDE_FRAME_WIDTH = 300
SIDE_FRAME_PADDING = 25

TAB_VIEW_PADDING = 12


def load_configs():
    global FONTS
    load_fonts(**{"JetBrains Mono": [16, 24], "Verdana": [14]})

    load_icons("mouse", "gym", "keyboard", "ppt", "sign_lang_letter", "sign_lang_word", size=ICON_SIZE)
    load_icons("AI_VISION", "AI_VISION_normal", size=LOGO_SIZE)


def load_fonts(**kwargs):
    for name, values in kwargs.items():
        for size in values:
            FONTS.update({f"{name}_{size}": ck.CTkFont(family=name, size=size)})


def load_icons(*icons, size):
    for icon_name in icons:
        icon_image = ck.CTkImage(light_image=PIL.Image.open("Assets/icon_" + icon_name + "_light.png"),
                                 dark_image=PIL.Image.open("Assets/icon_" + icon_name + "_dark.png"), size=size)
        ICONS.update({icon_name: icon_image})
