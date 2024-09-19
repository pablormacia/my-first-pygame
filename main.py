import pygame
import constantes
import personaje
from weapon import Weapon
import os #Para pode trabajar con archivos y carpetas

#Correr en la consola: venv/Scripts/activate

#Funciones:
#Escalar:
def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale,h*scale))
    return nueva_imagen

#Contar cantidad de elementos de una carpeta:
def contar_elementos(directorio):
    return len(os.listdir(directorio))

#Listar los nombres de los archivos de una carpeta:
def nombre_carpetas(directorio):
    return os.listdir(directorio)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
pygame.display.set_caption("Primer juego con Pygame")


#Importar imagenes
animaciones = []
for i in range(7):
    img = pygame.image.load(f"assets\images\characters\players\Player_{i}.png").convert_alpha() #conver_alpha optimiza las imagenes para una mejor velocidad de carga, manteniendo la transparencia
    img = escalar_img(img,constantes.ESCALA_PERSONAJE )
    animaciones.append(img)

#enemigos
directorio_enemigos = 'assets\images\characters\enemies'
tipo_enemigos = nombre_carpetas(directorio_enemigos)
animaciones_enemigos = []

for enemigo in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"assets\images\characters\enemies\{enemigo}"
    num_animaciones = contar_elementos(ruta_temp)
    #print(num_animaciones)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}\{enemigo}-{i+1}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo,constantes.ESCALA_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)

#print(animaciones_enemigos)

#Imagenes
imagen_pistola = pygame.image.load(f"assets\images\weapons\Glock18.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola,constantes.ESCALA_PISTOLA)

imagen_bala = pygame.image.load(f"assets\images\weapons\Bulletuzi.png").convert_alpha()
imagen_bala = escalar_img(imagen_bala,constantes.ESCALA_BALA)

#Crear un jugador de la clase personaje
jugador = personaje.Personaje(50,50,animaciones)

#Crear un enemigo de la clase personaje
goblin = personaje.Personaje(400,300,animaciones_enemigos[0])
mushroom = personaje.Personaje(200,300,animaciones_enemigos[1])
goblin_2 = personaje.Personaje(100,200,animaciones_enemigos[0])

#Crear lista de enemigos
lista_enemigos = []
lista_enemigos.append(goblin)
lista_enemigos.append(goblin_2)
lista_enemigos.append(mushroom)

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

    #Actualizar el estado del enemigo
    for enemigo in lista_enemigos:
        enemigo.update()

    #Actualizar el estado del arma
    bala = pistola.update(jugador)
    if bala:   
        grupo_balas.add(bala)

    #print(grupo_balas)
    for bala in grupo_balas:
        bala.update()


    #Dibujar al jugador
    jugador.dibujar(ventana)

    #Dibujar al enemigo
    for enemigo in lista_enemigos:
        enemigo.dibujar(ventana)

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