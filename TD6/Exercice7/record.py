from kivy.event import EventDispatcher
from kivy.properties import ListProperty, BooleanProperty
import logging

logging.getLogger("matplotlib").propagate = False
logging.getLogger("PIL").setLevel(logging.INFO)

import matplotlib.pyplot as plt


class Record(EventDispatcher):
    iteration: list[int] = ListProperty([])
    population: list[int] = ListProperty([])

    active: bool = BooleanProperty(False)
    exist: bool = BooleanProperty(False)

    def start(self):
        self.iteration = []
        self.population = []
        self.active = True
        self.exist = False

    def stop(self):
        self.active = False

    def toggle(self):
        if self.active:
            self.stop()
        else:
            self.start()

    def add(self, i, p):
        if self.active:
            self.exist = True
            if i in self.iteration:
                self.population[self.iteration.index(i)] = p
            else:
                self.iteration.append(i)
                self.population.append(p)

    def open(self):
        if not self.exist:
            return
        print(">>> Display record")
        plt.plot(self.iteration, self.population)
        plt.xlabel("Iterations")
        plt.ylabel("Population")
        plt.show()
