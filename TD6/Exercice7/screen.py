from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from grid import Grid


Builder.load_file(".kv/box_infos.kv")


INFO_TEMPLATE = (
    "Population: {pop}\n"
    "Iteration: {it}\n"
    "Size: {w}x{h}\n"
    "Simulation rate: {rate} sim/s\n"
    "Initial life probability: {prob} %"
)


class BoxInfos(BoxLayout):
    info_text = StringProperty("")

    def __init__(self, grid: Grid, **kwargs):
        self.grid = grid
        self.grid.bind(update=self.update_info)
        self.update_info()
        super().__init__(**kwargs)

    def update_info(self, *args):
        self.info_text = INFO_TEMPLATE.format(
            pop=self.grid.population,
            it=self.grid.iteration,
            w=self.grid.GRID_SIZE[0],
            h=self.grid.GRID_SIZE[1],
            rate=self.grid.SIMULATION_RATE,
            prob=int(self.grid.INIT_LIFE_PROB * 100),
        )


class Screen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = Grid()
        self.box_infos = BoxInfos(self.grid)
        self.add_widget(self.grid)
        self.add_widget(self.box_infos)
