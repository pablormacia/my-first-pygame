import pygame
import constantes

class Personaje():
    def __init__(self, x, y,animaciones):
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks() #Guarda el tiempo transcurrido en milisegundos
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()
        self.forma.center = (x,y) # Lo movemos a la coordenada x,y que le pasamos
        
    def update(self):
        cooldown_animacion = 100 #cuanto tiempo quiero que se mantenga una imagen en ms
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks()-self.update_time >= cooldown_animacion: #Al inicio del juego son iguales, pero luego cambia
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index=0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma) #Debo indicar que quiero dibujar y donde (forma)

    def movimiento(self, delta_x, delta_y):
        if delta_x<0:
            self.flip = True
        if delta_x>0:
            self.flip = False
        self.forma.x += delta_x
        self.forma.y += delta_y
