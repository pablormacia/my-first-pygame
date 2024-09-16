import pygame
import math
import constantes

class Weapon():
    def __init__(self, image,imagen_bala):
        self.imagen_bala = imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(
            self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.disparada = False
        self.ultimo_disparo = pygame.time.get_ticks() #Tomo el tiempo del último disparo

    def update(self, personaje):
        disparo_cooldown = constantes.COOLDOWN_BALAS #Tiempo de espera para poder disparar la siguiente bala
        bala = None
        self.forma.center = personaje.forma.center  # personaje es de la clase Personaje
        if not (personaje.flip):
            self.forma.x += personaje.forma.width/2
            self.rotar(False)
        else:
            self.forma.x -= personaje.forma.width/2
            self.rotar(True)

        mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)
        distancia_x = mouse_pos[0] - self.forma.x
        distancia_y = - (mouse_pos[1] - self.forma.y)
        angulo = math.degrees(math.atan2(distancia_y, distancia_x))
        if -15 < angulo < 15 or -165<angulo<165:
            self.angulo = angulo
        """ print(self.angulo) 
        self.angulo = angulo """

        #Detectar clic del mouse
        if pygame.mouse.get_pressed()[0] and self.disparada==False and pygame.time.get_ticks() - self.ultimo_disparo >= disparo_cooldown: #clic izq
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.disparada = True
            self.ultimo_disparo = pygame.time.get_ticks()
            #Resetear el click del mouse
        if pygame.mouse.get_pressed()[0]==False:
            self.disparada = False
        return bala

    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)

    def rotar(self, rotar):
        if rotar:
            imagen_flip = pygame.transform.flip(
                self.imagen_original, True, False)
        else:
            imagen_flip = pygame.transform.flip(
                self.imagen_original, False, False)
        self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


class Bullet(pygame.sprite.Sprite):  # Hereda de la clase pygame.sprite.Sprite
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self) #Nos permite utilizar los métodos y atributos de la clase
        self.imagen_original = image
        self.angulo = angle
        #Usamos los nombres en inglés tal cual la libreria:
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #Calculo de velocidad
        self.delta_x = math.cos(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
        self.delta_y = -math.sin(math.radians(self.angulo))*constantes.VELOCIDAD_BALA

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        #Veo si las balas salieron de la pantalla para eliminarlas de la memoria:
        if self.rect.right <0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.bottom<0 or self.rect.top>constantes.ALTO_VENTANA:
            self.kill()

    def dibujar(self,interfaz):
        interfaz.blit(self.image, (self.rect.centerx,self.rect.centery - int(self.image.get_height())))