#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_WHITE, WINDOW_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
import pygame as pg

from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        self.timeout = 20000

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player - Health: {ent.health} | Score:{ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player - Health: {ent.health} | Score:{ent.score}', C_CYAN, (10, 45))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'{self.name} - timeout: {self.timeout / 100 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WINDOW_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WINDOW_HEIGHT - 20))
            pg.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
