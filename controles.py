import pygame

AZUL = (0,255,255)
BLANCO = (255,255,255)

class Control:
	def __init__(self):
		self.izq = pygame.K_LEFT
		self.der = pygame.K_RIGHT
		self.arriba = pygame.K_UP
		self.bahamut = pygame.K_q
		self.leviathan = pygame.K_w
		self.phoenix = pygame.K_e
		self.oso = pygame.K_r
		self.buey = pygame.K_t

	def menuControl(self,pantalla):
		fin = False
		fondo = pygame.image.load("textures/controles.jpg")
		cont = 1
		fuente = pygame.font.Font(None, 30)
		texto1 = fuente.render("TECLA IZQUIERDA", 0, AZUL)
		texto12 = fuente.render("",0,BLANCO)
		texto2 = fuente.render("TECLA DERECHA", 0, AZUL)
		texto22 = fuente.render("",0,BLANCO)
		texto3 = fuente.render("TECLA ARRIBA", 0, AZUL)
		texto32 = fuente.render("",0,BLANCO)
		texto4 = fuente.render("TECLA BAHAMUT", 0, AZUL)
		texto42 = fuente.render("",0,BLANCO)
		texto5 = fuente.render("TECLA LEVIATHAN", 0, AZUL)
		texto52 = fuente.render("",0,BLANCO)
		texto6 = fuente.render("TECLA PHOENIX", 0, AZUL)
		texto62 = fuente.render("",0,BLANCO)
		texto7 = fuente.render("TECLA OSO", 0, AZUL)
		texto72 = fuente.render("",0,BLANCO)
		texto8 = fuente.render("TECLA BUEY", 0, AZUL)
		texto82 = fuente.render("",0,BLANCO)
		texto9 = fuente.render("", 0, BLANCO)
		while not fin:
			pantalla.blit(fondo,(0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					fin = True
					return -1
				if event.type == pygame.KEYDOWN:
					if cont == 1:
						texto1 = fuente.render("TECLA IZQUIERDA", 0, BLANCO)
						texto12 = fuente.render(event.unicode,0,BLANCO)
						self.izq = event.key
						cont += 1
					elif cont == 2:
						texto2 = fuente.render("TECLA DERECHA", 0, BLANCO)
						texto22 = fuente.render(event.unicode,0,BLANCO)
						self.der = event.key
						cont += 1
					elif cont == 3:
						texto3 = fuente.render("TECLA ARRIBA", 0, BLANCO)
						texto32 = fuente.render(event.unicode,0,BLANCO)
						self.arriba = event.key
						cont += 1
					elif cont == 4:
						texto4 = fuente.render("TECLA BAHAMUT", 0, BLANCO)
						texto42 = fuente.render(event.unicode,0,BLANCO)
						self.bahamut = event.key
						cont += 1
					elif cont == 5:
						texto5 = fuente.render("TECLA LEVIATHAN", 0, BLANCO)
						texto52 = fuente.render(event.unicode,0,BLANCO)
						self.leviathan = event.key
						cont += 1
					elif cont == 6:
						texto6 = fuente.render("TECLA PHOENIX", 0, BLANCO)
						texto62 = fuente.render(event.unicode,0,BLANCO)
						self.phoenix = event.key
						cont += 1
					elif cont == 7:
						texto7 = fuente.render("TECLA OSO", 0, BLANCO)
						texto72 = fuente.render(event.unicode,0,BLANCO)
						self.oso = event.key
						cont += 1
					elif cont == 8:
						texto8 = fuente.render("TECLA BUEY", 0, BLANCO)
						texto82 = fuente.render(event.unicode,0,BLANCO)
						self.buey = event.key
						texto9 = fuente.render("Presione tecla ESCAPE para salir", 0, BLANCO)
						cont += 1
					elif event.key == pygame.K_ESCAPE and cont == 9:
						fin = True
						return 0
					else:
						None
				    
			
			pantalla.blit(texto1, (300,150))
			pantalla.blit(texto12, (600,150))
			pantalla.blit(texto2, (300,200))
			pantalla.blit(texto22, (600,200))
			pantalla.blit(texto3, (300,250))
			pantalla.blit(texto32, (600,250))
			pantalla.blit(texto4, (300,300))
			pantalla.blit(texto42, (600,300))
			pantalla.blit(texto5, (300,350))
			pantalla.blit(texto52, (600,350))
			pantalla.blit(texto6, (300,400))
			pantalla.blit(texto62, (600,400))
			pantalla.blit(texto7, (300,450))
			pantalla.blit(texto72, (600,450))
			pantalla.blit(texto8, (300,500))
			pantalla.blit(texto82, (600,500))
			pantalla.blit(texto9, (400,550))
			pygame.display.flip()
