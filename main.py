import pygame
from enemy import Enemy
from sys import exit
from Health import Health
from Char import Character
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Lonk to the Future')
clock = pygame.time.Clock()


screen.fill('cyan')

Lonk = pygame.Surface((50,50)).convert_alpha()
Lonk.fill('blue')
Lonk_x_pos = 475
Lonk_y_pos = 275
vel = 5
#Objekte
enemy01 = Enemy(220,220,69,69,2)
health_bar = Health(5)
player = Character()


while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
   
    #Zeichnen
    screen.fill((0, 0, 0))
    enemy01.bewegung(player.Lonk_x_pos,player.Lonk_y_pos)
    health_bar.render_hp()
    player.render_char()
    pygame.display.update()
    clock.tick(60)
    