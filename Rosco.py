import pygame
import sys

pygame.init()

Pantalla = pygame.display.set_mode((900, 508))
pygame.display.set_caption("Palabras Huergo")

Negro = (0, 0, 0)
Blanco = (255, 255, 255)


Fondo_Menu = pygame.image.load('Fondos Rosco/Fondo.png')
Fondo_Tutorial = pygame.image.load('Fondos Rosco/Fondo Tutorial(Rosco).png')
Fondo_Rosco = pygame.image.load('Fondos Rosco/Fondo Rosco.png')
Fondo_Final = pygame.image.load('Fondos Rosco/Fondo Victoria.png')
Fondo_inicio = Fondo_Menu

Boton_diseño = pygame.image.load('Botones/Boton.png')
Boton_Oscuro = pygame.image.load('Botones/Boton Oscuro.png')
Boton_return = pygame.image.load('Botones/Boton de Return.png')
Boton_ret_o = pygame.image.load('Botones/Boton de Return Oscuro.png')
Boton_retorno = pygame.image.load('Botones/Boton Retorno.png')
Boton_retorno_oscuro = pygame.image.load('Botones/Boton Retorno Oscuro.png')
Boton_inicio = Boton_diseño
Boton_Tutorial = pygame.image.load('Botones/Tutorial_Boton.png')
Boton_Tutorial_Oscuro = pygame.image.load('Botones/Tutorial_Boton Oscuro.png')
Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))
Boton_Pasapalabra = pygame.image.load('Botones/Pasapalabra.png')
Boton_Pasapalabra_Oscuro = pygame.image.load('Botones/Pasapalabra Oscuro.png')
Recta = Boton_Pasapalabra.get_rect(topleft=(660, 415))

Fuente_pregunta = pygame.font.Font('Tipografias/cooper-black.ttf', 22)
Fuente_texto = pygame.font.Font('Tipografias/ShowcardGothic.ttf', 25)
Fuente_resultado = pygame.font.Font('Tipografias/ShowcardGothic.ttf', 30)

rosco = [
    {"Tipo": "Empieza con A",
     "Pregunta": "Vehiculo motorizado que te permite volar",
     "Respuesta": "avion",
     "Verde": pygame.image.load('Letras/A_Verde.png'),
     "Rojo": pygame.image.load('Letras/A_Roja.png'),
     "Amarillo": pygame.image.load('Letras/A_Amarrilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (170, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene B",
     "Pregunta": "Animal que produce miel",
     "Respuesta": "abeja",
     "Verde": pygame.image.load('Letras/B_Verde.png'),
     "Rojo": pygame.image.load('Letras/B_Roja.png'),
     "Amarillo": pygame.image.load('Letras/B_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (260, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con C",
     "Pregunta": "Prenda de vestir con botones",
     "Respuesta": "camisa",
     "Verde": pygame.image.load('Letras/C_Verde.png'),
     "Rojo": pygame.image.load('Letras/C_Roja.png'),
     "Amarillo": pygame.image.load('Letras/C_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (245, 46),
     "Posicion_T": (320, 24),
     },        
    {"Tipo": "Empieza con D",
     "Pregunta": "Lugar donde viven una persona o un grupo",
     "Respuesta": "domicilio",
     "Verde": pygame.image.load('Letras/D_Verde.png'),
     "Rojo": pygame.image.load('Letras/D_Roja.png'),
     "Amarillo": pygame.image.load('Letras/D_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (165, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene E",
     "Pregunta": "Dispositivo para comunicarse",
     "Respuesta": "telefono",
     "Verde": pygame.image.load('Letras/E_Verde.png'),
     "Rojo": pygame.image.load('Letras/E_Roja.png'),
     "Amarillo": pygame.image.load('Letras/E_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (235, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con F",
     "Pregunta": "Titulo dado al rey en Egipto",
     "Respuesta": "faraon",
     "Verde": pygame.image.load('Letras/F_Verde.png'),
     "Rojo": pygame.image.load('Letras/F_Roja.png'),
     "Amarillo": pygame.image.load('Letras/F_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (245, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene G",
     "Pregunta": "Ave nacional de los Estados Unidos",
     "Respuesta": "aguila",
     "Verde": pygame.image.load('Letras/G_Verde.png'),
     "Rojo": pygame.image.load('Letras/G_Roja.png'),
     "Amarillo": pygame.image.load('Letras/G_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (215, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con H",
     "Pregunta": "Elemento que permite volar a un helicoptero",
     "Respuesta": "helice",
     "Verde": pygame.image.load('Letras/H_Verde.png'),
     "Rojo": pygame.image.load('Letras/H_Roja.png'),
     "Amarillo": pygame.image.load('Letras/H_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (155, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con I",
     "Pregunta": "Superheroe de Marvel",
     "Respuesta": "ironman",
     "Verde": pygame.image.load('Letras/I_Verde.png'),
     "Rojo": pygame.image.load('Letras/I_Roja.png'),
     "Amarillo": pygame.image.load('Letras/I_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (275, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con J",
     "Pregunta": "Lo utilizamos para limpiarnos",
     "Respuesta": "jabon",
     "Verde": pygame.image.load('Letras/J_Verde.png'),
     "Rojo": pygame.image.load('Letras/J_Roja.png'),
     "Amarillo": pygame.image.load('Letras/J_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (235, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con L",
     "Pregunta": "Animal que perdio contra una tortuga",
     "Respuesta": "liebre",
     "Verde": pygame.image.load('Letras/L_Verde.png'),
     "Rojo": pygame.image.load('Letras/L_Roja.png'),
     "Amarillo": pygame.image.load('Letras/L_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (190, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con M",
     "Pregunta": "El fruto prohibido",
     "Respuesta": "manzana",
     "Verde": pygame.image.load('Letras/M_Verde.png'),
     "Rojo": pygame.image.load('Letras/M_Roja.png'),
     "Amarillo": pygame.image.load('Letras/M_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (300, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene N",
     "Pregunta": "Si uno no paga con billetes paga con",
     "Respuesta": "monedas",
     "Verde": pygame.image.load('Letras/N_Verde.png'),
     "Rojo": pygame.image.load('Letras/N_Roja.png'),
     "Amarillo": pygame.image.load('Letras/N_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (205, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con Ñ",
     "Pregunta": "Personaje del chabo del 8",
     "Respuesta": "ñoño",
     "Verde": pygame.image.load('Letras/Ña_Verde.png'),
     "Rojo": pygame.image.load('Letras/Ña_Roja.png'),
     "Amarillo": pygame.image.load('Letras/Ña_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (265, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con O",
     "Pregunta": "Instrumento de cocina",
     "Respuesta": "olla",
     "Verde": pygame.image.load('Letras/O_Verde.png'),
     "Rojo": pygame.image.load('Letras/O_Roja.png'),
     "Amarillo": pygame.image.load('Letras/O_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (275, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene P",
     "Pregunta": "Se le llama al comienzo de un espectaculo",
     "Respuesta": "apertura",
     "Verde": pygame.image.load('Letras/P_Verde.png'),
     "Rojo": pygame.image.load('Letras/P_Roja.png'),
     "Amarillo": pygame.image.load('Letras/P_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (175, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Contiene Q",
     "Pregunta": "Sinonimo de repugnante",
     "Respuesta": "asqueroso",
     "Verde": pygame.image.load('Letras/Q_Verde.png'),
     "Rojo": pygame.image.load('Letras/Q_Roja.png'),
     "Amarillo": pygame.image.load('Letras/Q_Amarrilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (270, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con R",
     "Pregunta": "Genero musical que toca la banda Soda Stereo",
     "Respuesta": "rock",
     "Verde": pygame.image.load('Letras/R_Verde.png'),
     "Rojo": pygame.image.load('Letras/R_Roja.png'),
     "Amarillo": pygame.image.load('Letras/R_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (150, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con S",
     "Pregunta": "Famosa pelicula la Princesa y el",
     "Respuesta": "sapo",
     "Verde": pygame.image.load('Letras/S_Verde.png'),
     "Rojo": pygame.image.load('Letras/S_Roja.png'),
     "Amarillo": pygame.image.load('Letras/S_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (225, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene T",
     "Pregunta": "El opuesto de adelante",
     "Respuesta": "atras",
     "Verde": pygame.image.load('Letras/T_Verde.png'),
     "Rojo": pygame.image.load('Letras/T_Roja.png'),
     "Amarillo": pygame.image.load('Letras/T_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (275, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con U",
     "Pregunta": "Villana de disney",
     "Respuesta": "ursula",
     "Verde": pygame.image.load('Letras/U_Verde.png'),
     "Rojo": pygame.image.load('Letras/U_Roja.png'),
     "Amarillo": pygame.image.load('Letras/U_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (305, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con V",
     "Pregunta": "Famosa saga de peliculas de terror",
     "Respuesta": "viernes 13",
     "Verde": pygame.image.load('Letras/V_Verde.png'),
     "Rojo": pygame.image.load('Letras/V_Roja.png'),
     "Amarillo": pygame.image.load('Letras/V_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (225, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Contiene X",
     "Pregunta": "Lo que genera una bomba",
     "Respuesta": "explosion",
     "Verde": pygame.image.load('Letras/X_Verde.png'),
     "Rojo": pygame.image.load('Letras/X_Roja.png'),
     "Amarillo": pygame.image.load('Letras/X_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (265, 46),
     "Posicion_T": (340, 24),
     },
    {"Tipo": "Empieza con Y",
     "Pregunta": "Postre de leche con sabor a frutas",
     "Respuesta": "yogur",
     "Verde": pygame.image.load('Letras/Y_Verde.png'),
     "Rojo": pygame.image.load('Letras/Y_Roja.png'),
     "Amarillo": pygame.image.load('Letras/Y_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (220, 46),
     "Posicion_T": (320, 24),
     },
    {"Tipo": "Empieza con Z",
     "Pregunta": "Prenda de vestir formal que se usa en los pies",
     "Respuesta": "zapato",
     "Verde": pygame.image.load('Letras/Z_Verde.png'),
     "Rojo": pygame.image.load('Letras/Z_Roja.png'),
     "Amarillo": pygame.image.load('Letras/Z_Amarilla.png'),
     "Imagen_posi": (462, 86),
     "Posicion_Pre": (155, 46),
     "Posicion_T": (320, 24),
     },
]

Pregunta_actual = 0
Tiempo = 0
Correctas = 0
Incorrectas = 0
Respuesta = ""

def Pasapalabra(surface):
    Posi_mouse = pygame.mouse.get_pos()
    if Recta.collidepoint(Posi_mouse):
        surface.blit(Boton_Pasapalabra_Oscuro, Recta.topleft)
    else:
        surface.blit(Boton_Pasapalabra, Recta.topleft)

def Boton_i(surface):
    Posi_mouse = pygame.mouse.get_pos()
    if Fondo_inicio == Fondo_Menu:
        if Rectangulo.collidepoint(Posi_mouse):
            surface.blit(Boton_Oscuro, Rectangulo.topleft)
        else:
            surface.blit(Boton_diseño, Rectangulo.topleft)
    elif Fondo_inicio == Fondo_Rosco:
        if Rectangulo.collidepoint(Posi_mouse):
            surface.blit(Boton_ret_o, Rectangulo.topleft)
        else:
            surface.blit(Boton_return, Rectangulo.topleft)
    elif Fondo_inicio == Fondo_Final:
        if Rectangulo.collidepoint(Posi_mouse):
            surface.blit(Boton_retorno_oscuro, Rectangulo.topleft)
        else:
            surface.blit(Boton_retorno, Rectangulo.topleft)

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
        
def Rosco(informacion_pregunta, tiempo):
    if Fondo_inicio == Fondo_Rosco:
        Pantalla.blit(Fondo_Rosco, (0, 0))
        Pregunta_text = Fuente_pregunta.render(informacion_pregunta["Pregunta"], True, Blanco)
        Pantalla.blit(Pregunta_text, informacion_pregunta["Posicion_Pre"])
        Tipo_text = Fuente_pregunta.render(informacion_pregunta["Tipo"], True, Blanco)
        Pantalla.blit(Tipo_text, informacion_pregunta["Posicion_T"])
        Texto = Fuente_texto.render(str(int(tiempo)), True, Blanco)
        Pantalla.blit(Texto, (815, 47))
        if Correctas < 10:
            Correcto = Fuente_resultado.render(str(int(Correctas)), True, Blanco)
            Pantalla.blit(Correcto, (186, 438))
        else:
            Correcto = Fuente_resultado.render(str(int(Correctas)), True, Blanco)
            Pantalla.blit(Correcto, (180, 438))
        if Incorrectas < 10:
            inco = Fuente_resultado.render(str(int(Incorrectas)), True, Blanco)
            Pantalla.blit(inco, (68, 438))
        else:
            inco = Fuente_resultado.render(str(int(Incorrectas)), True, Blanco)
            Pantalla.blit(inco, (62, 438)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if Rectangulo.collidepoint(mouse_pos):
                if Fondo_inicio == Fondo_Menu:
                    if Pregunta_actual < len(rosco):
                        Fondo_inicio = Fondo_Rosco
                        Boton_inicio = Boton_return
                        Rectangulo = Boton_return.get_rect(topleft=(10, 15))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                    elif Pregunta_actual > len(rosco):
                        Fondo_inicio = Fondo_Final
                        Boton_inicio = Boton_retorno
                        Rectangulo = Boton_retorno.get_rect(topleft=(325, 320))
                        Rectan = Boton_ret_o.get_rect(topleft=(900, 15))
                else:
                    Fondo_inicio = Fondo_Menu
                    Boton_inicio = Boton_diseño
                    Rectangulo = Boton_diseño.get_rect(topleft=(325, 230))
                    Rectan = Boton_Tutorial.get_rect(topleft=(338, 320))
            if Recta.collidepoint(mouse_pos):
                Pregunta_actual += 1
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
            if Fondo_inicio == Fondo_Rosco:
                if event.key == pygame.K_RETURN:
                    if Respuesta.lower() == rosco[Pregunta_actual]["Respuesta"]:
                        Correctas += 1
                    else:
                        Incorrectas += 1
                    Respuesta = ""
                    Pregunta_actual += 1
                    if Pregunta_actual < len(rosco):
                        Rosco(rosco[Pregunta_actual], Tiempo)
                    else:
                        Fondo_inicio = Fondo_Final
                        Pregunta_actual = 0
                elif event.key == pygame.K_BACKSPACE:
                    Respuesta = Respuesta[:-1]
                else:
                    Respuesta += event.unicode
    Pantalla.blit(Fondo_inicio, (0, 0))
    if Fondo_inicio != Fondo_Menu:
        if Fondo_inicio == Fondo_Rosco:
            Rosco(rosco[Pregunta_actual], Tiempo)
            Boton_i(Pantalla)
            Pasapalabra(Pantalla)
            Texto_Respuesta = Fuente_pregunta.render(Respuesta, True, Blanco)
            Pantalla.blit(Texto_Respuesta, (300, 280))
        elif Fondo_inicio == Fondo_Final:
            Boton_i(Pantalla)
            Rectangulo = Boton_retorno.get_rect(topleft=(285, 400))
            Correcto = Fuente_resultado.render(str(int(Correctas)), True, Blanco)
            Pantalla.blit(Correcto, (510, 345))
            inco = Fuente_resultado.render(str(int(Incorrectas)), True, Blanco)
            Pantalla.blit(inco, (365, 345))
        elif Fondo_inicio == Fondo_Tutorial:
            Boton_T(Pantalla)
            Pregunta_actual = 0
            Opcion_sel = 0
            Tiempo = 0
    else:
        Boton_i(Pantalla)
        Boton_T(Pantalla)
        Pregunta_actual = 0
        Correctas = 0
        Incorrectas = 0
    pygame.display.flip()