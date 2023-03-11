import pygame
from enemy import Enemy
from sys import exit
from Health import Health
from Character import Character
pygame.init()
screen= pygame.display.set_mode((1000,600))
pygame.display.set_caption('Lonk to the Future')
clock = pygame.time.Clock()

test_surface = pygame.Surface((1000,600))
test_surface.fill('cyan')


#Objekte
Lonk = Character()
enemy01 = Enemy(220,220,69,69,2)
health_bar = Health(5)


while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Zeichnen
    test_surface.fill((0, 0, 0))
    enemy01.bewegung(Lonk.Lonk_x_pos,Lonk.Lonk_y_pos)
    
    screen.blit(test_surface,(0,0))
    health_bar.render_hp()


    pygame.display.update()
    clock.tick(60)