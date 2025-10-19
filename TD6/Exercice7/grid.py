from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.graphics import Rectangle, Line, Color
from kivy.properties import NumericProperty, ListProperty
from kivy.graphics.texture import Texture

import numpy as np
from scipy.signal import convolve2d


class GameOfLife:
    """Game of life logic"""

    RULES = {"survive": [2, 3], "born": [3]}

    def __init__(self, size, alive_prob):
        self.rows, self.cols = size
        self.grid = (np.random.random(size) < alive_prob).astype(np.uint8)

    def toggle_cell(self, x: int, y: int):
        self.grid[y, x] ^= 1

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[y, x]

    def set_cell(self, x: int, y: int, value: int):
        self.grid[y, x] = value

    def get_population(self):
        return int(self.grid.sum())

    def count_neighbours(self):
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
        return convolve2d(self.grid, kernel, mode="same", boundary="fill", fillvalue=0)

    def step(self):
        neighbours = self.count_neighbours()

        survive_mask = np.isin(neighbours, self.RULES["survive"])
        born_mask = np.isin(neighbours, self.RULES["born"])

        survive = self.grid & survive_mask
        born = ~self.grid & born_mask
        self.grid = np.where(survive | born, 1, 0).astype(np.uint8)


class Grid(Widget):
    GRID_SIZE = ListProperty((50, 50))
    INIT_LIFE_PROB = NumericProperty(0.4)
    SIMULATION_RATE = NumericProperty(50)
    FRAME_RATE = NumericProperty(30)
    iteration = NumericProperty(0)
    population = NumericProperty(0)
    update = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(600), dp(600))

        self.cols, self.rows = self.GRID_SIZE
        self.game = GameOfLife(self.GRID_SIZE, self.INIT_LIFE_PROB)
        self.cell_size = self.height / self.rows
        self.draw_value = None

        self.texture = Texture.create(size=self.GRID_SIZE, colorfmt="rgba")
        self.texture.mag_filter = "nearest"
        self.texture.min_filter = "nearest"

        self.simulation_event = None
        self.display_event = None

        self.update_display()

    @property
    def is_running(self):
        return self.simulation_event is not None

    # ------------------------------
    # Events
    # ------------------------------

    def step(self):
        self.iteration += 1
        self.game.step()
        self.population = self.game.get_population()

    def start_simulation(self):
        if not self.is_running:
            self.step()
            self.update_display()
            self.simulation_event = Clock.schedule_interval(
                lambda dt: self.step(), 1 / self.SIMULATION_RATE
            )
            self.display_event = Clock.schedule_interval(
                lambda dt: self.update_display(),
                1 / min(self.SIMULATION_RATE, self.FRAME_RATE),
            )
            print(
                f"⏸ Simulation started ({self.SIMULATION_RATE} sim/s, {self.FRAME_RATE} fps)"
            )

    def stop_simulation(self):
        if self.simulation_event:
            self.simulation_event.cancel()
            self.simulation_event = None
        if self.display_event:
            self.display_event.cancel()
            self.display_event = None
        self.update_display()
        print("▶ Simulation stopped")

    def toggle_simulation(self):
        if self.is_running:
            self.stop_simulation()
        else:
            self.start_simulation()

    def on_touch_down(self, touch):
        x = int(touch.x // self.cell_size)
        y = int(touch.y // self.cell_size)

        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.draw_value = self.game.get_cell(x, y) ^ 1
            self.game.set_cell(x, y, self.draw_value)
            self.update_display()
        else:
            self.toggle_simulation()
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        x = int(touch.x // self.cell_size)
        y = int(touch.y // self.cell_size)

        if 0 <= x < self.cols and 0 <= y < self.rows and self.draw_value is not None:
            self.game.set_cell(x, y, self.draw_value)
            self.update_display()

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.draw_value is not None:
            self.draw_value = None
        return super().on_touch_up(touch)

    # ------------------------------
    # Display
    # ------------------------------

    def update_display(self):
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

        self.update += 1
