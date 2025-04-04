# C
import pygame as pg

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (253, 253, 150)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)


# E
EVENT_ENEMY = pg.USEREVENT + 1

EVENT_TIMEOUT = pg.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 50,
    'Enemy2Shot': 15
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 50,
    'Enemy2Shot': 1,
}

ENTITY_SHOOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200
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
PLAYER_KEY_SHOOT = {'Player1': pg.K_RCTRL,
                    'Player2': pg.K_LCTRL}

# S
SPAWN_TIME = 4000



# T
TIMEOUT_STEP = 100  # ms
TIMEOUT_LEVEL = 10000  # ms

# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324


SCORE_POS = {'Title': (WINDOW_WIDTH / 2, 50),
             'EnterName': (WINDOW_WIDTH / 2, 80),
             'Label': (WINDOW_WIDTH / 2, 90),
             'Name': (WINDOW_WIDTH / 2, 10),
             0: (WINDOW_WIDTH / 2, 110),
             1: (WINDOW_WIDTH / 2, 130),
             2: (WINDOW_WIDTH / 2, 150),
             3: (WINDOW_WIDTH / 2, 170),
             4: (WINDOW_WIDTH / 2, 190),
             5: (WINDOW_WIDTH / 2, 210),
             6: (WINDOW_WIDTH / 2, 230),
             7: (WINDOW_WIDTH / 2, 250),
             8: (WINDOW_WIDTH / 2, 270),
             9: (WINDOW_WIDTH / 2, 290)}
