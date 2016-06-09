import pygame

def MostrarTutorial(pantalla):
	fin = False
	fondo = pygame.image.load("textures/tutorial.png")
	fondo = pygame.transform.scale(fondo,(1300,600))
	while not fin:
		pantalla.blit(fondo,(0,0))
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        fin = True
		    if event.type == pygame.KEYDOWN:
		    	fin = True
		    	return 0