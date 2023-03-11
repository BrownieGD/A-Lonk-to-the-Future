import pygame
from enemy import Enemy
from sys import exit
from Health import Health
pygame.init()
screen= pygame.display.set_mode((1000,600))
pygame.display.set_caption('Lonk to the Future')
clock = pygame.time.Clock()

test_surface = pygame.Surface((1000,600))
test_surface.fill('cyan')

Lonk = pygame.Surface((50,50)).convert_alpha()
Lonk.fill('blue')
Lonk_x_pos = 475
Lonk_y_pos = 275
vel = 5
#Objekte
enemy01 = Enemy(220,220,69,69,2)
health_bar = Health(5)


while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    #character logik
    if keys[pygame.K_w] and keys[pygame.K_a] and Lonk_y_pos>0 and Lonk_x_pos>0:
        Lonk_y_pos -= (vel/1.5)
        Lonk_x_pos -= (vel/1.5)

    elif keys[pygame.K_w] and keys[pygame.K_d] and Lonk_x_pos<950 and Lonk_y_pos>0:
        Lonk_y_pos -= (vel/1.5)
        Lonk_x_pos += (vel/1.5)

    elif keys[pygame.K_d] and keys[pygame.K_s] and Lonk_x_pos<950 and Lonk_y_pos<550:
        Lonk_y_pos += (vel/1.5)
        Lonk_x_pos += (vel/1.5)

    elif keys[pygame.K_a] and keys[pygame.K_s] and Lonk_x_pos>0 and Lonk_y_pos<550 :
        Lonk_y_pos += (vel/1.5)
        Lonk_x_pos -= (vel/1.5)
    elif keys[pygame.K_w] and Lonk_y_pos>0:
        Lonk_y_pos -= vel

    elif keys[pygame.K_s] and Lonk_y_pos<550:
        Lonk_y_pos += vel

    elif keys[pygame.K_a] and Lonk_x_pos>0:
        Lonk_x_pos -= vel

    elif keys[pygame.K_d] and Lonk_x_pos<950:
        Lonk_x_pos += vel
    #Zeichnen
    test_surface.fill((0, 0, 0))
    enemy01.bewegung(Lonk_x_pos,Lonk_y_pos)
    screen.blit(test_surface,(0,0))
    screen.blit(Lonk,(Lonk_x_pos,Lonk_y_pos))
    health_bar.render_hp()


    pygame.display.update()
    clock.tick(60)