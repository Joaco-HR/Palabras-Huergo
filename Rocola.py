import cv2
import pygame
import sys
from moviepy.editor import VideoFileClip

# Inicializar Pygame y sus módulos  
pygame.init()
pygame.mixer.init()

# Definir colores
Gris = (88, 88, 88)
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Verde = (0, 255, 0)
Rojo = (255, 0, 0)

# Configurar la pantalla
Pantalla = pygame.display.set_mode((900, 508))
pygame.display.set_caption("Palabras Huergo")

# Cargar fondos
Fondo_Menu = pygame.image.load('Fondos/Fondo.jpg')
Fondo_Mini_Juego_3 = pygame.image.load('Fondos/Fondo MiniJuegos 3.png')
Fondo_inicio = Fondo_Menu

# Cargar botones
Boton_diseño = pygame.image.load('Botones/Boton.png')
Boton_Oscuro = pygame.image.load('Botones/Boton Oscuro.png')
Boton_return = pygame.image.load('Botones/Boton de Return.png')
Boton_ret_o = pygame.image.load('Botones/Boton de Return Oscuro.png')

# Configurar botones y sus rectángulos
Boton_inicio = Boton_diseño
Rectangulo = Boton_diseño.get_rect(topleft=(325, 250))
Boton_Play_Pausa = pygame.Rect(320, 410, 100, 50)
Boton_Restart = pygame.Rect(495, 410, 100, 50)

# Definir fuentes
Fuente_Botones = pygame.font.Font("Tipografias/ShowcardGothic.ttf", 30)
Fuente_pregunta = pygame.font.Font('Tipografias/cooper-black.ttf', 30)
Fuente_opcion = pygame.font.Font('Tipografias/cooper-black.ttf', 24)
Fuente_opcion_3 = pygame.font.Font('Tipografias/cooper-black.ttf', 28)
Fuente_texto = pygame.font.Font('Tipografias/ShowcardGothic.ttf', 25)

# Información de preguntas
informacion = [
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Mente en Blanco', 'Caos', 'Extra', 'Sour Candy'],
     "Correcta": 0,
     "Posicion_Pre": (141, 55),
     "Audio": "Canciones/Mente en Blanco.mp3",
     "Posicion": [(18, 210), (755, 210), (75, 402), (705, 402)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Judas', 'Poker Face', 'Bad Romance', 'Blody Marry'],
     "Correcta": 1,
     "Posicion_Pre": (141, 55),
     "Audio": "Canciones/Poker Face.mp3",
     "Posicion": [(72, 210), (712, 210), (22, 402), (700, 402)]
    },  
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Deja Vu', 'Loba', 'Acrosito', 'Objection'],
     "Correcta": 2,
     "Posicion_Pre": (141, 55),
     "Audio": "Canciones/Mente en Blanco.mp3",
     "Posicion": [(60, 210), (748, 210), (58, 402), (715, 402)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Man', 'Shake it Up', 'Bad Blood', 'Cruel Summer'],
     "Correcta": 3,
     "Posicion_Pre": (141, 55),
     "Audio": "Canciones/Acróstico.mp3",
     "Posicion": [(83, 210), (705, 210), (45, 402), (700, 406)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Dance the Night', 'Leviatating', 'Houdini', 'Sweet Pie'],
     "Correcta": 0,
     "Posicion_Pre": (141, 55),
     "Audio": "Canciones/Dance the Night.mp3",
     "Posicion": [(18, 210), (707, 210), (58, 402), (720, 402)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Taste', 'Please', 'Espresso', 'Feathers'],
     "Correcta": 0,
     "Posicion_Pre": (141, 55),
     "Audio": "Canciones/Taste.mp3",
     "Posicion": [(80, 210), (743, 210), (58, 402), (725, 402)]
    }
]

# Variables globales
Pregunta_actual = 0
Opcion_sel = 0
Tiempo = 0
respuesta_correcta = None
Jugando = False
Pausado = False
Video = None
Ruta_Video = None
Audio = None

# Función para cargar audio y video
def cargar_audio_y_video(Pregunta_actual):
    global Video, Ruta_Video, Audio
    if Fondo_inicio == Fondo_Mini_Juego_3:
        if Pregunta_actual == 0:
            Audio = "Canciones/Mente en Blanco.mp3"
            Ruta_Video = "Canciones/Ondas.mp4"
        elif Pregunta_actual == 1:
            Audio = "Canciones/Poker Face.mp3"
            Ruta_Video = "Canciones/Ondas.mp4"
        elif Pregunta_actual == 2:
            Audio = "Canciones/Acróstico.mp3"
            Ruta_Video = "Canciones/Ondas.mp4"
        elif Pregunta_actual == 3:
            Audio = "Canciones/Cruel Summer.mp3"
            Ruta_Video = "Canciones/Ondas.mp4"
        elif Pregunta_actual == 4:
            Audio = "Canciones/Dance the Night.mp3"
            Ruta_Video = "Canciones/Ondas.mp4"
        elif Pregunta_actual == 5:
            Audio = "Canciones/Taste.mp3"
            Ruta_Video = "Canciones/Ondas.mp4"
        else:
            Audio = "Canciones/Fondo.mp3"
            Ruta_Video = None
        Video = cv2.VideoCapture(Ruta_Video)
    else:
        Audio = "Canciones/Sin Sonido.mp3"

# Función para reproducir la música
def reproducir_musica():
    pygame.mixer.music.load(Audio)
    pygame.mixer.music.play(-1)

# Función para detener la música
def detener_musica():
    pygame.mixer.music.stop()

# Función para dibujar botones
def Botones(surface, Texto, rect):
    mouse_pos = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Gris, rect)
        texto_color = Negro
    else:
        pygame.draw.rect(surface, Gris, rect)
        texto_color = Blanco

    texto = Fuente_Botones.render(Texto, True, texto_color)
    surface.blit(texto, (rect.x + (rect.width - texto.get_width()) // 2, 
                          rect.y + (rect.height - texto.get_height()) // 2))

# Función para dibujar el mini juego
def Mini_Juego(informacion_pregunta, tiempo):
    Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
    Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
    for i, option in enumerate(informacion_pregunta["Opcion"]):
        x, y = informacion_pregunta["Posicion"][i]
        Usar = Fuente_opcion if i == 0 else Fuente_opcion_3
        Usar_3 = Fuente_opcion if i == 3 else Fuente_opcion_3
        if Pregunta_actual == 0 or Pregunta_actual == 4:
            if respuesta_correcta is not None:
                if i == informacion_pregunta["Correcta"]:
                    text = Usar.render(option, True, Verde)
                elif i == Opcion_sel and not respuesta_correcta:
                    text = Usar.render(option, True, Rojo)
                else:                        
                    text = Usar.render(option, True, Blanco)
            else:
                if i == Opcion_sel:
                    text = Usar.render(option, True, Negro)
                else:
                    text = Usar.render(option, True, Blanco)
            Pantalla.blit(text, (x, y))
        elif Pregunta_actual == 3:
            if respuesta_correcta is not None:
                if i == informacion_pregunta["Correcta"]:
                    text = Usar_3.render(option, True, Verde)
                elif i == Opcion_sel and not respuesta_correcta:
                    text = Usar_3.render(option, True, Rojo)
                else:
                    text = Usar_3.render(option, True, Blanco)
            else:
                if i == Opcion_sel:
                    text = Usar_3.render(option, True, Negro)
                else:
                    text = Usar_3.render(option, True, Blanco)
            Pantalla.blit(text, (x, y))
        else:                
            if respuesta_correcta is not None:
                if i == informacion_pregunta["Correcta"]:
                    text = Fuente_opcion_3.render(option, True, Verde)
                elif i == Opcion_sel and not respuesta_correcta:
                    text = Fuente_opcion_3.render(option, True, Rojo)
                else:
                    text = Fuente_opcion_3.render(option, True, Blanco)
            else:
                if i == Opcion_sel:
                    text = Fuente_opcion_3.render(option, True, Negro)
                else:
                    text = Fuente_opcion_3.render(option, True, Blanco)
            Pantalla.blit(text, (x, y))
        Texto = Fuente_texto.render(str(int(tiempo)), True, Blanco)
        Pantalla.blit(Texto, (815, 47))


# Función para dibujar el botón de inicio
def Boton_i(surface):
    surface.blit(Boton_inicio, Rectangulo.topleft)
    Posi_mouse = pygame.mouse.get_pos()
    if Fondo_inicio == Fondo_Menu:
        if Rectangulo.collidepoint(Posi_mouse):
            surface.blit(Boton_Oscuro, Rectangulo.topleft)
        else:
            surface.blit(Boton_diseño, Rectangulo.topleft)
    elif Fondo_inicio == Fondo_Mini_Juego_3:
        if Rectangulo.collidepoint(Posi_mouse):
            surface.blit(Boton_ret_o, Rectangulo.topleft)
        else:
            surface.blit(Boton_return, Rectangulo.topleft)
    pygame.display.flip()

# Función principal del juego
def main():
    global Video, Jugando, Pausado, Pregunta_actual, Opcion_sel, Tiempo, respuesta_correcta, Fondo_inicio, Boton_inicio, Rectangulo
    Reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Boton_Play_Pausa.collidepoint(mouse_pos):
                    if Jugando:
                        if Pausado:
                            pygame.mixer.music.unpause()
                            Pausado = False
                        else:
                            pygame.mixer.music.pause()
                            Pausado = True
                elif Boton_Restart.collidepoint(mouse_pos):
                    if Jugando:
                        Video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        pygame.mixer.music.rewind()
                        reproducir_musica()
                        Pausado = False
                elif Rectangulo.collidepoint(mouse_pos):
                    if Fondo_inicio == Fondo_Menu:
                        Fondo_inicio = Fondo_Mini_Juego_3
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        if not Jugando:
                            cargar_audio_y_video(Pregunta_actual)
                            reproducir_musica()
                            Jugando = True
                            Pausado = False
                    else:
                        Fondo_inicio = Fondo_Menu
                        Boton_inicio = Boton_diseño
                        Rectangulo = Boton_diseño.get_rect(topleft=(325, 250))
                        if Video:
                            Video.release()
                            Video = None
                        detener_musica()
                        Jugando = False
                        Pausado = False
                        Tiempo = 0
                        Pregunta_actual = 0
                        Opcion_sel = 0
                if event.key == pygame.K_LEFT:
                    Opcion_sel = (Opcion_sel - 1) % len(informacion[Pregunta_actual]["Opcion"])
                    respuesta_correcta = None 
                elif event.key == pygame.K_RIGHT:
                    Opcion_sel = (Opcion_sel + 1) % len(informacion[Pregunta_actual]["Opcion"])
                    respuesta_correcta = None 
                elif event.key == pygame.K_UP:
                    Opcion_sel = (Opcion_sel + 2) % len(informacion[Pregunta_actual]["Opcion"])
                    respuesta_correcta = None
                elif event.key == pygame.K_DOWN:
                    Opcion_sel = (Opcion_sel - 2) % len(informacion[Pregunta_actual]["Opcion"])
                    respuesta_correcta = None  
                elif event.key == pygame.K_RETURN:
                    if Opcion_sel == informacion[Pregunta_actual]["Correcta"]:
                        Tiempo += 10
                        respuesta_correcta = True
                    else:
                        respuesta_correcta = False
                    if Fondo_inicio == Fondo_Mini_Juego_3:
                        Pantalla.blit(Fondo_Mini_Juego_3, (0, 0))
                        Botones(Pantalla, 'Play' if not Jugando else 'Pause' if not Pausado else 'Resume', Boton_Play_Pausa)
                        Botones(Pantalla, 'Restart', Boton_Restart)
                        Mini_Juego(informacion[Pregunta_actual], Tiempo)
                        pygame.display.flip()
                        pygame.time.delay(500)
                        Pregunta_actual += 1
                        Opcion_sel = 0
                        respuesta_correcta = None
                        if Pregunta_actual >= len(informacion):
                            Pregunta_actual = 0
                            Opcion_sel = 0
                            Tiempo = 0
                            Fondo_inicio = Fondo_Menu
                            Boton_inicio = Boton_diseño
                            Rectangulo = Boton_diseño.get_rect(topleft=(325, 250))
                            if Video:
                                Video.release()
                                Video = None
                            detener_musica()
                            Jugando = False
                            Pausado = False
                        pygame.time.delay(500)
                        cargar_audio_y_video(Pregunta_actual)
                        reproducir_musica()

        Pantalla.blit(Fondo_inicio, (0, 0))
        if Fondo_inicio == Fondo_Mini_Juego_3:
            if Jugando and not Pausado:
                ret, frame = Video.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.transpose(frame)
                    frame = cv2.flip(frame, flipCode=1)
                    frame_surface = pygame.surfarray.make_surface(frame)
                    frame_surface = pygame.transform.scale(frame_surface, (413, 217))
                    Pantalla.blit(frame_surface, (245, 153))
                else:
                    Video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    Jugando = False
                    detener_musica()
            Botones(Pantalla, 'Play' if not Jugando else 'Pause' if not Pausado else 'Resume', Boton_Play_Pausa)
            Botones(Pantalla, 'Restart', Boton_Restart)
            pygame.draw.rect(Pantalla, Negro, (558, 321, 100, 50))
            Mini_Juego(informacion[Pregunta_actual], Tiempo)
        Boton_i(Pantalla)
        pygame.display.flip()
        Reloj.tick(30)

# Ejecutar el juego
main()