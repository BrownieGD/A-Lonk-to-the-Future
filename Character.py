import pygame
pygame.init()

class Character:
        def bewegung(self,Lonk_x_pos,Lonk_y_pos,test_surface,):
            #character logik
            self.Lonk = pygame.Surface((50,50)).convert_alpha()           
            self.Lonk_x_pos = 475
            self.Lonk_y_pos = 275
            vel = 5
            keys = pygame.key.get_pressed()
            from main import test_surface
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
            pygame.draw.rect(test_surface ('blue'), (self.Lonk_x_pos,self.Lonk_y_pos))