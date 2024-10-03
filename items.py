import pygame.sprite

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type,animacion_list):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type # 0 monedas 1 pociones
        self.animacion_list = animacion_list
        self.frame_index = 0 # Se para en la primera imagen, en 1 en la segunda, etc...
        self.update_time = pygame.time.get_ticks() #Guarda el tiempo actual cuando se ejecuta
        self.image = self.animacion_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self,personaje):
        #comprobar la colisión entre el personaje y el item
        if self.rect.colliderect(personaje.forma):
            #monedas
            if self.item_type==0:
                personaje.score+=1
            #posiones
            elif self.item_type==1:
                personaje.energia += 50
                if personaje.energia > 100:
                    personaje.energia = 100
            self.kill() #método de sprite
        cooldown_animacion = 100 #milisegundos
        self.image = self.animacion_list[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        
        if self.frame_index >= len(self.animacion_list):
            self.frame_index = 0