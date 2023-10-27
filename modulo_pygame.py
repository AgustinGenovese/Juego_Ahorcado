import pygame
from data.modulo_carga import *

BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
VENTANA = pygame.display.set_mode((700,600))

def configurar_ventana_pygame():
    """
    Esta función configura la ventana de la aplicación de Pygame, estableciendo el título de la ventana y el ícono.
    - Configura el título de la ventana de la aplicación de Pygame como "Pygame".
    - Establece el ícono de la ventana a partir de un archivo de imagen llamado "Icono.ico".
    """
    pygame.display.set_caption("Pygame")
    icono = pygame.image.load("imagenes\Icono.ico")
    pygame.display.set_icon(icono)

def cargar_reglas(archivo):
    x = 50
    y = 370
    for linea in archivo:
        linea = linea.strip()
        fuente = pygame.font.SysFont("rockwell", 14)
        reglas = fuente.render(linea, True, BLANCO)
        VENTANA.blit(reglas, (x, y))
        y += 25 
 
def cargar_inicio_pygame():
    """
    Esta función se encarga de cargar y mostrar la pantalla de inicio del juego.
    - Carga la imagen de fondo 'imagen_menu.jpg', la ajusta al tamaño de 700x600 píxeles y la muestra en la ventana.
    - Muestra el título "PLAY" en la ventana.
    - Dibuja un rectángulo en la ventana alrededor del título.
    - Lee las reglas del juego desde el archivo 'reglas.csv' y las muestra en la ventana.
    """
    
    imagen_menu = pygame.image.load("imagenes\imagen_menu.jpg")
    imagen_menu = pygame.transform.scale(imagen_menu, (700, 600))
    VENTANA.blit(imagen_menu,(0, 0))

    fuente = pygame.font.SysFont("jokerman",40)
    titulo = fuente.render("PLAY",False,BLANCO)
    VENTANA.blit(titulo,(290,150)) 
    pygame.draw.rect(VENTANA, NEGRO, (250, 130, 200, 100), 15)
    
    obtener_reglas(cargar_reglas) 
    #Si cargar reglas se escribe con parentesis se estaria ejecuando primero esa funcion,
    #en cambio, de esta manera se la envia como parametro para q la utilice obtener regla
    # obtener_regla abre el archivo csv cada vez que se llama la funcion y cargar regla, dentro de esa funcion
    #imprime en la venana pygame la informacion de ese archivo csv       

def refrescar_fondo_pygame():
    """
    Esta función actualiza y refresca el fondo de la ventana de la aplicación Pygame.
    - Carga una imagen de fondo desde un archivo llamado "imagen_fondo.jpg" y la escala a las dimensiones 700x600.
    - Muestra la imagen de fondo en la ventana.
    - Crea un título "Ahorcado" con un tipo de letra específico y lo muestra en la ventana.
    """
    imagen_fondo = pygame.image.load("imagenes\imagen_fondo.jpg")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (700, 600))
    VENTANA.blit(imagen_fondo,(0, 0))

    fuente_titulo = pygame.font.SysFont("jokerman",45)
    titulo = fuente_titulo.render("Ahorcado",False,BLANCO)
    VENTANA.blit(titulo,(350,50))
    
def refrescar_datos_pygame(puntaje:int, vidas:int, tema:str, palabra_oculta:str, tiempo_inicial:int):
    """
    Esta función actualiza y muestra datos  en la ventana de la aplicación Pygame.
    - Muestra el puntaje del jugador en la esquina superior derecha de la ventana.
    - Muestra el número de vidas restantes en la esquina superior izquierda de la ventana.
    - Muestra la categoría o tema actual en la parte superior central de la ventana.
    - Muestra la palabra oculta que el jugador debe adivinar en el centro de la ventana.
    - LLama a otra funcon qued ibuja una representación gráfica de las vidas restantes del jugador.
    
    Parámetros:
    - puntaje (int): El puntaje actual del jugador.
    - vidas (int): El número de vidas restantes del jugador.
    - tema (str): La categoría o tema actual del juego.
    - palabra_oculta (str): La palabra oculta que el jugador debe adivinar.
    - tiempo_inicial (int): El tiempo inicial del juego, en milisegundos.
    
    Return:
    - Devuelve el valor de retorno de la función mostrar_reloj_pygame, que muestra el tiempo transcurrido en el juego.
    """
   
    mensaje = (f"Puntaje: {puntaje}")
    mostrar_texto_pygame(mensaje,550,540)
    mensaje = (f"Vidas: {vidas}")
    mostrar_texto_pygame(mensaje,100,55)  
    mensaje = (f"Categoria: {tema}")
    mostrar_texto_pygame(mensaje, 300,540) 
    mostrar_texto_pygame(palabra_oculta,300,400, 45)
    dibujar_persona_pygame(vidas)
    return mostrar_reloj_pygame(tiempo_inicial)

def mostrar_reloj_pygame(tiempo_inicial):
    """
    Esta función muestra un contador de tiempo en la ventana de la aplicación Pygame.
    - Obtiene el tiempo actual en milisegundos
    - Calcula el tiempo transcurrido en segundos desde el tiempo inicial.
    - Muestra el tiempo transcurrido en la ventana.

    Parámetros:
    - tiempo_inicial (int): El tiempo inicial en segundos desde el que se va a contar.

    Return:
    - int: El tiempo transcurrido en segundos desde el tiempo inicial.
    """
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = int((tiempo_actual - tiempo_inicial) * 0.001)
    tiempo_transcurrido_string = (f"Contador: {tiempo_transcurrido}")   
    mostrar_texto_pygame(tiempo_transcurrido_string, 100, 30) 
    return tiempo_transcurrido  

def mostrar_texto_pygame(palabra:str,x:int,y:int, fuente = 20):
    """
    Esta función muestra texto en la ventana de la aplicación Pygame.
    - Crea una fuente con el tipo de letra "Arial" y el tamaño especificado (o predeterminado a 20).
    - Renderiza el texto usando la fuente y el color blanco.
    - Muestra el texto en la ventana en las coordenadas especificadas.
    
    Parámetros:
    - palabra (str): El texto que se va a mostrar en la ventana.
    - x (int): La coordenada X en la que se va a mostrar el texto en la ventana.
    - y (int): La coordenada Y en la que se va a mostrar el texto en la ventana.
    - fuente (int, opcional): El tamaño de fuente para el texto (predeterminado a 20).
    """
    fuente = pygame.font.SysFont("Arial",fuente)
    texto = fuente.render(palabra,True,BLANCO)
    VENTANA.blit(texto,(x,y))
    
def dibujar_persona_pygame(vida):
    """
     Esta función dibuja la representación gráfica de la persona en el juego.
    Parámetros:
    - vida (int): El número de vidas restantes, que determina el nivel de la representación gráfica.
    """
    match vida:
        case 5:
            pygame.draw.circle(VENTANA, BLANCO, (235, 197), 30, 4)
        case 4:
            pygame.draw.circle(VENTANA, BLANCO, (235, 197), 30, 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 227), (235, 350), 4)
        case 3:
            pygame.draw.circle(VENTANA, BLANCO, (235, 197), 30, 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 227), (235, 350), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (183, 260), 4)
        case 2:
            pygame.draw.circle(VENTANA, BLANCO, (235, 197), 30, 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 227), (235, 350), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (183, 260), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (287, 260), 4)
        case 1:
            pygame.draw.circle(VENTANA, BLANCO, (235, 197), 30, 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 227), (235, 350), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (183, 260), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (287, 260), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 350), (270, 400), 4)
        case 0:
            pygame.draw.circle(VENTANA, BLANCO, (235, 197), 30, 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 227), (235, 350), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (183, 260), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 240), (287, 260), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 350), (270, 400), 4)
            pygame.draw.line(VENTANA, BLANCO, (235, 350), (200, 400), 4)
            

def cargar_final_pygame():
    """
     Esta función carga una pantalla de final de juego en la ventana de la aplicación Pygame.
    - Llena la ventana con un color negro (NEGRO) para crear una pantalla de final de juego.
    - Muestra un mensaje de despedida "GAME OVER" en el centro de la pantalla.
    """
    VENTANA.fill(NEGRO)
    fuente = pygame.font.SysFont("jokerman",40)
    despedida = fuente.render("GAME OVER",False,BLANCO)
    VENTANA.blit(despedida,(230,250)) 