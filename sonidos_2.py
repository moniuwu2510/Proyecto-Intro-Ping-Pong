import pygame
import sonidos
sonido_rebote = pygame.mixer.Sound("rebote_efecto.mp3")
sonido_victoria = pygame.mixer.Sound("victoria_efecto.mp3")
sonido_rebote.set_volume(0.5)
sonido_victoria.set_volume(0.5)
def reproducir_rebote():
    if sonidos.efectos_activos[0]:
        sonido_rebote.play()
def reproducir_victoria():
    if sonidos.efectos_activos[0]:
        sonido_victoria.play()

