from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

from game import GameOfLife
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

    def __init__(self, game: GameOfLife, **kwargs):
        self.game = game
        self.game.bind(on_update=self.update_info)
        self.update_info()
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.game.toggle_simulation()
        return super().on_touch_down(touch)

    def update_info(self, *args):
        self.info_text = INFO_TEMPLATE.format(
            pop=self.game.population,
            it=self.game.iteration,
            w=self.game.GRID_SIZE[0],
            h=self.game.GRID_SIZE[1],
            rate=self.game.SIMULATION_RATE,
            prob=int(self.game.INIT_LIFE_PROB * 100),
        )


class Screen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = GameOfLife()
        self.grid = Grid(self.game)
        self.box_infos = BoxInfos(self.game)
        self.add_widget(self.grid)
        self.add_widget(self.box_infos)
