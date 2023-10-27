from modulo_logica import *
from modulo_pygame import *
from data.modulo_carga import *
from excepciones.excepciones import  *
import pygame

pygame.init()
configurar_ventana_pygame() #Inicializa la biblioteca Pygame y configura la ventana del juego.

diccionario_de_temas = carga_json() #Carga datos del juego desde un archivo JSON.

jugando = True           #Establece las banderas  para controlar el flujo del juego.
pantalla_inicio = True
pantalla_perdida = False 
while pantalla_inicio:    #Entra en un bucle que representa la pantalla de inicio del juego.
    cargar_inicio_pygame()   # Llama a cargar_inicio_pygame() para cargar la pantalla de inicio del juego.
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:          #Itera a través de los eventos en lista_eventos 
        if evento.type == pygame.QUIT:    #y evalua los que van sucediendo
            pantalla_inicio = False
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            try:     
                pantalla_inicio = not validador_start(pygame.key.name(evento.key))      
            except NoPresionaEnterException as error:
                print(error.message)
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if evento.pos[0] > 265 and evento.pos[0] < 436:
                    if evento.pos[1] > 146 and evento.pos[1] < 214:
                        pantalla_inicio = False
                     
    pygame.display.update()   #Actualiza la pantalla de inicio del juego utilizando pygame.display.update().
         
clock = pygame.time.Clock()        #Se crea un objeto Clock de Pygame para controlar la velocidad del juego.
tiempo_inicial = pygame.time.get_ticks()

palabra_adivinada = True
puntaje = 0
tiempo_sumar_puntaje = 0
vidas = 6
lista_letras = []
se_presiono_letra = False
while jugando:                              #Ciclo Principal
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:            #Itera a través de los eventos en lista_eventos 
        if evento.type == pygame.QUIT:      #y evalua los que van sucediendo
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            nombre_de_letra = pygame.key.name(evento.key)           
            try:     
                se_presiono_letra = validar_letras(lista_letras,nombre_de_letra)
                if se_presiono_letra:
                    lista_letras.append(nombre_de_letra.upper())
            except NoEsLetraException as error:                  #Se lanzan excepciones en caso que sucedan
                print(error.message)
            except EstaRepetidoException as error:
                print(error.message)
                
    
    if palabra_adivinada:                #setup juego
        refrescar_fondo_pygame() 
        tema = obtener_tema(diccionario_de_temas)
        palabra = obtener_palabra(diccionario_de_temas,tema)
        palabra_oculta = reemplazar_letras(palabra,lista_letras)
        pygame.time.set_timer(pygame.QUIT,60000) 
        refrescar_datos_pygame(puntaje, vidas, tema, palabra_oculta, tiempo_inicial)
        palabra_adivinada = False
        
    
    if se_presiono_letra :                  #Se chequea  si la palabra o parte de ella fue descubierta o no
        if palabra != palabra_oculta:       #Se modifican datos en base a eso
            previa_palabra_oculta = palabra_oculta
            palabra_oculta = reemplazar_letras(palabra,lista_letras)
            
            if palabra_oculta == previa_palabra_oculta:
                vidas -= 1
                puntaje -= 5 
                           
            elif palabra == palabra_oculta:
                palabra_adivinada = True
                tiempo_inicial = pygame.time.get_ticks()
                puntaje += 100
                puntaje += (60 - tiempo_sumar_puntaje) * 10
                lista_letras = []
            else:
                puntaje += 10

            if vidas == 0: 
                pantalla_perdida = True
                jugando = False
            
        se_presiono_letra = False   
        
    refrescar_fondo_pygame()
    tiempo_sumar_puntaje = refrescar_datos_pygame(puntaje, vidas, tema, palabra_oculta, tiempo_inicial)
                                                  #refresca fondo y envia informacion para contador.
      
    pygame.display.update()

while pantalla_perdida:                        #3er ciclo de cierre.
    cargar_final_pygame()
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pantalla_perdida = False
            
    pygame.display.update()

pygame.quit()