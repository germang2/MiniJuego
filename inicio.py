import pygame

def Menu(pantalla):
	fin = False
	fondo = pygame.image.load("textures/inicio.jpg")
	fondo = pygame.transform.scale(fondo,(1300,600))
	while not fin:
		pantalla.blit(fondo,(0,0))
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        fin = True
		    if event.type == pygame.KEYDOWN:
		    	if event.key == pygame.K_1:
		    		fin = True
		    		return 1
		    	if event.key == pygame.K_2:
		    		fin = True
		    		return 2
		    	if event.key == pygame.K_3:	
		    		fin = True
		    		return 0