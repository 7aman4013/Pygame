import pygame as pg
from pygame.locals import *
import numpy as np

pg.init()
HEIGHT = 600
WIDTH = 600
screen = pg.display.set_mode((HEIGHT,WIDTH))
clock = pg.time.Clock()
running = True
dt = 0

gravity = pg.Vector2(0,5000)

player_pos = pg.Vector2(300,300)
player_vel = pg.Vector2(0,0)
player_acc = pg.Vector2(0,0)
player_size = 10
player_friction = 0.9
player_speed = 150
player_jump = 2000
player_bounce = 0.4
player_mouse_force = 50
player_acc_loss_rate = 0.2

mouse_held_down = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_held_down = True
        if event.type == pg.MOUSEBUTTONUP or pg.mouse.get_focused() == False: 
            mouse_held_down = False
    
    screen.fill("white")

    #####

    ###
    pg.draw.circle(screen, "black", player_pos, player_size)
    
    keys = pg.key.get_pressed()

    if keys[K_w] and player_pos.y > HEIGHT - player_size * (1 + player_bounce):
        player_vel.y -= player_jump
    if keys[K_s]:
        player_vel.y += player_speed
    if keys[K_a]:
        player_vel.x -= player_speed
    if keys[K_d]:
        player_vel.x += player_speed
    
    player_pos += player_vel * dt

    if (player_pos.x) < player_size:
        player_pos.x = player_size
        player_vel.x = -player_vel.x * 2 * player_bounce
    if (player_pos.x) > WIDTH - player_size:
        player_pos.x = WIDTH - player_size
        player_vel.x = -player_vel.x * 2 * player_bounce
    if (player_pos.y) < player_size:
        player_pos.y = player_size
        player_vel.y = -player_vel.y * 2 * player_bounce
    if (player_pos.y) > HEIGHT - player_size:
        player_pos.y = HEIGHT - player_size
        player_vel.y = -player_vel.y * 2 * player_bounce
    
    player_vel = player_vel * player_friction
    player_vel += (player_acc + gravity) * dt

    player_acc *= player_acc_loss_rate

    if mouse_held_down:
        player_acc = pg.mouse.get_pos() - player_pos
        player_acc *= player_mouse_force
    else:
        player_acc = pg.Vector2(0,0)

    #####

    if mouse_held_down: 
        # pg.draw.line(screen, "black", player_pos, pg.mouse.get_pos(), 5)
        dashed_steps = 10
        mouse_pos = pg.mouse.get_pos()
        direction = (mouse_pos - player_pos).normalize()
        length = (mouse_pos - player_pos).length()
        for i in range(0, int(length), dashed_steps * 2):
            start_pos = player_pos + direction * i
            end_pos = player_pos + direction * min(i + dashed_steps, length)
            pg.draw.line(screen, "black", start_pos, end_pos, 5)

    ###

    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()