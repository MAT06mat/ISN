from kivy.event import EventDispatcher
from kivy.core.window import Window


class KeyboardEvent(EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_keydown)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keydown)
        self._keyboard = None

    def on_keydown(self, *args):
        pass
