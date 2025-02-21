import pygame as pg
from config import Config
from player import Player

class Game: 
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player(300, 300)
        self.running = True
        self.dt = 0
        self.mouse_held = False
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_held = True
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_held = False
    
    def calculate_mouse_force(self):
        if self.mouse_held:
            mouse_pos = pg.mouse.get_pos()
            direction = mouse_pos - self.player.pos
            return direction * Config.MOUSE_FORCE
        return pg.Vector2(0,0)

    def draw_mouse_line(self):
        if self.mouse_held:
            mouse_pos = pg.mouse.get_pos()
            direction = (mouse_pos - self.player.pos).normalize()
            length = (mouse_pos - self.player.pos).length()
            
            for i in range(0, int(length), Config.MOUSE_DASH_STEPS * 2):
                start = self.player.pos + direction * i
                end = self.player.pos + direction * min(i + Config.MOUSE_DASH_STEPS, length)
                pg.draw.line(self.screen, "black", start, end, 5)

    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(Config.BG_COLOR)
            
            mouse_force = self.calculate_mouse_force()
            self.player.update(self.dt, mouse_force)
            
            self.player.draw(self.screen)
            self.draw_mouse_line()
            
            pg.display.flip()
            self.dt = self.clock.tick(Config.FPS) / 1000
        
        pg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()