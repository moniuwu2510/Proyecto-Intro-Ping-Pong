import pygame
if not pygame.mixer.get_init():
    pygame.mixer.init()
sonido_boton = pygame.mixer.Sound("boton_efecto.mp3")
sonido_boton.set_volume(0.5)
# Estado de los efectos de sonido
efectos_activos = [True]
def reproducir_sonido():
    if efectos_activos[0]:
        sonido_boton.play()
def activar_efectos(activar):
    efectos_activos[0] = activar