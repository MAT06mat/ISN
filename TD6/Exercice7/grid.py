from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import Rectangle, Line, Color
from kivy.graphics.texture import Texture

import numpy as np

from game import GameOfLife


class Grid(Widget):
    def __init__(self, game: GameOfLife, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.size_hint = (None, None)
        self.size = (dp(600), dp(600))

        self.cols, self.rows = self.game.GRID_SIZE
        self.cell_size = self.height / self.rows
        self.draw_value = None

        self.texture = Texture.create(size=self.game.GRID_SIZE, colorfmt="rgba")
        self.texture.mag_filter = "nearest"
        self.texture.min_filter = "nearest"

        self.update_display()
        self.game.bind(on_update=self.update_display)

    # ------------------------------
    # Events
    # ------------------------------

    def on_touch_down(self, touch):
        x = int(touch.x // self.cell_size)
        y = int(touch.y // self.cell_size)

        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.draw_value = self.game.get_cell(x, y) ^ 1
            self.game.set_cell(x, y, self.draw_value)
        else:
            self.game.toggle_simulation()
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        x = int(touch.x // self.cell_size)
        y = int(touch.y // self.cell_size)

        if 0 <= x < self.cols and 0 <= y < self.rows and self.draw_value is not None:
            self.game.set_cell(x, y, self.draw_value)

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.draw_value is not None:
            self.draw_value = None
        return super().on_touch_up(touch)

    # ------------------------------
    # Display
    # ------------------------------

    def update_display(self, *args):
        # Create RGBA image from numpy grid
        grid = self.game.grid * 255
        rgba = np.zeros((self.rows, self.cols, 4), dtype=np.uint8)
        rgba[..., 0:3] = grid[..., None]
        rgba[..., 3] = 255

        # Convert image in bytes and update texture
        self.texture.blit_buffer(rgba.flatten(), colorfmt="rgba", bufferfmt="ubyte")

        # Draw texture
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1)
            Rectangle(texture=self.texture, pos=self.pos, size=self.size)
            Color(0.2, 0.2, 0.2)
            Line(
                points=(
                    (self.right, self.y),
                    (self.right, self.top),
                    (self.x, self.top),
                ),
                width=1,
            )
