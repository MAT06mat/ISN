from kivy.uix.scatterlayout import ScatterLayout
from kivy.graphics.transformation import Matrix

from grid import Grid
from game import GameOfLife


class GridContainer(ScatterLayout):
    do_rotation = False

    def __init__(self, game: GameOfLife, **kw):
        super().__init__(**kw)
        self.scale = 1
        self.scale_min = 1
        self.scale_max = 15
        self.auto_bring_to_front = False
        self.grid = Grid(game)
        self.add_widget(self.grid)

    def on_bbox(self, *args):
        m = min(self.size)
        max_x = int((self.width - m) / 2)
        min_x = int((3 * self.width - m) / 2)
        max_y = int((self.height - m) / 2)
        min_y = int((3 * self.height - m) / 2)

        if int(self.x) > max_x:
            self.x = max_x
        if int(self.top) < min_y:
            self.top = min_y
        if int(self.y) > max_y:
            self.y = max_y
        if int(self.right) < min_x:
            self.right = min_x

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling and not self.parent.is_editing:
            if touch.button == "scrolldown":
                if self.scale * 1.1 < self.scale_max:
                    self.apply_transform(
                        Matrix().scale(1.1, 1.1, 1.1), anchor=touch.pos
                    )
                return True
            elif touch.button == "scrollup":
                if self.scale * 0.91 > self.scale_min:
                    self.apply_transform(
                        Matrix().scale(0.91, 0.91, 0.91), anchor=touch.pos
                    )
                else:
                    self.scale = self.scale_min
                return True
        return super().on_touch_down(touch)
