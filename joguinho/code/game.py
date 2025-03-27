import pygame as pg

from code.level import Level
from code.menu import Menu
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):  # Construtor
        pg.init()
        self.window = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pg.quit()  # Fecha Janela
                quit()  # Finaliza o jogo
            else:
                pass
