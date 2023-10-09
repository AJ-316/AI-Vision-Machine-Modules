from Tab import Tab
from AppConfigs import *


class DesktopMouseInputTab(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=ICONS[DESKTOP_MOUSE_INPUT])
        frame = self._create_frame(tab_view)

        super().__init__(DESKTOP_MOUSE_INPUT, button, frame, tab_view)
