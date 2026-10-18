import pygame
# Inicializar el mezclador de audio si hace falta
if not pygame.mixer.get_init():
    pygame.mixer.init()
# Rutas de las canciones
tema_1 = "tema_1.mp3"
tema_2 = "tema_2.mp3"
# Tema predeterminado
tema_actual = [tema_1]

# Estado y volumen de la música
musica_activa = [True]
volumen_musica = [0.5]
def reproducir_musica():
    if musica_activa[0]:
        pygame.mixer.music.load(tema_actual[0])
        pygame.mixer.music.set_volume(volumen_musica[0])
        pygame.mixer.music.play(-1)
def detener_musica():
    pygame.mixer.music.stop()
def cambiar_tema(ruta):
    tema_actual[0] = ruta
    if musica_activa[0]:
        reproducir_musica()
def cambiar_volumen(volumen):
    volumen_musica[0] = float(volumen)
    pygame.mixer.music.set_volume(volumen_musica[0])
def activar_musica(activar):
    musica_activa[0] = activar
    if activar:
        reproducir_musica()
    else:
        detener_musica()
