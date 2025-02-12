import pygame
from pygame.locals import *

pygame.init()
HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(300,300)
player_vel = pygame.Vector2(0,0)
player_acc = pygame.Vector2(0,0)
player_size = 40
player_friction = 0.9
player_speed = 150
player_bounce = 0.5
player_mouse_force = 20
player_acc_loss_rate = 0.6


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    ###

    pygame.draw.circle(screen, "black", player_pos, player_size)

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        player_vel.y -= player_speed
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
    player_vel += player_acc * dt

    player_acc *= player_acc_loss_rate

    if event.type == pygame.MOUSEBUTTONDOWN:
        player_acc = pygame.mouse.get_pos() - player_pos
        player_acc *= player_mouse_force
    if event.type == pygame.MOUSEBUTTONUP: 
        player_acc = pygame.Vector2(0,0)
    ###

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()