from kivy.event import EventDispatcher
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty,
    ListProperty,
    AliasProperty,
    ObjectProperty,
    BoundedNumericProperty,
)
import numpy as np
from scipy.signal import convolve2d

from record import Record


class GameOfLife(EventDispatcher):
    """Game of Life logic"""

    # ------------------------------
    # Class constants & Kivy properties
    # ------------------------------

    RULES = {"survive": [2, 3], "born": [3]}
    GRID_SIZE: list[int] = ListProperty((100, 100))
    INIT_LIFE_PROB: float = NumericProperty(0.3)
    SIMULATION_RATE: int = BoundedNumericProperty(30, min=1, errorvalue=1)
    FRAME_RATE: int = NumericProperty(30)

    iteration: int = NumericProperty(0)
    population: int = NumericProperty(0)

    record: Record = ObjectProperty(Record())

    simulation_event = ObjectProperty(None, allownone=True)
    display_event = ObjectProperty(None, allownone=True)

    # ------------------------------
    # Initialization
    # ------------------------------

    def __init__(self):
        self.register_event_type("on_update")
        self.bind(SIMULATION_RATE=self._on_simulation_rate)
        self.generate()

    # ------------------------------
    # Properties and helpers
    # ------------------------------

    def _is_running(self):
        return self.simulation_event is not None

    is_running = AliasProperty(_is_running, bind=["simulation_event"])

    def _update_population(self):
        self.population = int(self.grid.sum())

    # ------------------------------
    # Update and event handling
    # ------------------------------

    def _update(self, *args):
        self._update_population()
        self.dispatch("on_update")

    def _on_simulation_rate(self, *args):
        if self.is_running:
            self.delete_events()
            self.create_events()
        self._update()

    def on_update(self, *args):
        """Triggered each frame (UI binding point)."""
        pass

    # ------------------------------
    # Cell manipulation
    # ------------------------------

    def toggle_cell(self, x: int, y: int):
        self.grid[y, x] ^= 1
        self._update()

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[y, x]

    def set_cell(self, x: int, y: int, value: int):
        if self.grid[y, x] != value:
            self.grid[y, x] = value
            self._update()

    def draw_line(self, start, end, value):
        """Draw a line of live/dead cells using Bresenham's algorithm."""
        x0, y0 = start
        x1, y1 = end

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while x0 != x1 or y0 != y1:
            self.set_cell(x0, y0, value)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        self.set_cell(x1, y1, value)

    def clear(self):
        self.grid = np.zeros(self.GRID_SIZE).astype(np.uint8)
        self._update()

    def generate(self):
        self.grid = (np.random.random(self.GRID_SIZE) < self.INIT_LIFE_PROB).astype(
            np.uint8
        )
        self._update()

    # ------------------------------
    # Simulation logic
    # ------------------------------

    def count_neighbours(self):
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
        return convolve2d(self.grid, kernel, mode="same", boundary="fill", fillvalue=0)

    def step(self, *args):
        """Advance the simulation by one step."""
        self.iteration += 1
        neighbours = self.count_neighbours()

        survive_mask = np.isin(neighbours, self.RULES["survive"])
        born_mask = np.isin(neighbours, self.RULES["born"])

        survive = self.grid & survive_mask
        born = ~self.grid & born_mask
        self.grid = np.where(survive | born, 1, 0).astype(np.uint8)
        self.record.add(self.iteration, self.population)

    # ------------------------------
    # Simulation control (start / stop / toggle)
    # ------------------------------

    def create_events(self):
        """Create the simulation and display update events."""
        if self.is_running:
            return
        self.simulation_event = Clock.schedule_interval(
            self.step, 1 / self.SIMULATION_RATE
        )
        self.display_event = Clock.schedule_interval(
            self._update,
            1 / min(self.SIMULATION_RATE, self.FRAME_RATE),
        )

    def delete_events(self):
        """Cancel all running events."""
        if self.simulation_event:
            self.simulation_event.cancel()
            self.simulation_event = None
        if self.display_event:
            self.display_event.cancel()
            self.display_event = None

    def start_simulation(self):
        """Start the simulation."""
        if self.is_running:
            return
        self.step()
        self._update()
        self.create_events()
        print(
            f"⏸ Simulation started ({self.SIMULATION_RATE} sim/s, {self.FRAME_RATE} fps)"
        )

    def stop_simulation(self):
        """Stop the simulation."""
        self.delete_events()
        self._update()
        print("▶ Simulation stopped")

    def toggle_simulation(self):
        """Toggle between start and stop states."""
        if self.is_running:
            self.stop_simulation()
        else:
            self.start_simulation()
