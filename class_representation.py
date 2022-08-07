import pygame


class representation:
    def __init__(x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.dim = 1

    def set_image(dir):
        self.image = pygame.image.load(dir)

    def set_dim(a):
        if a > 1:
            self.dim = 1
        elif a < 0:
            self.dim = 0
        else:
            self.dim = a
        
    def forward():
        self.x += 1

    def backwards():
        self.x -= 1

    def represent(elem):
        elem.blit(self.image, (self.x,self.y))