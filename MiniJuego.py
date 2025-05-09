import pygame
import sys
pygame.init()

Pantalla = pygame.display.set_mode((900, 508))
pygame.display.set_caption("Palabras Huergo")

Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Verde = (0, 255, 0)
Rojo = (255, 0, 0)

Fondo_Menu = pygame.image.load('Fondos/Fondo.jpg')
Fondo_Tutorial = pygame.image.load('Fondos/Fondo Tutorial.png')
Fondo_Mini_Juego_1 = pygame.image.load('Fondos/Fondo MiniJuegos 1.png')
Fondo_Mini_Juego_2 = pygame.image.load('Fondos/Fondo MiniJuegos 2.png')
Fondo_inicio = Fondo_Menu

Boton_diseño = pygame.image.load('Botones/Boton.png')
Boton_Oscuro = pygame.image.load('Botones/Boton Oscuro.png')
Boton_return = pygame.image.load('Botones/Boton de Return.png')
Boton_ret_o = pygame.image.load('Botones/Boton de Return Oscuro.png')
Boton_inicio = Boton_diseño
Boton_Tutorial = pygame.image.load('Botones/Tutorial_Boton.png')
Boton_Tutorial_Oscuro = pygame.image.load('Botones/Tutorial_Boton Oscuro.png')
Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))

Fuente_texto = pygame.font.Font('Tipografias/ShowcardGothic.ttf', 25)
Fuente_pregunta = pygame.font.Font('Tipografias/cooper-black.ttf', 30)
Fuente_opcion = pygame.font.Font('Tipografias/cooper-black.ttf', 24)
Fuente_opcion_2 = pygame.font.Font('Tipografias/cooper-black.ttf', 35)

informacion = [
    {"Pregunta": "¿Cuál es la capital de Italia?",
     "Opcion": ["A) Paris", "B) Roma", "C) Venecia", "D) Napoli"],
     "Correcta": 1,
     "Posicion_Pre": (240,280),
     "Posicion": [(180, 370), (480, 370), (180, 438), (480, 438)]
    },
    {"Pregunta": "¿Cuánto tarda la luz del sol en llegar a la Tierra?",
     "Opcion": ['A) 6 minutos', 'B) 8 segundos', 'C) 8 minutos', 'D) 6 segundos'],
     "Correcta": 2,
     "Posicion_Pre": (85,280),
     "Posicion": [(180, 370), (480, 370), (180, 438), (480, 438)]
    },
    {"Pregunta": "¿Cuál es el país más grande y el más pequeño?",
     "Opcion": ['A) Rusia y Vaticano', 'B) Rusia y China', 'C) EEUU y China', 'D) Rusia y EEUU'],
     "Correcta": 0,
     "Posicion_Pre": (100,280),
     "Posicion": [(180, 370), (480, 370), (180, 438), (480, 438)]
    },
    {"Pregunta": "¿Cuál palabra está escrita correctamente?",
     "Opcion": ['A) Conclullente', 'B) Mayor', 'C) Embaruyar', 'D) Soslalio'],
     "Correcta": 1,
     "Posicion_Pre": (130,280),
     "Posicion": [(180, 370), (480, 370), (180, 438), (480, 438)]
    },
    {"Pregunta": "¿Cuál de estas palabras se escribe con H?",
     "Opcion": ['A) Humillacion', 'B) Hiluso', 'C) Hinflar', 'D) Hinodoro'],
     "Correcta": 0,
     "Posicion_Pre": (140,280),
     "Posicion": [(180, 370), (480, 370), (180, 438), (480, 438)]
    },
    {"Pregunta": "¿Cuál de las palabras está bien escrita?",
     "Opcion": ['A) Mahonesa', 'B) Royo', 'C) Fayar', 'D) Hierba'],
     "Correcta": 3,
     "Posicion_Pre": (140,280),
     "Posicion": [(180, 370), (480, 370), (180, 438), (480, 438)]
    },
    {"Pregunta": "¿Adivina quien es el Personaje?",
     "Opcion": ['Galileo Galilei', 'Isaac Newton', 'Albert Einstein ', 'Nikola Tesla'],
     "Correcta": 3,
     "imagen": pygame.image.load('Personaje/Tesla.jpg'),
     "Posicion_Pre": (155,55),
     "imagen_posi": (100,178),
     "Posicion": [(445, 225), (692, 225), (438, 405), (697, 405)]
    },
    {"Pregunta": "¿Adivina quien es el Personaje?",
     "Opcion": ['Mirtha Legrand', 'Moria Casan', 'Susana Gimenez', 'Lizy Tagliani'],
     "Correcta": 0,
     "imagen": pygame.image.load('Personaje/Mirtha Legrand.png'),
     "Posicion_Pre": (155,55),
     "imagen_posi": (113,178),
     "Posicion": [(438, 225), (700, 225), (433, 405), (696, 405)]
    },
    {"Pregunta": "¿Adivina quien es el Personaje?",
     "Opcion": ['Hera', 'Afrodita', 'Atenea', 'Demeter'],
     "Correcta": 2,
     "imagen": pygame.image.load('Personaje/Atenea.jpg'),
     "Posicion_Pre": (155,55),
     "imagen_posi": (110,178),
     "Posicion": [(490, 220), (698, 220), (470, 400), (700, 400)]
    },
    {"Pregunta": "¿A que Juego Pertenece?",
     "Opcion": ['EarthBound', 'Deltarune', 'Undertale', 'Final Fantasy'],
     "Correcta": 2,
     "imagen": pygame.image.load('Personaje/Gaster.png'),
     "Posicion_Pre": (200,55),
     "imagen_posi": (95,178),
     "Posicion": [(458, 225), (715, 225), (468, 405), (692, 405)]
    },
    {"Pregunta": "¿A que Juego Pertenece?",
     "Opcion": ['Ratchet & Clank', 'Bioumutant', 'Star Fox', 'Crash Bandicoot'],
     "Correcta": 3,
     "imagen": pygame.image.load('Personaje/Doctor Neo.png'),
     "Posicion_Pre": (200,55),
     "imagen_posi": (105,178),
     "Posicion": [(432, 225), (700, 225), (482, 405), (674, 405)]
    },
    {"Pregunta": "¿A que Juego Pertenece?",
     "Opcion": ['Mortal Kombat', 'Soulcalibur', 'Street Fighter', 'Injustice 2'],
     "Correcta": 1,
     "imagen": pygame.image.load('Personaje/Mitsurugi.png'),
     "Posicion_Pre": (200,55),
     "imagen_posi": (95,178),
     "Posicion": [(440, 225), (705, 225), (445, 405), (710, 405)]
    },
]
Pregunta_actual = 0
Opcion_sel = 0
Tiempo = 0
respuesta_correcta = None 
def Boton_i(surface):
    Posi_mouse = pygame.mouse.get_pos()
    if Fondo_inicio == Fondo_Menu or Fondo_inicio == Fondo_Mini_Juego_1 or Fondo_inicio == Fondo_Mini_Juego_2:
        if Fondo_inicio == Fondo_Menu:
            if Rectangulo.collidepoint(Posi_mouse):
                surface.blit(Boton_Oscuro, Rectangulo.topleft)
            else:
                surface.blit(Boton_diseño, Rectangulo.topleft)
        elif Fondo_inicio == Fondo_Mini_Juego_1:
            if Rectangulo.collidepoint(Posi_mouse):
                surface.blit(Boton_ret_o, Rectangulo.topleft)
            else:
                surface.blit(Boton_return, Rectangulo.topleft)

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

def Mini_Juego(informacion_pregunta, tiempo):
    if Pregunta_actual < 6:
        Pantalla.blit(Fondo_Mini_Juego_1, (0, 0))
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
        Pantalla.blit(Texto, (815, 47))
    else:
        Pantalla.blit(Fondo_Mini_Juego_2, (0, 0))
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        Pantalla.blit(informacion_pregunta["imagen"], informacion_pregunta["imagen_posi"])
        for i, option in enumerate(informacion_pregunta["Opcion"]):
            x, y = informacion_pregunta["Posicion"][i]
            if Pregunta_actual == 8:
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
        Pantalla.blit(Texto, (815, 47))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Rectangulo.collidepoint(event.pos):
                if Fondo_inicio == Fondo_Menu:
                    if Pregunta_actual < 6:
                        Fondo_inicio = Fondo_Mini_Juego_1
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                    else:
                        Fondo_inicio = Fondo_Mini_Juego_2
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                else:
                    Fondo_inicio = Fondo_Menu
                    Boton_inicio = Boton_diseño
                    Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))
                    Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
            if Rectan.collidepoint(event.pos):
                if Fondo_inicio == Fondo_Menu:
                    Fondo_inicio = Fondo_Tutorial
                    Boton_inicio = Boton_return
                    Rectan = Boton_return.get_rect(topleft=(10, 15))
                else:
                    Fondo_inicio = Fondo_Menu
                    Boton_inicio = Boton_Tutorial
                    Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
        elif event.type == pygame.KEYDOWN:
            if Fondo_inicio != Fondo_Menu:
                if event.key == pygame.K_LEFT:
                    Opcion_sel = (Opcion_sel - 1) % len(informacion[Pregunta_actual]["Opcion"])
                    respuesta_correcta = None 
                elif event.key == pygame.K_RIGHT:
                    Opcion_sel = (Opcion_sel + 1) % len(informacion[Pregunta_actual]["Opcion"])
                    respuesta_correcta = None 
                elif event.key == pygame.K_RETURN:
                    if Opcion_sel == informacion[Pregunta_actual]["Correcta"]:
                        Tiempo += 10
                        respuesta_correcta = True
                    else:
                        Tiempo += 0
                        respuesta_correcta = False
                    Mini_Juego(informacion[Pregunta_actual], Tiempo)
                    Boton_i(Pantalla)
                    Boton_T(Pantalla)
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
                    pygame.time.delay(500)
    Pantalla.blit(Fondo_inicio, (0, 0))
    if Fondo_inicio != Fondo_Menu:
        if Fondo_inicio == Fondo_Tutorial:
            Boton_T(Pantalla)
            Boton_i(Pantalla)
        else:
            Mini_Juego(informacion[Pregunta_actual], Tiempo)
            Boton_i(Pantalla)
            Boton_T(Pantalla)
    else:
        Boton_T(Pantalla)
        Boton_i(Pantalla)
        Pregunta_actual = 0
        Opcion_sel = 0
        Tiempo = 0
    pygame.display.flip()