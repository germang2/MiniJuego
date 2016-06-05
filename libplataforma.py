import pygame

# Constantes

# Colores
NEGRO   = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO      = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO  = 1300
ALTO = 600
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

# Sprite de lluvia
class Lluvia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lluvia = cargar_fondo("Sprites/lluvia.png",1000,600)
        self.image = pygame.transform.scale(self.lluvia[0][0],(1300,600))
        self.rect = self.image.get_rect()
        self.ind = 0

    def update(self):
        if self.ind < 2:
            self.ind += 1
        else:
            self.ind = 0
        self.image = pygame.transform.scale(self.lluvia[self.ind][0],(1300,600))




class Jugador(pygame.sprite.Sprite):
    
    # Atributos
    # velocidad del jugador
    vel_x = 0
    vel_y = 0
    
    # Lista de elementos con los cuales chocar
    nivel = None
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bahamut = cargar_fondo("Sprites/bahamut.png",96,96)
        self.leviathan = cargar_fondo("Sprites/leviathan.png",96,96)
        self.phoenix = cargar_fondo("Sprites/phoenix.png",96,96)
        self.bear = cargar_fondo("Sprites/bear.png",72,85)
        self.ifrit = cargar_fondo("Sprites/ifrit.png",80,80)
        self.jugador = self.bear
        self.image = self.jugador[0][2]
        self.rect = self.image.get_rect()
        self.derecha = False
        self.izquierda = False
        self.cant = 3
        self.ind = 0
        self.aux = 2
        self.planear = False
        self.aum_y = -10

    def cambiarPersonaje(self,pj):
        if pj == 1:
            self.jugador = self.bahamut
        elif pj == 2:
            self.jugador = self.leviathan
        elif pj == 3:
            self.jugador = self.phoenix
            self.planear = True
        elif pj == 4:
            self.jugador = self.bear
        elif pj == 5:
            self.jugador = self.ifrit
            self.aum_y = -15
        else:
            self.jugador = self.bear
        if pj != 3:
            self.planear = False
        if pj != 5:
            self.aum_y = -10
        

    def update(self):

        """ Movimiento de Sprite """
        if self.ind < self.cant:
            self.ind += 1
        else:
            self.ind = 0

        if self.derecha:
            self.aux = 2
        elif self.izquierda:
            self.aux = 1
        else:
            self.ind = 0

        self.image = self.jugador[self.ind][self.aux]

        """ Mueve el jugador. """
        # Gravedad
        self.calc_grav()
        
        # Mover izq/der
        self.rect.x += self.vel_x
        
        # Revisar si golpeamos con algo (bloques con colision)
        bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in bloque_col_list:
            # Si nos movemos a la derecha,
            # ubicar jugador a la izquierda del objeto golpeado
            if self.vel_x > 0:
                self.rect.right = bloque.rect.left
            elif self.vel_x < 0:
                # De otra forma nos movemos a la izquierda
                self.rect.left = bloque.rect.right
        
        # Mover arriba/abajo
        self.rect.y += self.vel_y
        
        # Revisamos si chocamos
        bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in bloque_col_list:
            
            # Reiniciamos posicion basado en el arriba/bajo del objeto
            if self.vel_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.vel_y < 0:
                self.rect.top = bloque.rect.bottom
            
            # Detener movimiento vertical
            self.vel_y = 0
            
            
    def calc_grav(self):
        """ Calculamos efecto de la gravedad. """
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            if self.vel_y >= 0 and self.planear:
                self.vel_y += .08
            else:    
                self.vel_y += .35
        
        # Revisamos si estamos en el suelo
        if self.rect.y >= ALTO - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = ALTO - self.rect.height
            
    def salto(self):
        """ saltamos al pulsar boton de salto """
        #print "en salto"
        # Nos movemos abajo un poco y revisamos si hay una plataforma bajo el jugador
        self.rect.y += 2
        plataforma_col_lista = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        self.rect.y -= 2
        
        # Si es posible saltar, aumentamos velocidad hacia arriba
        if len(plataforma_col_lista) > 0 or self.rect.bottom >= ALTO:
            self.vel_y = self.aum_y
            
    # Control del movimiento
    def ir_izq(self):
        """ Usuario pulsa flecha izquierda """
        self.vel_x = -6

    def ir_der(self):
        """ Usuario pulsa flecha derecha """
        self.vel_x = 6

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.vel_x = 0

class Pincho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Objetos/pinchos.png").convert_alpha()
        self.rect = self.image.get_rect()

class Base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Objetos/pl1.png").convert_alpha()
        self.rect = self.image.get_rect()

class Vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.valor = 20

    def update(self):
        if self.valor == 20:
            self.image = pygame.image.load("textures/health_20.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 19:
            self.image = pygame.image.load("textures/health_19.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 18:
            self.image = pygame.image.load("textures/health_18.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 17:
            self.image = pygame.image.load("textures/health_17.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 16:
            self.image = pygame.image.load("textures/health_16.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 15:
            self.image = pygame.image.load("textures/health_15.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 14:
            self.image = pygame.image.load("textures/health_14.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 13:
            self.image = pygame.image.load("textures/health_13.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 12:
            self.image = pygame.image.load("textures/health_12.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 11:
            self.image = pygame.image.load("textures/health_11.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 10:
            self.image = pygame.image.load("textures/health_10.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 9:
            self.image = pygame.image.load("textures/health_9.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 8:
            self.image = pygame.image.load("textures/health_8.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 7:
            self.image = pygame.image.load("textures/health_7.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 6:
            self.image = pygame.image.load("textures/health_6.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 5:
            self.image = pygame.image.load("textures/health_5.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 4:
            self.image = pygame.image.load("textures/health_4.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 3:
            self.image = pygame.image.load("textures/health_3.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 2:
            self.image = pygame.image.load("textures/health_2.png").convert_alpha()
            self.rect = self.image.get_rect()
        elif self.valor == 1:
            self.image = pygame.image.load("textures/health_1.png").convert_alpha()
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load("textures/health_0.png").convert_alpha()
            self.rect = self.image.get_rect()  
        self.rect.x = 30
        self.rect.y = 40