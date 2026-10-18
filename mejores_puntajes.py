from py_compile import main
import tkinter as tk 
from PIL import Image, ImageTk 
#____________________________________________________________________________________________________________________________________________________________________________________________________#
def guardar_puntaje(nombre, puntos, dificultad):
    try:
        archivo = open("mejores_puntajes.txt", "r")
        resultados = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        resultados = []
    resultado = nombre + "," + str(puntos) + "," + dificultad + "\n"
    resultados.append(resultado)

    resultados.sort(
        key=lambda linea: int(linea.strip().split(",")[1]),
        reverse=True
    )
    resultados = resultados[:10]
    archivo = open("mejores_puntajes.txt", "w")
    archivo.writelines(resultados)
    archivo.close()
#____________________________________________________________________________________________________________________________________________________________________________________________________#
def mejores_puntajes():
    window = tk.Toplevel()
    window.title("Mejores Puntajes")
    window.geometry("600x500")
    # Fondo
    imagen = Image.open("fondo_definitivo_2.gif")
    imagen = imagen.resize((600, 500))
    fondo = ImageTk.PhotoImage(imagen, master=window)
    canvas = tk.Canvas(window, width=600, height=500, highlightthickness=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=fondo, anchor="nw")
    # Guardar la imagen para que Tkinter no la elimine
    canvas.fondo = fondo
    # Título de la ventana
    titulo = tk.Label(
        window,
        text="🏆 MEJORES PUNTAJES",
        font=("Segoe UI Black", 22, "bold"),
        bg="#292A2B",
        fg="white"
    )
    titulo.place(x=100, y=25, width=400, height=45)
    # Encabezados de la tabla
    label_posicion = tk.Label(
        window,
        text="Pos.",
        font=("Segoe UI Black", 12, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_posicion.place(x=35, y=100, width=55, height=30)
#____________________________________________________________________________________________________________________________________________________________________________________
# Espacios para mostrar los 10 mejores resultados
    posiciones = []
    for i in range(10):
        etiqueta = tk.Label(
            window,
            text=str(i + 1),
            font=("Arial", 12, "bold"),
            bg="#292A2B",
            fg="white"
        )
        etiqueta.place(x=35, y=140 + i * 30, width=55, height=25)
        posiciones.append(etiqueta)
    nombres = []
    for i in range(10): # espacio para mostrar los nombres de los jugadores
        etiqueta = tk.Label(
            window,
            text="---",
            font=("Arial", 12),
            bg="#292A2B",
            fg="white"
        )
        etiqueta.place(x=100, y=140 + i * 30, width=200, height=25)
        nombres.append(etiqueta)
    puntos = []
    for i in range(10): # espacio para mostrar los puntajes de los jugadores
        etiqueta = tk.Label(
            window,
            text="---",
            font=("Arial", 12),
            bg="#292A2B",
            fg="white"
        )
        etiqueta.place(x=315, y=140 + i * 30, width=90, height=25)
        puntos.append(etiqueta)
    dificultades = []
    for i in range(10): # espacio para mostrar las dificultades a la que le jugador jugó
        etiqueta = tk.Label(
            window,
            text="---",
            font=("Arial", 12),
            bg="#292A2B",
            fg="white"
        )
        etiqueta.place(x=420, y=140 + i * 30, width=120, height=25)
        dificultades.append(etiqueta)
        # Abrir el archivo de puntajes
    try:
        archivo = open("mejores_puntajes.txt", "r")
        resultados = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        resultados = []
    # Ordenar de mayor a menor según los puntos
    resultados.sort(
        key=lambda linea: int(linea.strip().split(",")[1]),
        reverse=True
    )
    # Mostrar los resultados guardados
    for i in range(len(resultados)):
        if i < 10:
            datos = resultados[i].strip().split(",")

            if len(datos) == 3:
                nombres[i].config(text=datos[0])
                puntos[i].config(text=datos[1])
                dificultades[i].config(text=datos[2])
    aviso = tk.Label(
        window,
        text="Cierra esta ventana para volver al menú principal",
        font=("Arial", 11, "bold"),
        bg="#292A2B",
        fg="white"
    )
    aviso.place(x=50, y=455, width=500, height=25)