import pygame as pg
from config import Config

class Player:
    def __init__(self, x ,y):
        self.pos = pg.Vector2(x, y)
        self.vel = pg.Vector2(0, 0)
        self.acc = pg.Vector2(0, 0)
        self.config = Config()
    
    def apply_force(self, force):
        self.acc += force
    
    def handle_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self.on_ground():
            self.vel.y -= self.config.PLAYER_JUMP
        if keys[pg.K_s]:
            self.vel.y += self.config.PLAYER_JUMP
        if keys[pg.K_a]:
            self.vel.x -= self.config.PLAYER_SPEED
        if keys[pg.K_d]:
            self.vel.x += self.config.PLAYER_SPEED
    
    def on_ground(self):
        return self.pos.y >= self.config.HEIGHT - self.config.PLAYER_SIZE

    def on_ground_lenient(self):
        return self.pos.y >= self.config.HEIGHT - self.config.PLAYER_SIZE * (1 + self.config.BOUNCE_FACTOR)
    
    def update(self, dt, mouse_force = None):
        self.handle_input()

        # Physics
        self.vel += (self.acc + self.config.GRAVITY) * dt
        self.pos += self.vel * dt
        self.vel *= self.config.FLOOR_FRICTION if self.on_ground() else self.config.AIR_FRICTION
        self.acc *= self.config.ACC_LOSS_RATE

        if mouse_force:
            self.apply_force(mouse_force)
        
        self.handle_boundaries()
    
    def handle_boundaries(self):
        cfg = self.config
        for i in range(2):
            axis = 'x' if i == 0 else 'y'
            pos = getattr(self.pos, axis)
            vel = getattr(self.vel, axis)
            
            if pos < cfg.PLAYER_SIZE:
                setattr(self.pos, axis, cfg.PLAYER_SIZE)
                setattr(self.vel, axis, -vel * 2 * cfg.BOUNCE_FACTOR)
            elif pos > (cfg.WIDTH if i == 0 else cfg.HEIGHT) - cfg.PLAYER_SIZE:
                setattr(self.pos, axis, (cfg.WIDTH if i == 0 else cfg.HEIGHT) - cfg.PLAYER_SIZE)
                setattr(self.vel, axis, -vel * 2 * cfg.BOUNCE_FACTOR)
    
    def draw(self, surface):
        pg.draw.circle(surface, "black", self.pos, self.config.PLAYER_SIZE)