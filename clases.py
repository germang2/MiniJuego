import pygame
from pygame.locals import *
import sys
from libplano import *
import os
import random
from Bresenham import *

#cargar matriz de sprites
def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo).convert_alpha()
    imagen_ancho, imagen_alto = imagen.get_size()
    #print 'ancho: ', imagen_ancho, ' xmax: ', imagen_ancho/ancho
    #print 'alto: ',imagen_alto, ' ymax: ', imagen_alto/alto
    tabla_fondos = []  
      
    for fondo_x in range(0, imagen_ancho/ancho):
       linea = []
       tabla_fondos.append(linea)
       for fondo_y in range(0, imagen_alto/alto):
            cuadro = (fondo_x * ancho, fondo_y * alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos


#Clase Jugador
class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.jugador = cargar_fondo("turtle.jpg",59,67)
		self.image = self.jugador[0][0]
		self.rect = self.image.get_rect()
		self.derecha = False
		self.izquierda = False

	def update(self):
		if self.derecha:



#clase usuario
class	Usuario(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("ship.png")
		self.rect=self.image.get_rect()		
	def posicion(self,pos):
		self.rect.x=pos[0]
		self.rect.y=pos[1]	

#clase enemigo
class	Enemigo(pygame.sprite.Sprite):
	def __init__(self, image,posinicial):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		self.direccion=0
		self.recarga=100
		self.enemigos = cargar_fondo("ene1.png", 80, 40)		
		self.disparar=False
		self.actual=0
		self.tempe1=30
		self.bandera=0
		self.image=self.enemigos[self.actual][0]
		self.puntos = circunferenciaPuntoMedio2((250,100),100)
		self.indice=posinicial*80
		self.cant = len(self.puntos)

	def update(self):
		
		if self.indice < self.cant:
			self.p = self.puntos[self.indice]
			self.rect.x = self.p[0]
			self.rect.y = self.p[1]
			self.indice+=1

		else:
			self.indice=0
				
		if self.recarga==0:
			self.recarga=100
			self.disparar=True
		else:
			self.recarga-=1		
		
		
		#tiempo de enemigos
		if self.tempe1==0:
			if self.actual<5:
				self.actual+=1
			else:
				self.actual=0
			self.image=self.enemigos[self.actual][0]
			self.tempe1=30
			
		else:
			self.tempe1-=1
		
		
	def Disparar(self):
		pass		

class	Enemigo2(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		self.direccion=0
		self.recarga=100
		self.disparar=False
		self.enemigos = cargar_fondo("ene2.png", 49, 50)		
		self.actual=0
		self.tempe1=30
		self.bandera=0
		self.image=self.enemigos[self.actual][0]
		self.indice=0
		self.x= random.randrange(200,ANCHO-100) 
		self.y= random.randrange(0,200)
		self.puntos = circunferenciaPuntoMedio((self.x,self.y),60)
		self.cant = len(self.puntos)
		self.p=self.puntos[0]		
		self.aux=0
		
	def update(self):
		if self.indice < self.cant:
			self.p = self.puntos[self.indice]
			self.rect.x = self.p[0]
			self.rect.y = self.p[1]
			self.indice+=8

		else:
			if self.aux<=8:
				self.aux+=1
				self.indice = self.aux
			else:
				self.aux=0 
				
		if self.recarga==0:
			self.recarga=100
			self.disparar=True
		else:
			self.recarga-=1		
			
		#tiempo de enemigos
		if self.tempe1==0:
			if self.actual<5:
				if self.bandera==0:
					self.actual+=1
				if self.bandera==1:
					self.actual-=1
				if self.actual==0:
					self.bandera=0	
			if self.actual==5:
				self.bandera=1
				self.actual-=1
			
				
			self.image=self.enemigos[self.actual][0]	
			self.tempe1=30
			
		else:
			self.tempe1-=1
			
	def Disparar(self):
		pass			

#Vidas del jugador			
	
class Vida(pygame.sprite.Sprite):
    def __init__(self,image):
          pygame.sprite.Sprite.__init__(self)
          self.image=pygame.image.load("vida.png")
          self.rect = self.image.get_rect()

#clase municion		
class	Municion(pygame.sprite.Sprite):
	def __init__(self, image,posicion):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("muun.png")
		self.rect=self.image.get_rect()
		self.rect.x=posicion[0]+5
		self.rect.y=posicion[1]-10
		self.bando=0
			
	def update(self):
		if self.bando==0:
			self.rect.y-=5		
		else:
			self.rect.y+=5	

#clase municion enemiga uno
class	Municionene(pygame.sprite.Sprite):
	def __init__(self, image,posicion):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("mune.png")
		self.rect=self.image.get_rect()
		self.rect.x=posicion[0]
		self.rect.y=posicion[1]
		self.bando=0
			
	def update(self):
		if self.bando==0:
			self.rect.y-=5		
		else:
			self.rect.y+=5	

#clase municion eneimga 2			
class	Municionene2(pygame.sprite.Sprite):
	def __init__(self, image,posicion,puntos_bala):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("mune2.png")
		self.rect=self.image.get_rect()
		self.rect.x=posicion[0]
		self.rect.y=posicion[1]
		self.bando=0
		self.indice=0
		self.cant = len(puntos_bala)
		self.puntos = puntos_bala
			
	def update(self):		
		p=self.puntos[self.indice]
		self.rect.x=p[0]
		self.rect.y=p[1]
		if self.indice < self.cant-1:
			self.indice+=1
		else:
			self.indice=0