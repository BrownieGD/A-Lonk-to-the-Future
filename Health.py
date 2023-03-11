
import pygame
pygame.init()
class Health:
    def __init__(self,start):
        self.hp = start
        self.health_bar_font = pygame.font.Font(None,40)
        self.health_bar_canvas = self.health_bar_font.render(str(self.hp),True,"Red")
    def set_hp(self,Php):
        from main import screen
        global hp
        self.hp = Php
        self.health_bar_font = pygame.font.Font(None,40)
        self.health_bar_canvas = self.health_bar_font.render(str(self.hp),True,"Red")

    def render_hp(self):
        from main import screen
        self.health_bar_canvas = self.health_bar_font.render(str(self.hp),True,"Red")
        screen.blit(self.health_bar_canvas,(0,0))
    



