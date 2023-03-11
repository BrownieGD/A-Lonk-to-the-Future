import pygame
from enemy import Enemy
from sys import exit
from Health import Health
<<<<<<< HEAD
from Char import Character
=======
from Character import Character
>>>>>>> ce6f3f5bae7da3249f809e5a0ac8f24b2ea5b9a9
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Lonk to the Future')
clock = pygame.time.Clock()


screen.fill('cyan')


#Objekte
Lonk = Character()
enemy01 = Enemy(220,220,69,69,2)
health_bar = Health(5)
player = Character()


while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
<<<<<<< HEAD
    keys = pygame.key.get_pressed()
   
    #Zeichnen
    screen.fill((0, 0, 0))
    enemy01.bewegung(player.Lonk_x_pos,player.Lonk_y_pos)
=======
    
    #Zeichnen
    test_surface.fill((0, 0, 0))
    enemy01.bewegung(Lonk.Lonk_x_pos,Lonk.Lonk_y_pos)
    
    screen.blit(test_surface,(0,0))
>>>>>>> ce6f3f5bae7da3249f809e5a0ac8f24b2ea5b9a9
    health_bar.render_hp()
    player.render_char()
    pygame.display.update()
    clock.tick(60)
    