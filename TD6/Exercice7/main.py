from kivy.app import App
from screen import Screen


class GameOfLifeApp(App):
    title = "The game of life"

    def build(self):
        return Screen()


if __name__ == "__main__":
    GameOfLifeApp().run()
