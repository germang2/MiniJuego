import pygame

AZUL     = (   0,   0, 255)

def Menu(pantalla):
	fin = False
	fondo = pygame.image.load("textures/inicio.jpg").convert_alpha()
	fondo = pygame.transform.scale(fondo,(1300,600))
	while not fin:
		#pantalla.fill(fondo,(1300,600))
		pantalla.blit(fondo,(0,0))
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        fin = True
		    if event.type == pygame.KEYDOWN:
		    	if event.key == pygame.K_1:
		    		fin = True
		    		return 1
		    	elif event.key == pygame.K_2:
		    		fin = True
		    		return 2
		    	elif event.key == pygame.K_3:	
		    		fin = True
		    		return 0
		pygame.display.flip()
		    	