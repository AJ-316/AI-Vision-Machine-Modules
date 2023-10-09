from Tab import Tab
from AppConfigs import *


class AIVisionMachineHome(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=ICONS[AI_VISION_MACHINE], hover_color=LOGO_BG, border_width=0)
        frame = self._create_frame(tab_view)

        super().__init__(AI_VISION_MACHINE, button, frame, tab_view)

    def on_normal_config(self):
        self._button.configure(image=ICONS[f"{self.name}_normal"],
                               fg_color="transparent", hover_color=LOGO_BG)

    def on_selected_config(self):
        self._button.configure(image=ICONS[self.name],
                               fg_color="transparent", hover_color=LOGO_HOVER_BTN_BG)
