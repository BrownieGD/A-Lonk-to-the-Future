import pygame
from main import *
pygame.init()
hp = None
health_bar_font = pygame.font.Font(None,40)
health_bar_canvas = health_bar_font.render(str(hp),True,"Red")
def set_hp(Php):
    global hp
    hp = Php
health_bar_font = pygame.font.Font(None,40)
health_bar_canvas = health_bar_font.render(str(hp),True,"Red")

def render_hp():
    global hp
    health_bar_canvas = health_bar_font.render(str(hp),True,"Red")
    screen.blit(health_bar_canvas,(0,0))
    



