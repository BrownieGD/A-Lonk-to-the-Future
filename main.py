import pygame
from enemy import Enemy
from sys import exit

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

enemy01 = Enemy()

while True:
    enemy01.bewegung(Lonk_x_pos,Lonk_y_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
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
    
    screen.blit(test_surface,(0,0))
    screen.blit(Lonk,(Lonk_x_pos,Lonk_y_pos))

    pygame.display.update()
    clock.tick(60)