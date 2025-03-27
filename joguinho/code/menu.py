import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, WINDOW_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pg.mixer_music.load('./asset/Menu.mp3')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            pg.display.flip()

            # Checado por todos os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
