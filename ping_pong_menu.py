import tkinter as tk
from PIL import Image, ImageTk
import jugador_vs_ia
import mejores_puntajes
import jugador_vs_jugador
import configuracion
import sonidos
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________#
window = tk.Tk()
window.title("Menú Ping Pong")
window.geometry("1100x800")
# Cantidad máxima de ventanas abiertas
ventanas_abiertas = [0]
# Cargar imagen de fondo
imagen = Image.open("fondo_definitivo_2.gif")
imagen = imagen.resize((1100, 800))
fondo = ImageTk.PhotoImage(imagen, master=window)
# Crear canvas
canvas = tk.Canvas(window, width=1100, height=800)
canvas.pack()
canvas.create_image(0, 0, image=fondo, anchor="nw")
#____________________________________________________________________________________________________________________________________________________________________________________________________________#
# Logo del juego
imagen = Image.open("logo_definitivo.png")
imagen = imagen.resize((600, 450))
logo = ImageTk.PhotoImage(imagen, master=window)
canvas.create_image(700, 50, image=logo, anchor="n")
#____________________________________________________________________________________________________________________________________________________________________________________________________#
# funciones para abrir los botones desde otras carpetas.
def abrir_jugador_vs_ia():
    jugador_vs_ia.abrir_jugador_vs_ia()
        
def abrir_ventana_puntajes():
    mejores_puntajes.mejores_puntajes()

def abrir_jugador_vs_jugador():
    jugador_vs_jugador.abrir_jugador_vs_jugador()

def abrir_configuracion():
    configuracion.abrir_configuracion()
    
def cerrar_ventana():
    window.destroy()
#____________________________________________________________________________________________________________________________________________________________________________________________________#
# botones del menu principal
boton1 = tk.Button( 
    window, 
    text="Jugador VS IA", 
    command=lambda: (sonidos.reproducir_sonido(), abrir_jugador_vs_ia()),
    font=("Impact", 16, "bold"), 
    bg="#4B7496", 
    fg="white" 
)
boton1.place(x=180, y=175, width=240, height=50)

boton2 = tk.Button( 
    window, 
    text="Jugador VS Jugador", 
    command=lambda: (sonidos.reproducir_sonido(), abrir_jugador_vs_jugador()),
    font=("Impact", 16, "bold"), 
    bg="#4B7496", 
    fg="white" 
)
boton2.place(x=180, y=300, width=240, height=50)

boton3 = tk.Button( 
    window, 
    text="Configuración", 
    command=lambda: (sonidos.reproducir_sonido(), abrir_configuracion()),
    font=("Impact", 16, "bold"), 
    bg="#4B7496", 
    fg="white" 
)
boton3.place(x=180, y=425, width=240, height=50)

boton4 = tk.Button( 
    window, 
    text="Mejores puntajes", 
    command=lambda: (sonidos.reproducir_sonido(), abrir_ventana_puntajes()),
    font=("Impact", 16, "bold"), 
    bg="#4B7496", 
    fg="white" 
)
boton4.place(x=180, y=550, width=240, height=50)

boton5 = tk.Button( 
    window, 
    text="Salir", 
    command=lambda: (sonidos.reproducir_sonido(), cerrar_ventana()),
    font=("Impact", 16, "bold"), 
    bg="#4B7496", 
    fg="white" 
)
boton5.place(x=180, y=675, width=240, height=50)
#___________________________________________________________________________________________________________________________________________________________________________________________________#
# Espacios de etiquetas diseños del menu principal 
label = tk.Label(
    window, 
    text="Seleccione una opción", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=100, y=50, width=400, height=50)

label = tk.Label(
    window, 
    text="Intrucciones de uso:", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=500, y=450, width=500, height=50)

label = tk.Label(
    window, 
    text="Evita que tu pelota", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=500, y=500, width=500, height=50)

label = tk.Label(
    window, 
    text="Entre a la cancha", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=500, y=550, width=500, height=50)

label = tk.Label(
    window, 
    text="Usa > W < para moverte arriba", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=500, y=600, width=500, height=50)

label = tk.Label(
    window, 
    text="Y > S < hacia abajo en PVP", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=500, y=650, width=500, height=50)

label = tk.Label(
    window, 
    text="usa up y down (las flechas)", 
    font=("Segoe UI Black", 24, "bold"), 
    bg="#292A2B", 
    fg="white" 
)
label.place(x=500, y=700, width=500, height=50)
#____________________________________________________________________________________________________________________________________________________________________________________________________#
window.mainloop()