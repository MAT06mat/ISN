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
        self.selection_mode = False
        self.selection = [None, None]
        self.has_after = False

        self.texture = Texture.create(size=self.game.GRID_SIZE, colorfmt="rgba")
        self.texture.mag_filter = "nearest"
        self.texture.min_filter = "nearest"

        self.game.bind(on_update=self.update_display)

    def get_cell_pos(self, x, y):
        cell_x = int(x // self.cell_size)
        cell_y = int(y // self.cell_size)
        if 0 <= cell_x < self.cols and 0 <= cell_y < self.rows:
            return cell_x, cell_y
        return None, None

    # ------------------------------
    # Events
    # ------------------------------

    def on_touch_down(self, touch):
        if not self.do_edit or touch.is_mouse_scrolling:
            return super().on_touch_down(touch)

        x, y = self.get_cell_pos(*touch.pos)

        if x is not None:
            if self.selection_mode:
                if touch.button == "right":
                    self.selection = [None, None]
                else:
                    self.selection = [[x, y], None]
                self.update_selection()
            else:
                self.draw_value = self.game.get_cell(x, y) ^ 1
                self.game.set_cell(x, y, self.draw_value)
                self.last_cell = (x, y)
            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if not self.do_edit:
            return super().on_touch_move(touch)

        x, y = self.get_cell_pos(*touch.pos)

        if x is not None:
            if self.selection_mode and self.selection[0] is not None:
                self.selection[1] = [x, y]
                self.update_selection()
            elif self.draw_value is not None:
                if self.last_cell is not None:
                    self.game.set_cell(x, y, self.draw_value)
                    self.game.draw_line(self.last_cell, (x, y), self.draw_value)
                self.last_cell = (x, y)
            else:
                return super().on_touch_move(touch)
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.last_cell = None
        self.draw_value = None
        if self.selection_mode:
            self.update_selection()
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

        # Update the selection
        self.update_selection()

        # Update black grid
        self.update_black_grid(scale)

    def update_selection(self):
        self.canvas.after.clear()
        if self.selection_mode and self.selection[1] is not None:
            x1 = self.x + self.selection[0][0] * self.cell_size
            y1 = self.y + self.selection[0][1] * self.cell_size
            x2 = self.x + self.selection[1][0] * self.cell_size
            y2 = self.y + self.selection[1][1] * self.cell_size

            xmin = min(x1, x2)
            xmax = max(x1, x2) + self.cell_size
            ymin = min(y1, y2)
            ymax = max(y1, y2) + self.cell_size

            with self.canvas.after:
                Color(1, 0, 0)
                Line(
                    points=(
                        (xmin, ymin),
                        (xmin, ymax),
                        (xmax, ymax),
                        (xmax, ymin),
                        (xmin, ymin),
                    ),
                    width=1,
                )

    def update_black_grid(self, scale):
        if scale is None:
            return
        # Clear or not the black grid
        if scale < 1.5 and self.has_after:
            self.canvas.clear()
            self.has_after = False
            return
        # Draw of not the black grid
        if scale >= 1.5 and not self.has_after:
            with self.canvas:
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
