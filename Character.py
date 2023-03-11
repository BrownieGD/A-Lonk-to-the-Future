from main import *
import pygame

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
    

screen.blit(Lonk,(Lonk_x_pos,Lonk_y_pos))
