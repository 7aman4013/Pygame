import pygame as pg

class Config:
    # Window
    WIDTH, HEIGHT = 800, 600
    BG_COLOR = "white"
    FPS = 60

    # Physics
    GRAVITY = pg.Vector2(0, 5000)
    FLOOR_FRICTION = 0.4
    AIR_FRICTION = 0.9
    ACC_LOSS_RATE = 0.2
    BOUNCE_FACTOR = 0.4

    # Player
    PLAYER_SIZE = 10
    PLAYER_SPEED = 100
    PLAYER_JUMP = 1500

    # Mouse
    MOUSE_FORCE = 50
    MOUSE_DASH_STEPS = 10

