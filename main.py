import pygame
import constantes
import personaje

#Correr en la consola: venv/Scripts/activate

pygame.init()





ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

pygame.display.set_caption("Primer juego con Pygame")


def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale,h*scale))
    return nueva_imagen

animaciones = []
for i in range(7):
    img = pygame.image.load(f"assets\images\characters\players\Player_{i}.png")
    img = escalar_img(img,constantes.ESCALA_PERSONAJE )
    animaciones.append(img)

#jugador = personaje.Personaje(50,50,player_image)
jugador = personaje.Personaje(50,50,animaciones)

#player_image = pygame.image.load("assets\images\characters\players\Player_0.png")
#player_image = pygame.transform.scale(player_image, (player_image.get_width()*constantes.ESCALA_PERSONAJE,player_image.get_height()*constantes.ESCALA_PERSONAJE))
#player_image = escalar_img(player_image, constantes.ESCALA_PERSONAJE)

#Definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

run = True

while run:

    #Relleno con el color de fondo

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

    #print(f"{delta_x}, {delta_y}")
    #Mover al jugador
    jugador.movimiento(delta_x, delta_y)

    jugador.update()

    jugador.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                #print("Izquierda")
                mover_izquierda = True
            if event.key == pygame.K_d:
                #print("Derecha")
                mover_derecha = True
            if event.key == pygame.K_w:
                #print("Arriba")
                mover_arriba = True
            if event.key == pygame.K_s:
                #print("Abajo")
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