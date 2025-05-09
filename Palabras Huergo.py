import cv2
import pygame
import sys
from moviepy.editor import VideoFileClip

# Inicializar Pygame y sus módulos  
pygame.init()
pygame.mixer.init()

# Definir colores
Gris = (115, 115, 115)
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Verde = (0, 255, 0)
Rojo = (255, 0, 0)

# Configurar la pantalla
Pantalla = pygame.display.set_mode((898, 506))
pygame.display.set_caption("Palabras Huergo")

# Cargar fondos
Fondo_Menu = pygame.image.load('Fondos/Fondo.png')
Fondo_Tutorial = pygame.image.load('Fondos/Fondo Tutorial.png')
Fondo_Mini_Juego_1 = pygame.image.load('Fondos/Fondo Minijuego 1.png')
Fondo_Mini_Juego_2 = pygame.image.load('Fondos/Fondo Minijuego 2.png')
Fondo_Mini_Juego_3 = pygame.image.load('Fondos/Fondo Minijuego 3.png')
Fondo_Mini_Juego_4 = pygame.image.load('Fondos/Fondo Minijuego 4.png')
Fondo_Mini_Juego_5 = pygame.image.load('Fondos/Fondo Minijuego 5.png')
Fondo_inicio = Fondo_Menu

# Cargar botones
Boton_diseño = pygame.image.load('Botones/Boton.png')
Boton_Oscuro = pygame.image.load('Botones/Boton Oscuro.png')
Boton_return = pygame.image.load('Botones/Boton de Return.png')
Boton_ret_o = pygame.image.load('Botones/Boton de Return Oscuro.png')
Boton_inicio = Boton_diseño
Boton_Tutorial = pygame.image.load('Botones/Tutorial_Boton.png')
Boton_Tutorial_Oscuro = pygame.image.load('Botones/Tutorial_Boton Oscuro.png')
Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))
Boton_Play_Pausa = pygame.Rect(300, 400, 100, 50)
Boton_Restart = pygame.Rect(492, 398, 100, 50)

# Definir fuentes
Fuente_Botones = pygame.font.Font("Tipografias/ShowcardGothic.ttf", 30)
Fuente_pregunta = pygame.font.Font('Tipografias/cooper-black.ttf', 29)
Fuente_opcion = pygame.font.Font('Tipografias/cooper-black.ttf', 26)
Fuente_opcion_2 = pygame.font.Font('Tipografias/cooper-black.ttf', 35)
Fuente_opcion_3 = pygame.font.Font('Tipografias/cooper-black.ttf', 28)
Fuente_opcion_4 = pygame.font.Font('Tipografias/cooper-black.ttf', 20)
Fuente_opcion_5 = pygame.font.Font('Tipografias/cooper-black.ttf', 23)
Fuente_opcion_6 = pygame.font.Font('Tipografias/cooper-black.ttf', 25)
Fuente_texto = pygame.font.Font('Tipografias/ShowcardGothic.ttf', 25)

#Definir Imagen
Tesla = pygame.image.load('Personaje/Tesla.jpg')
Tesla = pygame.transform.scale(Tesla, (237, 301.1))
Atenea = pygame.image.load('Personaje/Atenea.jpg')
Atenea = pygame.transform.scale(Atenea, (235.1, 300.2))
Mirtha = pygame.image.load('Personaje/Mirtha Legrand.png')
Mirtha = pygame.transform.scale(Mirtha, (212.9, 299.3))
Gaster = pygame.image.load('Personaje/Gaster.png')
Gaster = pygame.transform.scale(Gaster, (236, 300))
Doctor_neo = pygame.image.load('Personaje/Doctor Neo.png')
Doctor_neo = pygame.transform.scale(Doctor_neo, (211.1, 295.9))
Mitsurugi = pygame.image.load('Personaje/Mitsurugi.png')
Mitsurugi = pygame.transform.scale(Mitsurugi, (236.4, 299.4))
Japon = pygame.image.load("Banderas/Japon.png")
Japon = pygame.transform.scale(Japon, (303, 179.7))
Ecuador = pygame.image.load("Banderas/Ecuador.png")
Ecuador = pygame.transform.scale(Ecuador, (303, 179.7))
Pakistan = pygame.image.load("Banderas/Pakistan.png")
Pakistan = pygame.transform.scale(Pakistan, (303, 179.7))
Grecia = pygame.image.load("Banderas/Grecia.png")
Grecia = pygame.transform.scale(Grecia, (303, 179.7))
Tailandia= pygame.image.load("Banderas/Tailandia.png")
Tailandia = pygame.transform.scale(Tailandia, (303, 179.7))
Egipto = pygame.image.load("Banderas/Egipto.png")
Egipto = pygame.transform.scale(Egipto, (303, 179.7))
Szboloszlai = pygame.image.load("FootBall/Szboloszlai.png")
Szboloszlai = pygame.transform.scale(Szboloszlai, (235.5, 300.1))
McGoat = pygame.image.load("FootBall/McGoat.png")
McGoat = pygame.transform.scale(McGoat, (235.5, 300.1))
Borhalland = pygame.image.load("FootBall/Borhalland.png")
Borhalland = pygame.transform.scale(Borhalland, (235.5, 300.1))
River = pygame.image.load("FootBall/river.png")
River = pygame.transform.scale(River, (235.5, 300.1))
Douglas = pygame.image.load("FootBall/douglas.png")
Douglas = pygame.transform.scale(Douglas, (235.5, 300.1))
Talleres = pygame.image.load("FootBall/talleres.png")
Talleres = pygame.transform.scale(Talleres, (235.5, 300.1))
Araña = pygame.image.load('Emoji/Araña.png')
Nene = pygame.image.load("Emoji/Nene.png")
Rayo = pygame.image.load("Emoji/Rayo.png")
Lentes = pygame.image.load("Emoji/Lentes.png")
Zorro = pygame.image.load("Emoji/Zorro.png")
Placa = pygame.image.load("Emoji/Placa.png")
Conejo = pygame.image.load("Emoji/Conejo.png")
Payaso = pygame.image.load("Emoji/Payaso.png")
Pistola = pygame.image.load("Emoji/Pistola.png")
Tv = pygame.image.load("Emoji/TV.png")
Serpiente = pygame.image.load("Emoji/Serpiente.png")
negro = pygame.image.load("Emoji/Negro.png")
Azul = pygame.image.load('Emoji/Azul.png')
Planeta =  pygame.image.load('Emoji/Planeta.png')
Arco =  pygame.image.load('Emoji/Arco.png')

# Información de preguntas
informacion = [
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Mente en Blanco', 'Caos', 'Extra', 'Sour Candy'],
     "Correcta": 0,
     "Posicion_Pre": (151, 55),
     "Posicion": [(26, 214), (740, 210), (75, 395), (694, 395)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Judas', 'Poker Face', 'Bad Romance', 'Blody Marry'],
     "Correcta": 1,
     "Posicion_Pre": (151, 55),
     "Posicion": [(76, 208), (699, 208), (24, 402), (690, 402)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Deja Vu', 'Loba', 'Acrosito', 'Objection'],
     "Correcta": 2,
     "Posicion_Pre": (151, 55),
     "Posicion": [(61, 208), (741, 208), (58, 399), (708, 399)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Man', 'Shake it Up', 'Bad Blood', 'Cruel Summer'],
     "Correcta": 3,
     "Posicion_Pre": (151, 55),
     "Posicion": [(84, 208), (694, 208), (46, 399), (692, 399)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Dance the Night', 'Leviatating', 'Houdini', 'Sweet Pie'],
     "Correcta": 0,
     "Posicion_Pre": (151, 55),
     "Posicion": [(26, 208), (696, 208), (60, 399), (702, 399)]
    },
    {"Pregunta": "¿Cuál es el nombre de la canción?",
     "Opcion": ['Taste', 'Please', 'Espresso', 'Feathers'],
     "Correcta": 0,
     "Posicion_Pre": (151, 55),
     "Posicion": [(77, 208), (730, 208), (56, 392), (716, 392)]
    },
    {"Pregunta": "¿Cuál es la capital de Italia?",
     "Opcion": ["A) Paris", "B) Roma", "C) Venecia", "D) Napoli"],
     "Correcta": 1,
     "Posicion_Pre": (240,285),
     "Posicion": [(144, 364), (471, 364), (144, 438), (471, 438)]
    },
    {"Pregunta": "¿Cuánto tarda la luz del sol en llegar a la Tierra?",
     "Opcion": ['A) 6 minutos', 'B) 8 segundos', 'C) 8 minutos', 'D) 6 segundos'],
     "Correcta": 2,
     "Posicion_Pre": (95,285),
     "Posicion": [(144, 364), (471, 364), (144, 438), (471, 438)]
    },
    {"Pregunta": "¿Cuál es el país más grande y el más pequeño?",
     "Opcion": ['A) Rusia y Vaticano', 'B) Rusia y China', 'C) EEUU y China', 'D) Rusia y EEUU'],
     "Correcta": 0,
     "Posicion_Pre": (110,285),
     "Posicion": [(144, 364), (471, 364), (144, 438), (471, 438)]
    },
    {"Pregunta": "¿Cuál palabra está escrita correctamente?",
     "Opcion": ['A) Conclullente', 'B) Mayor', 'C) Embaruyar', 'D) Soslalio'],
     "Correcta": 1,
     "Posicion_Pre": (140,285),
     "Posicion": [(144, 364), (471, 364), (144, 438), (471, 438)]
    },
    {"Pregunta": "¿Cuál de estas palabras se escribe con H?",
     "Opcion": ['A) Humillacion', 'B) Hiluso', 'C) Hinflar', 'D) Hinodoro'],
     "Correcta": 0,
     "Posicion_Pre": (145,285),
     "Posicion": [(144, 364), (471, 364), (144, 438), (471, 438)]
    },
    {"Pregunta": "¿Cuál de las palabras está bien escrita?",
     "Opcion": ['A) Mahonesa', 'B) Royo', 'C) Fayar', 'D) Hierba'],
     "Correcta": 3,
     "Posicion_Pre": (160,285),
     "Posicion": [(144, 364), (471, 364), (144, 438), (471, 438)]
    },
    {"Pregunta": "¿Adivina quien es el Personaje?",
     "Opcion": ['Galileo Galilei', 'Isaac Newton', 'Albert Einstein ', 'Nikola Tesla'],
     "Correcta": 3,
     "imagen": Tesla,
     "Posicion_Pre": (175,55),
     "imagen_posi": (95.7, 167.3),
     "Posicion": [(407, 224), (678, 224), (400, 398), (684, 398)]
    },
    {"Pregunta": "¿Adivina quien es el Personaje?",
     "Opcion": ['Mirtha Legrand', 'Moria Casan', 'Susana Gimenez', 'Lizy Tagliani'],
     "Correcta": 0,
     "imagen": Mirtha,
     "Posicion_Pre": (175,55),
     "imagen_posi": (107.7,168.2),
     "Posicion": [(400, 225), (685, 225), (400, 398), (684, 398)]
    },
    {"Pregunta": "¿Adivina quien es el Personaje?",
     "Opcion": ['Hera', 'Afrodita', 'Atenea', 'Demeter'],
     "Correcta": 2,
     "imagen": Atenea,
     "Posicion_Pre": (175,55),
     "imagen_posi": (96.6,168.2),
     "Posicion": [(463, 218), (695, 218), (442, 398), (695, 395)]
    },
    {"Pregunta": "¿A que Juego Pertenece?",
     "Opcion": ['EarthBound', 'Deltarune', 'Undertale', 'Final Fantasy'],
     "Correcta": 2,
     "imagen": Gaster,
     "Posicion_Pre": (220,55),
     "imagen_posi": (96.2,167.4),
     "Posicion": [(422, 225), (698, 225), (436, 398), (681, 398)]
    },
    {"Pregunta": "¿A que Juego Pertenece?",
     "Opcion": ['Ratchet & Clank', 'Bioumutant', 'Star Fox', 'Crash Bandicoot'],
     "Correcta": 3,
     "imagen": Doctor_neo,
     "Posicion_Pre": (220,55),
     "imagen_posi": (108.7,168.8),
     "Posicion": [(398, 225), (691, 225), (445, 398), (660, 398)]
    },
    {"Pregunta": "¿A que Juego Pertenece?",
     "Opcion": ['Mortal Kombat', 'Soulcalibur', 'Street Fighter', 'Injustice 2'],
     "Correcta": 1,
     "imagen": Mitsurugi,
     "Posicion_Pre": (220,55),
     "imagen_posi": (96.3,168),
     "Posicion": [(402, 225), (691, 225), (409, 398), (700, 398)]
    },
    {"Pregunta": "¿Cual es la pelicula?",
     "Opcion": ['Spiderman 1', 'The Amazing Spiderman', 'Spiderman no way home', 'Spiderman 2'],
     "Correcta": 2,
     "imagen 1": pygame.transform.scale(Araña, (101.8, 98.9)),
     "imagen 2": pygame.transform.scale(Araña, (101.8, 98.9)),
     "imagen 3": pygame.transform.scale(Araña, (101.8, 98.9)),
     "Posicion_Pre": (300,280),
     "imagen_posi 1": (195.6,136.6),
     "imagen_posi 2": (387.5,135.7),
     "imagen_posi 3": (567.2,137.8),
     "Posicion": [(219, 365), (460, 365), (144, 442), (534, 442)]
    },
    {"Pregunta": "¿Cual es la pelicula?",
     "Opcion": ['Harry Potter', 'Shazam', 'Electra', "Flash"],
     "Correcta": 0,
     "imagen 1": pygame.transform.scale(Nene, (100, 100)),
     "imagen 2": pygame.transform.scale(Lentes, (109.8, 109.8)),
     "imagen 3": pygame.transform.scale(Rayo, (67, 96.3)),
     "Posicion_Pre": (300,280),
     "imagen_posi 1": (196,138),
     "imagen_posi 2": (383.5,132),
     "imagen_posi 3": (586.2,138),
     "Posicion": [(202, 365), (545, 365), (230, 442), (558, 442)]
    },
    {"Pregunta": "¿Cual es la pelicula?",
     "Opcion": ['Jungle Book', 'Zootopia', 'Balto', 'Madagascar'],
     "Correcta": 1,
     "imagen 1": pygame.transform.scale(Zorro, (320.1, 180)),
     "imagen 2": pygame.transform.scale(Conejo, (202.1, 113.7)),
     "imagen 3": pygame.transform.scale(Placa, (95.8, 95.8)),
     "Posicion_Pre": (300,280),
     "imagen_posi 1": (83.8,96.1),
     "imagen_posi 2": (337.4,132.1),
     "imagen_posi 3": (570.8,147.2),
     "Posicion": [(201, 365), (541, 365), (246, 442), (528, 442)]
    },
    {"Pregunta": "¿Cual es la pelicula?",
     "Opcion": ['It', 'Batman', 'Terrifier', 'Joker'],
     "Correcta": 3,
     "imagen 1": pygame.transform.scale(Payaso, (223.5, 97)),
     "imagen 2": pygame.transform.scale(Pistola, (172.8, 115)),
     "imagen 3": pygame.transform.scale(Tv, (129.1, 193.9)),
     "Posicion_Pre": (300,280),
     "imagen_posi 1": (135.1,143.9),
     "imagen_posi 2": (346.7,128.6),
     "imagen_posi 3": (553.6,89.9),
     "Posicion": [(274, 365), (549, 365), (231, 442), (556, 442)]
    },
    {"Pregunta": "¿Cual es la pelicula?",
     "Opcion": ['Venom', 'Morbius', 'T-Rex', 'Madam Web'],
     "Correcta": 0,
     "imagen 1": pygame.transform.scale(Serpiente, (218.3, 113.7)),
     "imagen 2": pygame.transform.scale(Araña, (101.8, 98.9)),
     "imagen 3": pygame.transform.scale(negro, (111.3, 111.3)),
     "Posicion_Pre": (300,280),
     "imagen_posi 1": (138.7,121.7),
     "imagen_posi 2": (387.5,135.7),
     "imagen_posi 3": (562.4,130.5),
     "Posicion": [(237, 365), (544, 365), (244, 442), (528, 442)]
    },
    {"Pregunta": "¿Cual es la pelicula?",
     "Opcion": ['Megamente', 'Los Pitufos', 'Avatar', 'Alien'],
     "Correcta": 2,
     "imagen 1": pygame.transform.scale(Azul, (112.2, 112.2)),
     "imagen 2": pygame.transform.scale(Planeta, (152.8, 106.2)),
     "imagen 3": pygame.transform.scale(Arco, (192.8, 104.3)),
     "Posicion_Pre": (300,280),
     "imagen_posi 1": (190.7,130.8),
     "imagen_posi 2": (362,133.8),
     "imagen_posi 3": (519.8,137),
     "Posicion": [(204, 370), (527, 370), (234, 438), (557, 438)]
    },
    {"Pregunta": "¿Cuál es esta bandera?",
     "Opcion": ["China", "Corea del Sur", "Bangladesh", "Japón"],
     "Correcta": 3,
     "imagen": Japon,
     "Posicion_Pre": (230,55),
     "imagen_posi": (37.1,226.8),
     "Posicion": [(470, 225), (687, 225), (437, 400), (730, 400)],
    },
    {"Pregunta": "¿Cuál es esta bandera?",
     "Opcion": ["Venezuela", "Colombia", "Ecuador", "Bolivia"],
     "Correcta": 2,
     "imagen": Ecuador,
     "Posicion_Pre": (230,55),
     "imagen_posi": (37.1,226.8),
     "Posicion": [(447, 225), (713, 225), (460, 400), (727, 400)],
    },
    {"Pregunta": "¿Cuál es esta bandera?",
     "Opcion": ["Turkeministan", "Argelia", "Pakistan", "Turquia"],
     "Correcta": 2,
     "imagen": Pakistan,
     "Posicion_Pre": (230,55),
     "imagen_posi": (37.1,226.8),
     "Posicion": [(410, 225), (725, 225), (450, 400), (720, 400)],
    },
    {"Pregunta": "¿Cuál es esta bandera?",
     "Opcion": ["Honduras", "Grecia", "Uruguay", "Guatemala"],
     "Correcta": 1,
     "imagen": Grecia,
     "Posicion_Pre": (230,55),
     "imagen_posi": (37.1,226.8),
     "Posicion": [(447, 225), (730, 225), (452, 400), (707, 400)],
    },
    {"Pregunta": "¿Cuál es esta bandera?",
     "Opcion": ["Costa Rica", "Cuba", "Tailandia", "Croacia"],
     "Correcta": 2,
     "imagen": Tailandia,
     "Posicion_Pre": (230,55),
     "imagen_posi": (37.1,226.8),
     "Posicion": [(440, 225), (740, 225), (447, 400), (725, 400)],
    },
    {"Pregunta": "¿Cuál es esta bandera?",
     "Opcion": ["Yemen", "Egipto", "Irak", "Siria"],
     "Correcta": 1,
     "imagen": Egipto,
     "Posicion_Pre": (230,55),
     "imagen_posi": (37.1,226.8),
     "Posicion": [(462, 225), (730, 225), (475, 400), (740, 400)],
    },
    {"Pregunta": "¿ Cuál es este jugador?",
     "Opcion": ["Xhaka", "Wirtz", "Szoboszlai", "Bellingham"],
     "Correcta": 2,
     "imagen": Szboloszlai,
     "Posicion_Pre": (235,55),
     "imagen_posi": (96.4,167.8),
     "Posicion": [(465, 225), (730, 225), (442, 400), (700, 400)],
    },
    {"Pregunta": "¿ Cuál es este jugador?",
     "Opcion": ["Mac Allister", "McTominay", "Mcginn", "Veretout"],
     "Correcta": 1,
     "imagen": McGoat,
     "Posicion_Pre": (235,55),
     "imagen_posi": (96.4,167.8),
     "Posicion": [(430, 225), (700, 225), (460, 400), (717, 400)],
    },
    {"Pregunta": "¿ Cuál es este jugador?",
     "Opcion": ["De la cruz", "Pratto", "Paulo Diaz", "Borhalland"],
     "Correcta": 3,
     "imagen": Borhalland,
     "Posicion_Pre": (235,55),
     "imagen_posi": (96.4,167.8),
     "Posicion": [(444, 225), (728, 225), (440, 400), (700, 400)],
    },
    {"Pregunta": "¿ Cuál es este equipo?",
     "Opcion": ["Nacional Potosí", "River Plate", "River Plate(URU)", "Boca"],
     "Correcta": 0,
     "imagen": River,
     "Posicion_Pre": (235,55),
     "imagen_posi": (96.4,167.8),
     "Posicion": [(410, 225), (702, 225), (400, 400), (742, 400)],
    },
    {"Pregunta": "¿ Cuál es este equipo?",
     "Opcion": ["Newells", "Douglas", "Chacarita", "Colon"],
     "Correcta": 1,
     "imagen": Douglas,
     "Posicion_Pre": (235,55),
     "imagen_posi": (96.4,167.8),
     "Posicion": [(455, 225), (722, 225), (445, 400), (733, 400)],
    },
    {"Pregunta": "¿ Cuál es este equipo?",
     "Opcion": ["Barracas Central", "San Martín (T)", "Talleres", "Internacional"],
     "Correcta": 2,
     "imagen": Talleres,
     "Posicion_Pre": (235,55),
     "imagen_posi": (96.4,167.8),
     "Posicion": [(405, 225), (678, 225), (457, 400), (682, 400)],
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
            Audio = "Canciones/Sin Sonido.mp3"
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
    
# Función para dibujar el botón de inicio
def Boton_i(surface):
    Posi_mouse = pygame.mouse.get_pos()
    if Fondo_inicio == Fondo_Menu or Fondo_inicio == Fondo_Mini_Juego_1 or Fondo_inicio == Fondo_Mini_Juego_2 or Fondo_inicio == Fondo_Mini_Juego_3 or Fondo_inicio == Fondo_Mini_Juego_4 or Fondo_inicio == Fondo_Mini_Juego_5:
        if Fondo_inicio == Fondo_Menu:
            if Rectangulo.collidepoint(Posi_mouse):
                surface.blit(Boton_Oscuro, Rectangulo.topleft)
            else:
                surface.blit(Boton_diseño, Rectangulo.topleft)
        elif Fondo_inicio == Fondo_Mini_Juego_1 or Fondo_inicio == Fondo_Mini_Juego_2 or Fondo_inicio == Fondo_Mini_Juego_3:
            if Rectangulo.collidepoint(Posi_mouse):
                surface.blit(Boton_ret_o, Rectangulo.topleft)
            else:
                surface.blit(Boton_return, Rectangulo.topleft)
    else:
        None

# Función para dibujar el botón de Tutorial
def Boton_T(surface):
    Posi_mouse = pygame.mouse.get_pos()
    if Fondo_inicio == Fondo_Menu or Fondo_inicio == Fondo_Tutorial:
        if Fondo_inicio == Fondo_Menu:
            if Rectan.collidepoint(Posi_mouse):
                surface.blit(Boton_Tutorial_Oscuro, Rectan.topleft)
            else:
                surface.blit(Boton_Tutorial, Rectan.topleft)
        elif Fondo_inicio == Fondo_Tutorial:
            if Rectan.collidepoint(Posi_mouse):
                surface.blit(Boton_ret_o, Rectan.topleft)
            else:
                surface.blit(Boton_return, Rectan.topleft)
    else:
        None
# Función para dibujar el mini juego
def Mini_Juego(informacion_pregunta, tiempo):
    if Pregunta_actual <= 5:
        Pantalla.blit(Fondo_Mini_Juego_3,(0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            Usar = Fuente_opcion_5 if i == 0 else Fuente_opcion_3
            Usar_3 = Fuente_opcion_5 if i == 3 else Fuente_opcion_3
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
        Pantalla.blit(Texto, (815, 60))
    elif Pregunta_actual <= 11:
        Pantalla.blit(Fondo_Mini_Juego_1, (0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            if respuesta_correcta is not None:
                if i == informacion_pregunta["Correcta"]:
                    text = Fuente_opcion.render(option, True, Verde)
                elif i == Opcion_sel and not respuesta_correcta:
                    text = Fuente_opcion.render(option, True, Rojo)
                else:
                    text = Fuente_opcion.render(option, True, Blanco)
            else:
                if i == Opcion_sel:
                    text = Fuente_opcion.render(option, True, Negro)
                else:
                    text = Fuente_opcion.render(option, True, Blanco)
            Pantalla.blit(text, (x, y))
        Texto = Fuente_texto.render(str(tiempo), True, Blanco)
        Pantalla.blit(Texto, (818, 60))
    elif Pregunta_actual <= 17:
        Pantalla.blit(Fondo_Mini_Juego_2, (0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        Pantalla.blit(informacion_pregunta["imagen"], informacion_pregunta["imagen_posi"])
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            if Pregunta_actual == 13:
                Usar = Fuente_opcion_6 if i == 2 else Fuente_opcion
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
            elif Pregunta_actual == 14:
                if respuesta_correcta is not None:
                    if i == informacion_pregunta["Correcta"]:
                        text = Fuente_opcion_2.render(option, True, Verde)
                    elif i == Opcion_sel and not respuesta_correcta:
                        text = Fuente_opcion_2.render(option, True, Rojo)
                    else:
                        text = Fuente_opcion_2.render(option, True, Blanco)
                else:
                    if i == Opcion_sel:
                        text = Fuente_opcion_2.render(option, True, Negro)
                    else:
                        text = Fuente_opcion_2.render(option, True, Blanco)
                Pantalla.blit(text, (x, y))
            elif Pregunta_actual == 16:
                Usar = Fuente_opcion_6 if i == 0 or 4  else Fuente_opcion
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
            else:
                if respuesta_correcta is not None:
                    if i == informacion_pregunta["Correcta"]:
                        text = Fuente_opcion.render(option, True, Verde)
                    elif i == Opcion_sel and not respuesta_correcta:
                        text = Fuente_opcion.render(option, True, Rojo)
                    else:
                        text = Fuente_opcion.render(option, True, Blanco)
                else:
                    if i == Opcion_sel:
                        text = Fuente_opcion.render(option, True, Negro)
                    else:
                        text = Fuente_opcion.render(option, True, Blanco)
                Pantalla.blit(text, (x, y))
        Texto = Fuente_texto.render(str(tiempo), True, Blanco)
        Pantalla.blit(Texto, (818, 60))
    elif Pregunta_actual <= 23:
        Pantalla.blit(Fondo_Mini_Juego_4, (0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        Pantalla.blit(informacion_pregunta["imagen 1"], informacion_pregunta["imagen_posi 1"])
        Pantalla.blit(informacion_pregunta["imagen 2"], informacion_pregunta["imagen_posi 2"])
        Pantalla.blit(informacion_pregunta["imagen 3"], informacion_pregunta["imagen_posi 3"])
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            if Pregunta_actual == 18:
                Usar = Fuente_opcion_5 if i == 1 or 2 else Fuente_opcion
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
            else:
                if respuesta_correcta is not None:
                    if i == informacion_pregunta["Correcta"]:
                        text = Fuente_opcion.render(option, True, Verde)
                    elif i == Opcion_sel and not respuesta_correcta:
                        text = Fuente_opcion.render(option, True, Rojo)
                    else:
                        text = Fuente_opcion.render(option, True, Blanco)
                else:
                    if i == Opcion_sel:
                        text = Fuente_opcion.render(option, True, Negro)
                    else:
                        text = Fuente_opcion.render(option, True, Blanco)
                Pantalla.blit(text, (x, y))
        Texto = Fuente_texto.render(str(tiempo), True, Blanco)
        Pantalla.blit(Texto, (818, 60))
    elif Pregunta_actual <= 29:
        Pantalla.blit(Fondo_Mini_Juego_5, (0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        Pantalla.blit(informacion_pregunta["imagen"], informacion_pregunta["imagen_posi"])
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            if respuesta_correcta is not None:
                if i == informacion_pregunta["Correcta"]:
                    text = Fuente_opcion.render(option, True, Verde)
                elif i == Opcion_sel and not respuesta_correcta:
                    text = Fuente_opcion.render(option, True, Rojo)
                else:
                    text = Fuente_opcion.render(option, True, Blanco)
            else:
                if i == Opcion_sel:
                    text = Fuente_opcion.render(option, True, Negro)
                else:
                    text = Fuente_opcion.render(option, True, Blanco)
            Pantalla.blit(text, (x, y))
        Texto = Fuente_texto.render(str(tiempo), True, Blanco)
        Pantalla.blit(Texto, (818, 60))
    else:
        Pantalla.blit(Fondo_Mini_Juego_2, (0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        Pantalla.blit(informacion_pregunta["imagen"], informacion_pregunta["imagen_posi"])  
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            if Pregunta_actual == 33:
                Usar = Fuente_opcion_5 if i == 0 or 2 else Fuente_opcion
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
            elif Pregunta_actual == 35:
                Usar = Fuente_opcion_5 if i == 0 else Fuente_opcion
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
            else:
                if respuesta_correcta is not None:
                    if i == informacion_pregunta["Correcta"]:
                        text = Fuente_opcion.render(option, True, Verde)
                    elif i == Opcion_sel and not respuesta_correcta:
                        text = Fuente_opcion.render(option, True, Rojo)
                    else:
                        text = Fuente_opcion.render(option, True, Blanco)
                else:
                    if i == Opcion_sel:
                        text = Fuente_opcion.render(option, True, Negro)
                    else:
                        text = Fuente_opcion.render(option, True, Blanco)
                Pantalla.blit(text, (x, y))
        Texto = Fuente_texto.render(str(tiempo), True, Blanco)
        Pantalla.blit(Texto, (818, 60))
        
# Bucle principal
while True:
    Reloj = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if Rectangulo.collidepoint(mouse_pos):
                if Fondo_inicio == Fondo_Menu:
                    if Pregunta_actual <= 5:
                        Fondo_inicio = Fondo_Mini_Juego_3
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                        if not Jugando:
                            cargar_audio_y_video(Pregunta_actual)
                            reproducir_musica()
                            Jugando = True
                            Pausado = False
                    elif Pregunta_actual <= 11:
                        Fondo_inicio = Fondo_Mini_Juego_1
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                        if Video:
                            Video.release()
                            Video = None
                        Jugando = False
                        Pausado = False
                    elif Pregunta_actual <= 17:
                        Fondo_inicio = Fondo_Mini_Juego_2
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                        if Video:
                            Video.release()
                            Video = None
                        Jugando = False
                        Pausado = False
                    elif Pregunta_actual <= 23:
                        Fondo_inicio = Fondo_Mini_Juego_4
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                        if Video:
                            Video.release()
                            Video = None
                        Jugando = False
                        Pausado = False
                    elif Pregunta_actual <= 29:
                        Fondo_inicio = Fondo_Mini_Juego_5
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                        if Video:
                            Video.release()
                            Video = None
                        Jugando = False
                        Pausado = False
                    else:
                        Fondo_inicio = Fondo_Mini_Juego_2
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                        if Video:
                            Video.release()
                            Video = None
                        Jugando = False
                        Pausado = False
                else:
                    Fondo_inicio = Fondo_Menu
                    Boton_inicio = Boton_diseño
                    Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))
                    Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
                    if Video:
                        Video.release()
                        Video = None
                    detener_musica()
                    Jugando = False
                    Pausado = False
            if Rectan.collidepoint(event.pos):
                if Fondo_inicio == Fondo_Menu:
                    Fondo_inicio = Fondo_Tutorial
                    Boton_inicio = Boton_return
                    Rectan = Boton_return.get_rect(topleft=(10, 15))
                    if Video:
                        Video.release()
                        Video = None
                    Jugando = False
                    Pausado = False
                else:
                    Fondo_inicio = Fondo_Menu
                    Boton_inicio = Boton_Tutorial
                    Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
                    if Video:
                        Video.release()
                        Video = None
                    detener_musica()
                    Jugando = False
                    Pausado = False
            elif Jugando and event.type == pygame.MOUSEBUTTONDOWN:
                if Boton_Play_Pausa.collidepoint(mouse_pos):
                    if Pausado:
                        pygame.mixer.music.unpause()
                        Pausado = False
                    else:
                        pygame.mixer.music.pause()
                        Pausado = True
                elif Boton_Restart.collidepoint(mouse_pos):
                    detener_musica()
                    cargar_audio_y_video(Pregunta_actual)
                    reproducir_musica()
                    Video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    Pausado = False
        elif event.type == pygame.KEYDOWN:
            if Jugando:
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
                    if respuesta_correcta is None:
                        if Opcion_sel == informacion[Pregunta_actual]["Correcta"]:
                            Tiempo += 10
                            respuesta_correcta = True
                        else:
                            respuesta_correcta = False
                        if Pregunta_actual <= 5:
                            Mini_Juego(informacion[Pregunta_actual], Tiempo)
                            Botones(Pantalla, 'Play' if not Jugando else 'Pause' if not Pausado else 'Resume', Boton_Play_Pausa)
                            Botones(Pantalla, 'Restart', Boton_Restart)
                            Boton_i(Pantalla)
                            pygame.display.flip()
                            pygame.time.delay(500)
                            Pregunta_actual += 1
                            Opcion_sel = 0
                            respuesta_correcta = None
                            cargar_audio_y_video(Pregunta_actual)
                            reproducir_musica()
                        else:
                            Mini_Juego(informacion[Pregunta_actual], Tiempo)
                            Boton_i(Pantalla)
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
                                Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))
                                Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
                                Jugando = False
                                Pausado = False
                                detener_musica()
                            pygame.time.delay(500)
    Pantalla.blit(Fondo_inicio, (0, 0))
    if Fondo_inicio != Fondo_Menu:
        if Fondo_inicio != Fondo_Tutorial:
            if Fondo_inicio == Fondo_Mini_Juego_3:
                Boton_i(Pantalla)
                Boton_T(Pantalla)
                Mini_Juego(informacion[Pregunta_actual], Tiempo)
                if Video is not None and Jugando and not Pausado:
                    ret, frame = Video.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frame = cv2.transpose(frame)
                        frame = cv2.flip(frame, flipCode=1)
                        frame_surface = pygame.surfarray.make_surface(frame)
                        frame_surface = pygame.transform.scale(frame_surface, (400, 208))
                        Pantalla.blit(frame_surface, (245, 153))
                        pygame.draw.rect(Pantalla, Negro, (542, 308, 100, 50))
                    else:
                        Video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        detener_musica()
                if Pregunta_actual <= 5:
                    Botones(Pantalla, 'Play' if not Jugando else 'Pause' if not Pausado else 'Resume', Boton_Play_Pausa)
                    Botones(Pantalla, 'Restart', Boton_Restart)
                Reloj.tick(30)
        else:
            Boton_T(Pantalla)
            Boton_i(Pantalla)
            Pregunta_actual = 0
            Opcion_sel = 0
            Tiempo = 0
    else:
        Pantalla.blit(Fondo_inicio, (0, 0))
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_actual = 0
        Opcion_sel = 0
        Tiempo = 0
    pygame.display.update()
    pygame.display.flip()    