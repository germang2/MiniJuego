import pygame
from  libplataforma import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, num, dist):
        pygame.sprite.Sprite.__init__(self)
        self.mover = True
        self.distancia = dist
        self.tipo = "enemigo"
        if num == 1:
			self.enemigo = cargar_fondo("Sprites/moco.png",107,77)
			self.cant = 7
        elif num == 3:
        	self.enemigo = cargar_fondo("Sprites/burro.png",106,131)
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
        self.lado = 1
        self.aux = 0
        self.cont = 0

    def caminar(self):
        if self.mover == True:            
            if self.cont <= self.distancia:
                self.cont += 1
            else:
                self.cont = 0
                if self.lado == 1:
                    self.lado = 0
                else:
                    self.lado = 1
            if self.lado == 1:
                self.aum = 4
            else:
                self.aum = -4
            self.rect.x += self.aum

    def update(self):
    	if self.ind < self.cant:
            self.ind += 1
        else:
            self.ind = 0
        if self.lado == 1:
            self.aux = 0
        else:
            self.aux = 1
        
        self.caminar()
        self.image = self.enemigo[self.ind][self.aux]
