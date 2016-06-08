import pygame
from  libplataforma import *
from Enemigo import *

#https://codeshare.io/2XFWk

class Plataforma(pygame.sprite.Sprite):
    """ Plataforma donde el usuario puede subir """
    
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(VERDE)  
        self.rect = self.image.get_rect()
                                    
class Nivel(object):
    """ Esta es una superclase usada para definir un nivel
        Se crean clases hijas por cada nivel que desee emplearse """
    
    # Lista de sprites usada en todos los niveles. Add or remove
    plataforma_lista = None
    enemigos_lista = None
    
    # Imagen de Fondo
    #fondo = None
    fondo=pygame.image.load("forest.jpg")
    fondo = pygame.transform.scale(fondo,(1300,600))
    #valor desplazamiento de fondo
    mov_fondo=0
    
    def __init__(self, jugador):
        self.plataforma_lista = pygame.sprite.Group() 
        self.enemigos_lista = pygame.sprite.Group()
        self.jugador = jugador
        self.cont = 0
    
    # Actualizamos elementos en el nivel
    def update(self):
        """ Actualiza todo lo que este en este nivel."""
        self.plataforma_lista.update()
        self.enemigos_lista.update()
        #cuando el jugador choca con un pincho
        self.ls_impactos=pygame.sprite.spritecollide(self.jugador,self.enemigos_lista,False)
        for self.elemento in self.ls_impactos:
            # Verifica que sea un enemigo para poder destruirlo
            self.pospies = self.jugador.rect.height+self.jugador.rect.y-10
            if self.elemento.tipo == "enemigo":
                if self.pospies <= self.elemento.rect.y and self.jugador.bajando:
                    self.enemigos_lista.remove(self.elemento)
                    self.jugador.vel_y = 0
            
            if self.cont >= 0:
                self.cont -= 1
            else:
                self.vida.valor -= 1
                self.cont = 40
        
    def draw(self, pantalla):
        """ Dibuja lo que se encuentre en el nivel. """
        
        # Dibujamos fondo
        pantalla.fill(AZUL)
        
        pantalla.blit(self.fondo, (0,0))
        
        # Dibujamos todos los sprites en las listas
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)

    def Mover_fondo(self, mov_x):
        self.mov_fondo += mov_x
        for plataforma in self.plataforma_lista:
            plataforma.rect.x += mov_x
        for enemigo in self.enemigos_lista:
            enemigo.rect.x += mov_x

# Creamos variasplataformas para un nivel
class Nivel_01(Nivel):
    """ Definition for level 1. """
    
    def __init__(self, jugador, vida):
        """ Creamos nivel 1. """
        self.vida = vida
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-9000
        self.lvl = 1

        # Creacion de 5 pinchos ubicados en el suelo
        for i in range(5):
            pincho = Pincho()
            pincho.rect.x = (i+1)*522
            pincho.rect.y = ALTO-pincho.rect.height
            self.enemigos_lista.add(pincho)

        # Mas pinchos en otras posiciones
        pincho1 = Pincho();pincho1.rect.x = 5750;pincho1.rect.y = ALTO-pincho1.rect.height
        pincho2 = Pincho();pincho2.rect.x = 6500;pincho2.rect.y = ALTO-pincho2.rect.height
        pincho3 = Pincho();pincho3.rect.x = 7300;pincho3.rect.y = ALTO-pincho3.rect.height
        pincho4 = Pincho();pincho4.rect.x = 7822;pincho4.rect.y = ALTO-pincho4.rect.height
        self.enemigos_lista.add(pincho);self.enemigos_lista.add(pincho2);self.enemigos_lista.add(pincho3);self.enemigos_lista.add(pincho4)

        # Arreglo con x, y de las plataformas
        nivel = [ [500, 500], [800, 400], [1000, 500], [1120, 300], [1500, 500], [1650, 200], [2400, 450], [2550, 150],
                  [2750, 300], [3300, 400], [3600,400], [3800,350], [4200, 350], [4700, 370], [5450, 420], [5100, 100],
                  [5700, 100],
                 ]
            
        # Creacion de las plataformas
        for plataforma in nivel:
            bloque = Base("Objetos/pl1.png")
            bloque.rect.x = plataforma[0]
            bloque.rect.y = plataforma[1]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

        enemigos = [ [1,20,1000,430], [1,21,1500,430], [1,19,2402,380], [4,100,1850,430], [4,100,3800,450], [4,90,4400,450],
                     [1,20,3300,330], [2,20,5450,380], [2,22,5100,60], [2,18,5700,60], [3,120,6500,285], [3,50,6560,285], [3,50,6800,285],
                    ]

        for e in enemigos:
            ene = Enemigo(e[0],e[1])
            ene.rect.x = e[2]
            ene.rect.y = e[3]
            self.enemigos_lista.add(ene)        

        basesMov = [ [5000,430, 80], [5800,390,200], [5300,200,140], [7100,430,201],
                     [7400,350,198], [7700,240,196],
                    ]

    
        for b in basesMov:
            bloque = BaseMov((b[0],b[1]),b[2])
            self.plataforma_lista.add(bloque)

        masBases = [ [6500,400], [6546,400], [6592,400], [6638,400], [6684,400], [6730,400], [6776,400], [6822,400], [6868,400],
                     [6914,400], [6960,400], [7006,400],
                    ]

        for  mb in masBases:
            bloque = Base("Objetos/pl3.png")
            bloque.rect.x = mb[0]
            bloque.rect.y = mb[1]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)
            #46
        torre = [ [8500,554], [8500,508], [8500,462], [8500,416], [8500,370], [8500,324], [8500,278],
                  [8500,232], [8500,186], [8500,140],
                ]

        for t in torre:
            bloque = Base("Objetos/pl4.png")
            bloque.rect.x = t[0]
            bloque.rect.y = t[1]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """
    
    def __init__(self, jugador):
        """ Creamos nivel 2. """
        
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-1000
        self.lvl = 1
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [ [210, 50, 500, 500],
                 [210, 50, 100, 400],
                 [210, 50, 1000, 520],
                 [210, 50, 1200, 300],
                 ]
            
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

if __name__ == "__main__":
    """ Programa principal """
    pygame.init()
    tam = [ANCHO, ALTO]
    pantalla = pygame.display.set_mode(tam)
    
    pygame.display.set_caption("Ejemplo de juego de plataforma")
    
    # Creamos jugador
    jugador = Jugador()
    
    # Creamos los niveles y la vida del jugador
    nivel_lista = []
    vida = Vida()
    nivel_lista.append( Nivel_01(jugador,vida) )
    nivel_lista.append( Nivel_02(jugador) )
    
    # Establecemos nivel actual
    nivel_actual_no = 0
    nivel_actual = nivel_lista[nivel_actual_no]
    
    # Lista de sprites activos
    activos_sp_lista = pygame.sprite.Group()
    # Indicamos a la clase jugador cual es el nivel
    jugador.nivel = nivel_actual
    
    jugador.rect.x = 8000
    jugador.rect.y = ALTO - jugador.rect.height
    activos_sp_lista.add(jugador)
    
    activos_sp_lista.add(vida)

    fin = False
    
    # Controlamos que tan rapido actualizamos pantalla
    reloj = pygame.time.Clock()
    
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugador.ir_izq()
                    jugador.izquierda = True
                if event.key == pygame.K_RIGHT:
                    jugador.ir_der()
                    jugador.derecha = True
                if event.key == pygame.K_UP:
                    #print "salto"
                    jugador.salto()
                if event.key == pygame.K_q:
                    jugador.cambiarPersonaje(1)
                if event.key == pygame.K_w:
                    jugador.cambiarPersonaje(2)
                if event.key == pygame.K_e:
                    jugador.cambiarPersonaje(3)
                if event.key == pygame.K_r:
                    jugador.cambiarPersonaje(4)
                if event.key == pygame.K_t:
                    jugador.cambiarPersonaje(5)
            else:
                jugador.derecha = False
                jugador.izquierda = False
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and jugador.vel_x < 0:
                    jugador.no_mover()
                if event.key == pygame.K_RIGHT and jugador.vel_x > 0:
                    jugador.no_mover()
                    
        # Actualizamos al jugador.
        activos_sp_lista.update()

        # Actualizamos elementos en el nivel
        nivel_actual.update()
        
        #  Si el jugador se aproxima al limite derecho de la pantalla (-x)
        if jugador.rect.x >= 650:
            dif = jugador.rect.x - 650
            jugador.rect.x = 650
            nivel_actual.Mover_fondo(-dif)
            
        # Si el jugador se aproxima al limite izquierdo de la pantalla (+x)
        if jugador.rect.x <= 300:
            dif = 300 - jugador.rect.x
            jugador.rect.x = 300
            nivel_actual.Mover_fondo(dif)
            
        #Si llegamos al final del nivel
        pos_actual=jugador.rect.x + nivel_actual.mov_fondo
        if pos_actual < nivel_actual.limite:
            jugador.rect.x=300
            if nivel_actual_no < len(nivel_lista)-1:
              nivel_actual_no += 1
              nivel_actual = nivel_lista[nivel_actual_no]
              jugador.nivel=nivel_actual

        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)
        reloj.tick(60)
        pygame.display.flip()
