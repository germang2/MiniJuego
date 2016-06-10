import pygame

def pausarJuego(pantalla):
	fin = False
	fondo = pygame.image.load("textures/pausa.jpg")
	while not fin:
		pantalla.blit(fondo,(0,0))
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        fin = True
		        return -1,False
		    if event.type == pygame.KEYDOWN:
		    	if event.key == pygame.K_1:
		    		fin = True
		    		return 2,False
		    	elif event.key == pygame.K_2:
		    		fin = True
		    		return 1,False
		    	elif event.key == pygame.K_3:	
		    		fin = True
		    		return -1,False
		    	else:
		    		None
		pygame.display.flip()