import pygame
import constantes
import personaje
from weapon import Weapon

#Correr en la consola: venv/Scripts/activate

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
pygame.display.set_caption("Primer juego con Pygame")

def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale,h*scale))
    return nueva_imagen


#Importar imagenes

animaciones = []
for i in range(7):
    img = pygame.image.load(f"assets\images\characters\players\Player_{i}.png").convert_alpha() #conver_alpha optimiza las imagenes para una mejor velocidad de carga, manteniendo la transparencia
    img = escalar_img(img,constantes.ESCALA_PERSONAJE )
    animaciones.append(img)

#Imagenes
imagen_pistola = pygame.image.load(f"assets\images\weapons\Glock18.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola,constantes.ESCALA_PISTOLA)

imagen_bala = pygame.image.load(f"assets\images\weapons\Bulletuzi.png").convert_alpha()
imagen_bala = escalar_img(imagen_bala,constantes.ESCALA_BALA)

#Crear un jugador de la clase personaje
jugador = personaje.Personaje(50,50,animaciones)

#Crear un arma de la clase Weapon
pistola = Weapon(imagen_pistola,imagen_bala)

#Crear un grupo de sprites
grupo_balas = pygame.sprite.Group() #Porque pueden haber varias balas en la pantalla


#Definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

run = True

while run:
    ventana.fill(constantes.COLOR_BG)

    #Que vaya a 60 FPS
    reloj.tick(constantes.FPS)

    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = 5 #pixeles
    if mover_izquierda == True:
        delta_x = -5
    if mover_arriba:
        delta_y = -5
    if mover_abajo:
        delta_y = 5
    
    

    #Mover al jugador
    jugador.movimiento(delta_x, delta_y)

    #Actualizar el estado del jugador
    jugador.update()

    #Actualizar el estado del arma
    bala = pistola.update(jugador)
    if bala:   
        grupo_balas.add(bala)

    #print(grupo_balas)
    for bala in grupo_balas:
        bala.update()


    #Dibujar al jugador
    jugador.dibujar(ventana)

    #Dibujar el arma
    pistola.dibujar(ventana)

    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update() #Asegura que se mantenga el programe en ejecución

pygame.quit()