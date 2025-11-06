from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Line, Color
from kivy.graphics.texture import Texture
import numpy as np

from game import GameOfLife


class Grid(Widget):
    def __init__(self, game: GameOfLife, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.size_hint = None, None

        self.cols, self.rows = self.game.GRID_SIZE
        self.draw_value = None
        self.do_edit = False
        self.has_after = False

        self.texture = Texture.create(size=self.game.GRID_SIZE, colorfmt="rgba")
        self.texture.mag_filter = "nearest"
        self.texture.min_filter = "nearest"

        self.game.bind(on_update=self.update_display)

    # ------------------------------
    # Events
    # ------------------------------

    def on_touch_down(self, touch):
        if not self.do_edit or touch.is_mouse_scrolling:
            return super().on_touch_down(touch)

        x = int(touch.x // self.cell_size)
        y = int(touch.y // self.cell_size)

        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.draw_value = self.game.get_cell(x, y) ^ 1
            self.game.set_cell(x, y, self.draw_value)
            self.last_cell = (x, y)
            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if not self.do_edit or self.draw_value is None:
            return super().on_touch_move(touch)

        x = int(touch.x // self.cell_size)
        y = int(touch.y // self.cell_size)

        if 0 <= x < self.cols and 0 <= y < self.rows:
            if self.last_cell is not None:
                self.game.set_cell(x, y, self.draw_value)
                self.game.draw_line(self.last_cell, (x, y), self.draw_value)
            self.last_cell = (x, y)
            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.last_cell = None
        self.draw_value = None
        return super().on_touch_up(touch)

    # ------------------------------
    # Display
    # ------------------------------

    def update_display(self, *args, scale=None, **kwargs):
        self.size = (min(self.parent.size), min(self.parent.size))
        self.cell_size = min(self.size) / self.rows

        # Create RGBA image from numpy grid
        grid = self.game.grid * 255
        rgba = np.zeros((self.rows, self.cols, 4), dtype=np.uint8)
        rgba[..., 0:3] = grid[..., None]
        rgba[..., 3] = 255

        # Convert image in bytes and update texture
        self.texture.blit_buffer(rgba.flatten(), colorfmt="rgba", bufferfmt="ubyte")

        # Draw texture
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1)
            Rectangle(texture=self.texture, pos=self.pos, size=self.size)

        # Update black grid
        self.update_black_grid(scale)

    def update_black_grid(self, scale):
        if scale is None:
            return
        # Clear or not the black grid
        if scale < 1.5 and self.has_after:
            self.canvas.after.clear()
            self.has_after = False
            return
        # Draw of not the black grid
        if scale >= 1.5 and not self.has_after:
            with self.canvas.after:
                self.has_after = True
                Color(0, 0, 0)
                for x in range(self.game.GRID_SIZE[0] + 1):
                    Line(
                        points=(
                            (self.x + x * self.cell_size, self.y),
                            (self.x + x * self.cell_size, self.top),
                        ),
                        width=self.cell_size / 15,
                    )
                for y in range(self.game.GRID_SIZE[1] + 1):
                    Line(
                        points=(
                            (self.x, self.y + y * self.cell_size),
                            (self.right, self.y + y * self.cell_size),
                        ),
                        width=self.cell_size / 15,
                    )
