from py_compile import main
import tkinter as tk
from PIL import Image, ImageTk
import sonidos
import musica
import personalizaciones
#_____________________________________________________________________________________________________________________________________________________________________#
def abrir_configuracion():
    window = tk.Toplevel()
    window.title("Configuración y Personalización")
    window.geometry("600x500")
    window.resizable(False, False)
# Fondo
    imagen = Image.open("fondo_definitivo_2.gif")
    imagen = imagen.resize((600, 500))
    fondo = ImageTk.PhotoImage(imagen, master=window)
    canvas = tk.Canvas(
        window,
        width=600,
        height=500,
        highlightthickness=0
    )
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=fondo, anchor="nw")
    canvas.fondo = fondo
#_______________________________________________________________________________________________________________________________________________________________________#
# comenzamos a crear etiquetas y botones   
    label = tk.Label(
        window, 
        text="Configuración", 
        font=("Segoe UI Black", 24, "bold"), 
        bg="#292A2B", 
        fg="white" 
    )
    label.place(x=150, y=50, width=300, height=50) 
    
    def cambiar_efectos(): # para los efectos de sonido usamos listas y recursividad si esta apagado podemos activarlo actualizando el estado actual y lo actualiza
        estado_actual = not sonidos.efectos_activos[0]
        sonidos.activar_efectos(estado_actual)
        if estado_actual:
            boton_musica.config(text="Efectos: Activados")
        else:
            boton_musica.config(text="Efectos: Desactivados")
# Aquí conectaremos el control con el sistema de audio
    if sonidos.efectos_activos[0]:
        texto_efectos = "Efectos: Activados"
    else:
        texto_efectos = "Efectos: Desactivados"
    boton_musica = tk.Button(
        window,
        text=texto_efectos,
        command=lambda: (sonidos.reproducir_sonido(), cambiar_efectos()),
        font=("Impact", 15, "bold"),
        bg="#4B7496",
        fg="white",
        width=20,
        height=1
    )
    boton_musica.place(x=180, y=125)
    label = tk.Label(
        window, 
        text="Sonido", 
        font=("Segoe UI Black", 24, "bold"), 
        bg="#292A2B", 
        fg="white" 
    )
    label.place(x=200, y=200, width=200, height=50)
# barra de volumen
    volumen = tk.DoubleVar(value=musica.volumen_musica[0] * 100)
    barra_volumen = tk.Scale(
        window,
        from_=0,
        to=100,
        orient="horizontal",
        variable=volumen,
        length=300,
        showvalue=True,
        resolution=1,
        font=("Arial", 10, "bold"),
        bg="#4B7496",
        fg="white",
        troughcolor="white",
        highlightthickness=0,
        command=lambda valor: musica.cambiar_volumen(float(valor) / 100)
    )
    barra_volumen.place(x=150, y=275)
    # Controlar el volumen de la música
    def ajustar_volumen(valor):
        musica.cambiar_volumen(float(valor) / 100)
    barra_volumen.config(command=ajustar_volumen)

# boton de personalizaciones de musica seleccion de fondo, musica y cambios de colores en las paletas
    boton_personalizaciones = tk.Button(
        window,
        text="Personalizaciones",
        command=lambda: (
            sonidos.reproducir_sonido(),
            personalizaciones.abrir_personalizaciones(window)
        ),
        font=("Impact", 15, "bold"),
        bg="#4B7496",
        fg="white",
        width=20,
        height=1
    )
    boton_personalizaciones.place(x=180, y=350)
