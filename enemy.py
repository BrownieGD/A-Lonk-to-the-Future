import pygame
from main import *
pygame.init()
class Enemy:
    def __init__(self):
        self.e_x = 250
        self.e_y = 250
        self.e_width = 20
        self.e_height = 20
        self.e_vel = 1
    def bewegung(self,lonk_x,lonk_y):
        if lonk_y > e_y:
            if lonk_x > self.e_x:
                if lonk_x - e_x > lonk_y - self.e_y:
                    self.e_x += self.e_vel
                elif lonk_x - self.e_x < lonk_y - self.e_y:
                    self.e_y += self.e_vel
                elif lonk_x - e_x == lonk_y - self.e_y:
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
