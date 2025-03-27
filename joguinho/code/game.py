import pygame as pg
from code.menu import Menu
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT


class Game:
    def __init__(self):  # Construtor
        pg.init()
        self.window = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
