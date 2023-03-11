import pygame
pygame.init()
class Enemy:
    def __init__(self,enemy_x_pos,enemy_y_pos,enemey_width,enemey_height,enemy_velocity):
        self.e_x = enemy_x_pos
        self.e_y = enemy_y_pos
        self.e_width = enemey_width
        self.e_height = enemey_height
        self.e_vel = enemy_velocity
    def bewegung(self,lonk_x,lonk_y):
        from main import test_surface
        if lonk_y > self.e_y:
            if lonk_x > self.e_x:
                if lonk_x - self.e_x > lonk_y - self.e_y:
                    self.e_x += self.e_vel
                elif lonk_x - self.e_x < lonk_y - self.e_y:
                    self.e_y += self.e_vel
                elif lonk_x - self.e_x == lonk_y - self.e_y:
                    self.e_y += self.e_vel/1.2
                    self.e_x += self.e_vel/1.2

            elif lonk_x < self.e_x and lonk_y > self.e_y:
                if (lonk_x - self.e_x)*-1 > lonk_y -self.e_y:
                    self.e_x -= self.e_vel
                elif (lonk_x - self.e_x)*-1 < lonk_y - self.e_y:
                    self.e_y += self.e_vel
                elif (lonk_x - self.e_x)*-1 == lonk_y - self.e_y:
                    self.e_y += self.e_vel/1.2
                    self.e_x += self.e_vel/1.2

        elif lonk_y < self.e_y:
            if lonk_x < self.e_x:
                if lonk_x - self.e_x < lonk_y - self.e_y:
                    self.e_x -= self.e_vel
                elif lonk_x - self.e_x > lonk_y - self.e_y:
                    self.e_y -= self.e_vel
                elif lonk_x - self.e_x == lonk_y - self.e_y:
                    self.e_y -= self.e_vel/1.2
                    self.e_x -= self.e_vel/1.2

            elif lonk_x > self.e_x:
                if lonk_x - self.e_x > (lonk_y - self.e_y)*-1:
                    self.e_x += self.e_vel
                elif lonk_x - self.e_x < (lonk_y - self.e_y)*-1:
                    self.e_y -= self.e_vel
                elif lonk_x - self.e_x == (lonk_y -self.e_y)*-1:
                    self.e_y += self.e_vel/1.2
                    self.e_x += self.e_vel/1.2
        pygame.draw.rect(test_surface, (255, 0, 0), (self.e_x, self.e_y, self.e_width, self.e_height)) 

