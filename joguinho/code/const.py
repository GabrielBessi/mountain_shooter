# C
import pygame as pg

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (253, 253, 150)

# E
EVENT_ENEMY = pg.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P

PLAYER_KEY_UP = {'Player1': pg.K_UP,
                 'Player2': pg.K_w}
PLAYER_KEY_DOWN = {'Player1': pg.K_DOWN,
                   'Player2': pg.K_s}
PLAYER_KEY_LEFT = {'Player1': pg.K_LEFT,
                   'Player2': pg.K_a}
PLAYER_KEY_RIGHT = {'Player1': pg.K_RIGHT,
                    'Player2': pg.K_d}
PLAYER_KEY_SHOOT = {'Player1': pg.K_SPACE,
                    'Player2': pg.KMOD_CTRL}

# S
SPAWN_TIME = 4000

# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
