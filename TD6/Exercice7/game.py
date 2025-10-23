from kivy.event import EventDispatcher
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty, AliasProperty, ObjectProperty
import numpy as np
from scipy.signal import convolve2d


class GameOfLife(EventDispatcher):
    """Game of life logic"""

    RULES = {"survive": [2, 3], "born": [3]}
    GRID_SIZE: list[int] = ListProperty((50, 50))
    INIT_LIFE_PROB: float = NumericProperty(0.3)
    SIMULATION_RATE: int = NumericProperty(50)
    FRAME_RATE: int = NumericProperty(30)

    iteration: int = NumericProperty(0)
    population: int = NumericProperty(0)

    simulation_event = ObjectProperty(None, allownone=True)
    display_event = ObjectProperty(None, allownone=True)

    def _is_running(self):
        return self.simulation_event is not None

    is_running = AliasProperty(_is_running, bind=["simulation_event"])

    def _update_population(self):
        self.population = int(self.grid.sum())

    def _update(self, *args):
        self._update_population()
        self.dispatch("on_update")

    def __init__(self):
        size = self.GRID_SIZE
        self.rows, self.cols = size
        self.grid = (np.random.random(size) < self.INIT_LIFE_PROB).astype(np.uint8)
        self._update_population()
        self.register_event_type("on_update")

    def on_update(self, *args):
        pass

    def toggle_cell(self, x: int, y: int):
        self.grid[y, x] ^= 1
        self._update()

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[y, x]

    def set_cell(self, x: int, y: int, value: int):
        if self.grid[y, x] != value:
            self.grid[y, x] = value
            self._update()

    def count_neighbours(self):
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
        return convolve2d(self.grid, kernel, mode="same", boundary="fill", fillvalue=0)

    def step(self, *args):
        self.iteration += 1
        neighbours = self.count_neighbours()

        survive_mask = np.isin(neighbours, self.RULES["survive"])
        born_mask = np.isin(neighbours, self.RULES["born"])

        survive = self.grid & survive_mask
        born = ~self.grid & born_mask
        self.grid = np.where(survive | born, 1, 0).astype(np.uint8)

    def start_simulation(self):
        if not self.is_running:
            self.step()
            self._update()
            self.simulation_event = Clock.schedule_interval(
                self.step, 1 / self.SIMULATION_RATE
            )
            self.display_event = Clock.schedule_interval(
                self._update,
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
        self._update()
        print("▶ Simulation stopped")

    def toggle_simulation(self):
        if self.is_running:
            self.stop_simulation()
        else:
            self.start_simulation()
