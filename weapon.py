import pygame
import math

class Weapon():
    def __init__(self,image):
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
    
    def update(self, personaje):
        self.forma.center = personaje.forma.center #personaje es de la clase Personaje
        if not(personaje.flip):
            self.forma.x += personaje.forma.width/2
            self.rotar(False)
        else:
            self.forma.x -= personaje.forma.width/2
            self.rotar(True)
    
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)
        distancia_x = mouse_pos[0] - self.forma.x
        distancia_y = - (mouse_pos[1] - self.forma.y)
        angulo = math.degrees(math.atan2(distancia_y,distancia_x))
        if -15<angulo<15:
            self.angulo = angulo
        #print(self.angulo)

    def dibujar(self,interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen,self.forma)

    def rotar(self, rotar):
        if rotar:
            imagen_flip = pygame.transform.flip(self.imagen_original,True,False)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,False,False)
        self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

