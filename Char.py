import pygame

class Character:
    def __init__(self):
        self.Lonk = pygame.Surface((50,50)).convert_alpha()
        self.Lonk.fill('blue')
        self.Lonk_x_pos = 475
        self.Lonk_y_pos = 275
        self.vel = 5
        
   
    def render_char(self):
        from main import keys, screen
        global vel
        if keys[pygame.K_w] and keys[pygame.K_a] and self.Lonk_y_pos>0 and self.Lonk_x_pos>0:
            self.Lonk_y_pos -= (self.vel/1.5)
            self.Lonk_x_pos -= (self.vel/1.5)

        elif keys[pygame.K_w] and keys[pygame.K_d] and self.Lonk_x_pos<950 and self.Lonk_y_pos>0:
            self.Lonk_y_pos -= (self.vel/1.5)
            self.Lonk_x_pos += (self.vel/1.5)

        elif keys[pygame.K_d] and keys[pygame.K_s] and self.Lonk_x_pos<950 and self.Lonk_y_pos<550:
            self.Lonk_y_pos += (self.vel/1.5)
            self.Lonk_x_pos += (self.vel/1.5)

        elif keys[pygame.K_a] and keys[pygame.K_s] and self.Lonk_x_pos>0 and self.Lonk_y_pos<550 :
            self.Lonk_y_pos += (self.vel/1.5)
            self.Lonk_x_pos -= (self.vel/1.5)
        elif keys[pygame.K_w] and self.Lonk_y_pos>0:
            self.Lonk_y_pos -= self.vel

        elif keys[pygame.K_s] and self.Lonk_y_pos<550:
            self.Lonk_y_pos += self.vel

        elif keys[pygame.K_a] and self.Lonk_x_pos>0:
            self.Lonk_x_pos -= self.vel

        elif keys[pygame.K_d] and self.Lonk_x_pos<950:
            self.Lonk_x_pos += self.vel
        screen.blit(self.Lonk,(self.Lonk_x_pos,self.Lonk_y_pos))