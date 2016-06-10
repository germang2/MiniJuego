import pygame
from  libplataforma import *
from Enemigo import *
from inicio import *
from tutorial import *
from controles import *
from pausa import *

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
    fondo = pygame.image.load("forest.jpg")
    fondo = pygame.transform.scale(fondo,(1300,600))
    #valor desplazamiento de fondo
    mov_fondo=0
    
    def __init__(self, jugador):
        self.plataforma_lista = pygame.sprite.Group() 
        self.enemigos_lista = pygame.sprite.Group()
        self.jugador = jugador
        self.cont = 4
        self.puntos = 0
        self.fuente = pygame.font.Font(None, 30)
        self.texto = self.fuente.render("Puntos: "+str(self.puntos), 0, BLANCO)

    # Actualizamos elementos en el nivel
    def update(self):
        """ Actualiza todo lo que este en este nivel."""
        self.plataforma_lista.update()
        self.enemigos_lista.update()
        self.ls_impactos=pygame.sprite.spritecollide(self.jugador,self.enemigos_lista,False)
        for self.elemento in self.ls_impactos:
            # Verifica que sea un enemigo para poder destruirlo
            self.pospies = self.jugador.rect.height+self.jugador.rect.y-10
            if self.elemento.tipo == "enemigo" or self.elemento.tipo == "jefe":
                if self.pospies <= self.elemento.rect.y and self.jugador.bajando:
                    self.enemigos_lista.remove(self.elemento)
                    self.jugador.vel_y = 0
                    self.puntos += 200
                    self.texto = self.fuente.render("Puntos: "+str(self.puntos), 0, BLANCO)

                    if self.elemento.tipo == "jefe":
                        self.cont -= 1
            
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
        pantalla.blit(self.texto, (1150, 50))
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
        nivel = [ [500, 500], [770, 400], [1000, 500], [1120, 250], [1500, 500], [1700, 200], [2400, 450], [2550, 150],
                  [3000,500], [3300, 380], [3600,380], [3800,350], [4200, 350], [4700, 370], [5450, 460], [5100, 100], [5700, 100],
                 ]
            
        # Creacion de las plataformas
        for plataforma in nivel:
            bloque = Base("Objetos/pl1.png")
            bloque.rect.x = plataforma[0]
            bloque.rect.y = plataforma[1]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

        enemigos = [ [1,20,1000,430], [1,21,1500,430], [1,19,2402,380], [4,100,1850,482], [4,100,3800,482], [4,90,4400,482],
                     [1,20,3300,310], [2,20,5450,420], [2,22,5100,60], [2,18,5700,60], [3,120,6500,285], [3,50,6560,285], [3,50,6800,285],
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
            
        torre = [ [8500,554], [8500,508], [8500,462], [8500,416], [8500,370], [8500,324], [8500,278],
                  [8500,232], [8500,186], [8500,140],
                ]

        for t in torre:
            bloque = Base("Objetos/pl4.png")
            bloque.rect.x = t[0]
            bloque.rect.y = t[1]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)


        posBoss = [ [8720,300], [9000,400], [9350,400], [9630,300],
                    ]
        for pb in posBoss:
            boss = Enemigo(5,0)
            boss.rect.x = pb[0]
            boss.rect.y = pb[1]
            self.enemigos_lista.add(boss)

        bloquesBoss = [ [8720,400], [9000,500], [9350,500], [9630,400],
                        ]

        for bb in bloquesBoss:
            bloque = Base("Objetos/pl2.png")
            bloque.rect.x = bb[0]
            bloque.rect.y = bb[1]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

        bloque = BaseMov((9000,160),100)
        self.plataforma_lista.add(bloque)

if __name__ == "__main__":
    """ Programa principal """
    pygame.init()
    tam = [ANCHO, ALTO]
    pantalla = pygame.display.set_mode(tam)
    
    # Se crea el control
    control = Control()

    pygame.display.set_caption("Ejemplo de juego de plataforma")            

    # Se carga musica de fondo
    pygame.mixer.music.load("Sonidos/fondo.mp3")
    
    # Controlamos que tan rapido actualizamos pantalla
    reloj = pygame.time.Clock()

    finalizar = False
    llamado = 1
    while not finalizar:
        if llamado == 1:
            continuar = False
            estado = 0
            while not continuar:
                if estado == 0:
                    estado = Menu(pantalla)
                if estado == 2:
                    estado = MostrarTutorial(pantalla)
                if estado == 3:
                    estado = control.menuControl(pantalla)
                if estado == 1:
                    continuar = True
                    llamado = 2
                if estado == -1:
                    continuar = True
                    finalizar = True

        if llamado == 2:
            jugador = Jugador()
            # Creamos los niveles y la vida del jugador
            nivel_lista = []
            vida = Vida()            
            # Establecemos nivel actual
            nivel_actual_no = 0            
            # Lista de sprites activos
            activos_sp_lista = pygame.sprite.Group()
            # Indicamos a la clase jugador cual es el nivel    
            nivel_lista.append( Nivel_01(jugador,vida) )
            nivel_actual = nivel_lista[nivel_actual_no]
            jugador.nivel = nivel_actual
            jugador.rect.x = 320
            jugador.rect.y = ALTO - jugador.rect.height
            activos_sp_lista.add(jugador)
            activos_sp_lista.add(vida)
            pygame.mixer.music.play(1)
            fin = False
            pausar = False

            while not fin and estado == 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        fin = True
                        finalizar = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == control.izq:
                            jugador.ir_izq()
                            jugador.izquierda = True
                        if event.key == control.der:
                            jugador.ir_der()
                            jugador.derecha = True
                        if event.key == control.arriba:
                            #print "salto"
                            jugador.salto()
                        if event.key == control.bahamut:
                            jugador.cambiarPersonaje(1)
                        if event.key == control.leviathan:
                            jugador.cambiarPersonaje(2)
                        if event.key == control.phoenix:
                            jugador.cambiarPersonaje(3)
                        if event.key == control.oso:
                            jugador.cambiarPersonaje(4)
                        if event.key == control.buey:
                            jugador.cambiarPersonaje(5)
                        if event.key == pygame.K_p:
                            pausar = True
                    else:
                        jugador.derecha = False
                        jugador.izquierda = False
                
                    if event.type == pygame.KEYUP:
                        if event.key == control.izq and jugador.vel_x < 0:
                            jugador.no_mover()
                        if event.key == control.der and jugador.vel_x > 0:
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

                if pausar:
                    llamado,pausar = pausarJuego(pantalla)

                if llamado == 1 or llamado == -1:
                    fin = True
                    activos_sp_lista.empty()

                nivel_actual.draw(pantalla)
                activos_sp_lista.draw(pantalla)
                reloj.tick(60)
                pygame.display.flip()

        if llamado == -1:
            finalizar = True
