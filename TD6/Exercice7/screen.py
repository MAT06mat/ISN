from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

from game import GameOfLife
from keyboard_event import KeyboardEvent
from grid_container import GridContainer


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

    def update_info(self, *args):
        self.info_text = INFO_TEMPLATE.format(
            pop=self.game.population,
            it=self.game.iteration,
            w=self.game.GRID_SIZE[0],
            h=self.game.GRID_SIZE[1],
            rate=self.game.SIMULATION_RATE,
            prob=int(self.game.INIT_LIFE_PROB * 100),
        )


class Screen(BoxLayout, KeyboardEvent):
    is_editing = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = GameOfLife()
        self.grid_container = GridContainer(self.game)
        self.box_infos = BoxInfos(self.game)
        self.add_widget(self.grid_container)
        self.add_widget(self.box_infos)

    def on_keydown(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "e":
            self.toggle_editing()
        elif keycode[1] == "r":
            self.game.record.toggle()
        elif keycode[1] == "spacebar":
            self.game.toggle_simulation()
        elif keycode[1] == "c":
            self.game.clear()
        elif keycode[1] == "g":
            self.game.generate()
        return True

    def toggle_editing(self):
        self.is_editing = not self.is_editing
        print("Editing..." if self.is_editing else "Stop editing")

    def on_is_editing(self, *args):
        self.grid_container.do_translation = not self.is_editing
        self.grid_container.do_scale = not self.is_editing
        self.grid_container.grid.do_edit = self.is_editing
