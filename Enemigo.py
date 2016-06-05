import pygame
from  libplataforma import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, num):
        pygame.sprite.Sprite.__init__(self)
        if num == 1:
			self.enemigo = cargar_fondo("Sprites/moco.png",107,77)
			self.cant = 7
        elif num == 3:
        	self.enemigo = cargar_fondo("Sprites/burro.png",106,132)
        	self.cant = 5
        elif num == 4:
        	self.enemigo = cargar_fondo("Sprites/pig.png",120,138)
        	self.cant = 3
        elif num == 2:
        	self.enemigo = cargar_fondo("Sprites/raton.png",109,60)
        	self.cant = 7
        else:
        	self.enemigo = cargar_fondo("Sprites/cave.png",246,255)
        	self.cant = 14
        self.image = self.enemigo[0][0]
        self.rect = self.image.get_rect()
        self.ind = 0

    def update(self):
    	if self.ind < self.cant:
            self.ind += 1
        else:
            self.ind = 0
        self.image = self.enemigo[self.ind][1]