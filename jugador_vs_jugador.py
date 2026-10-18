from py_compile import main
import tkinter as tk 
from PIL import Image, ImageTk 
import mejores_puntajes
import sonidos
import sonidos_2
import musica
import colores
import personalizacion_datos
#________________________________________________________________________________________________________________________________________________________________________________
def abrir_jugador_vs_jugador():  
    window = tk.Toplevel()
    window.title("Jugador VS Jugador")
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
#____________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Nombre del jugador 1
    label_nombre_1 = tk.Label(
        window,
        text="Añada su nombre player 1:",
        font=("Segoe UI Black", 15, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_1.place(x=170, y=50)

    nombre_1 = tk.Entry(
        window,
        font=("Arial", 14)
    )
    nombre_1.place(x=180, y=100, width=240, height=35)

    # Nombre del jugador 2
    label_nombre_2 = tk.Label(
        window,
        text="Añada su nombre player 2",
        font=("Segoe UI Black", 15, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_2.place(x=170, y=150)

    nombre_2 = tk.Entry(
        window,
        font=("Arial", 14)
    )
    nombre_2.place(x=180, y=200, width=240, height=35)
#____________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Dificultad botones
    label_dificultad = tk.Label(
        window,
        text="Seleccione la dificultad",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_dificultad.place(x=160, y=250)
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Con esto destruimos la ventana de selección y abrimos el juego para que se vea mas ordenado y no llenemos todo de ventanas abiertas
    def seleccionar_facil(window, nombre_1, nombre_2):
        jugador_1 = nombre_1.get()
        jugador_2 = nombre_2.get()
        window.destroy()
        abrir_juego_facil(jugador_1, jugador_2)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________    
    def seleccionar_medio(window, nombre_1, nombre_2):
        jugador_1 = nombre_1.get()
        jugador_2 = nombre_2.get()
        window.destroy()
        abrir_juego_medio(jugador_1, jugador_2)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
    def seleccionar_dificil(window, nombre_1, nombre_2):
        jugador_1 = nombre_1.get()
        jugador_2 = nombre_2.get()
        window.destroy()
        abrir_juego_dificil(jugador_1, jugador_2)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# botones de dificultad para seleccionar el nivel de dificultad del juego, y se pasa el nombre del jugador a la función que abre el juego
    boton_facil = tk.Button(
        window,
        text="Fácil",
        command=lambda: (sonidos.reproducir_sonido(), seleccionar_facil(window, nombre_1, nombre_2)),
        font=("Impact", 16, "bold"),
        bg="#4B7496",
        fg="white"
    )
    boton_facil.place(x=180, y=300, width=240, height=50)

    boton_medio = tk.Button(
        window,
        text="Medio",
        command=lambda: (sonidos.reproducir_sonido(), seleccionar_medio(window, nombre_1, nombre_2)),
        font=("Impact", 16, "bold"),
        bg="#4B7496",
        fg="white"
    )
    boton_medio.place(x=180, y=350, width=240, height=50)

    boton_dificil = tk.Button(
        window,
        text="Difícil",
        command=lambda: (sonidos.reproducir_sonido(), seleccionar_dificil(window, nombre_1, nombre_2)),
        font=("Impact", 16, "bold"),
        bg="#4B7496",
        fg="white"
    )
    boton_dificil.place(x=180, y=400, width=240, height=50)
#_______________________________________________________________________________________________________________________________________________________
def abrir_juego_facil(nombre_jugador_1, nombre_jugador_2):
    juego = tk.Toplevel()
    juego.title("Ping Pong modo fácil")
    juego.geometry("1100x800")
    def cerrar_juego():
        musica.detener_musica()
        juego.destroy()
    juego.protocol("WM_DELETE_WINDOW", cerrar_juego)
    musica.cambiar_tema(
        personalizacion_datos.cancion_seleccionada
    )
    musica.reproducir_musica()
    # Fondo
    imagen = Image.open(personalizacion_datos.fondo_seleccionado)
    imagen = imagen.resize((1100, 800))
    fondo = ImageTk.PhotoImage(imagen, master=juego)
    canvas = tk.Canvas(
        juego,
        width=1100,
        height=800
    )
    canvas.pack()
    canvas.create_image(
        0,
        0,
        image=fondo,
        anchor="nw"
    )
    canvas.fondo = fondo # guardamos la imagen
#______________________________________________________________________________________________________________________________________________________#
    label_nombre_1 = tk.Label(
        juego,
        text=nombre_jugador_1,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_1.place(x=850, y=20)

    label_nombre_2 = tk.Label(
        juego,
        text=nombre_jugador_2,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_2.place(x=150, y=20)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
#etiquetas del juego relevantes para mostrar el puntaje del jugador y de la IA, y el tiempo restante
    puntos_jugador_1 = [0]
    puntos_jugador_2 = [0]
    
    label_puntos_1 = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_1.place(x=850, y=60)

    label_puntos_2 = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_2.place(x=150, y=60)

    label_tiempo = tk.Label(
        juego,
        text="Tiempo: 60",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_tiempo.place(x=500, y=20)
    
    label_ganador = tk.Label(
        juego,
        text="",
        font=("Segoe UI Black", 24, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_ganador.place(x=400, y=700)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# sistema de conteo de tiempo, y guardado de puntaje version definitiva.
    tiempo = [120]
    juego_activo = [True] 
    def finalizar_partida():
        if not juego_activo[0]:
            return

        juego_activo[0] = False

        aviso = tk.Label(
            juego,
            text="Cierra esta ventana para volver al menú",
            font=("Arial", 14, "bold"),
            bg="#292A2B",
            fg="white"
        )
        aviso.place(x=350, y=750, width=400, height=35)

        if puntos_jugador_1[0] > puntos_jugador_2[0]:
            label_ganador.config(
                text=nombre_jugador_1 + " ¡Ganaste!"
            )
            mejores_puntajes.guardar_puntaje(
                nombre_jugador_1,
                puntos_jugador_1[0],
                "PVP Fácil"
            )
            sonidos_2.reproducir_victoria()
        elif puntos_jugador_2[0] > puntos_jugador_1[0]:
            label_ganador.config(
                text=nombre_jugador_2 + " ¡Ganaste!"
            )
            mejores_puntajes.guardar_puntaje(
                nombre_jugador_2,
                puntos_jugador_2[0],
                "PVP Fácil"
            )
            sonidos_2.reproducir_victoria()
        else:
            label_ganador.config(text="¡Empate!")

    def contar_tiempo():
        if not juego_activo[0]:
            return

        tiempo[0] -= 1
        label_tiempo.config(
            text="Tiempo: " + str(tiempo[0])
        )

        if tiempo[0] <= 0:
            finalizar_partida()
        else:
            juego.after(1000, contar_tiempo)
#____________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Dibujamos las metas donde se anotan los puntos son lineas negras al final de la ventana
    canvas.create_line(
        5, 0, 5, 800,
        fill="black",
        width=4
    ) # marca la meta izquierda donde anota el jugador

    canvas.create_line(
        1095, 0, 1095, 800,
        fill="black",
        width=4
    ) # marca la meta derecha donde anota la IA    
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos la pelota como un círculo
    esfera = canvas.create_oval(
        535, 385, 565, 415,
        fill= colores.color_pelota
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos la paleta del jugador 1
    paleta_jugador = canvas.create_rectangle(
        940, 340, 960, 460,
        fill=colores.color_jugador_1
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# insertamos la paleta del player 2 
    paleta_jugador_2 = canvas.create_rectangle(
        140, 340, 160, 460,
        fill=colores.color_jugador_2
    )
#______________________________________________________________________________________________________________________________________________________________________________________________
    # Movimiento de ambos jugadores
    movimiento_1 = [0]
    movimiento_2 = [0]
    def mover_paletas():
        if not juego_activo[0]:
            return
        # Jugador 1: paleta derecha, W y S
        posicion_1 = canvas.coords(paleta_jugador)
        if movimiento_1[0] == -1 and posicion_1[1] >= 0:
            canvas.move(paleta_jugador, 0, -10)
        elif movimiento_1[0] == 1 and posicion_1[3] <= 800:
            canvas.move(paleta_jugador, 0, 10)
        # Jugador 2: paleta izquierda, flechas
        posicion_2 = canvas.coords(paleta_jugador_2)
        if movimiento_2[0] == -1 and posicion_2[1] >= 0:
            canvas.move(paleta_jugador_2, 0, -10)
        elif movimiento_2[0] == 1 and posicion_2[3] <= 800:
            canvas.move(paleta_jugador_2, 0, 10)
        juego.after(10, mover_paletas)
    def presionar_tecla(event):
        if event.keysym.lower() == "w":
            movimiento_1[0] = -1
        elif event.keysym.lower() == "s":
            movimiento_1[0] = 1
        elif event.keysym == "Up":
            movimiento_2[0] = -1
        elif event.keysym == "Down":
            movimiento_2[0] = 1
    def soltar_tecla(event):
        if event.keysym.lower() == "w":
            if movimiento_1[0] == -1:
                movimiento_1[0] = 0
        elif event.keysym.lower() == "s":
            if movimiento_1[0] == 1:
                movimiento_1[0] = 0
        elif event.keysym == "Up":
            if movimiento_2[0] == -1:
                movimiento_2[0] = 0
        elif event.keysym == "Down":
            if movimiento_2[0] == 1:
                movimiento_2[0] = 0
    juego.bind("<KeyPress>", presionar_tecla)
    juego.bind("<KeyRelease>", soltar_tecla)
    juego.focus_set()
    mover_paletas()
#______________________________________________________________________________________________________________________________________________________________________________________________________________________ 
# Sistema de colisiones para las paletas de los jugadores
    def detectar_colision(esfera, paleta_jugador, paleta_jugador_2, dx, dy):
        posicion_bola = canvas.coords(esfera)
        posicion_jugador = canvas.coords(paleta_jugador)
        posicion_jugador_2 = canvas.coords(paleta_jugador_2)
        # Calcular el radio y el centro de la pelota.
        radio = (posicion_bola[2] - posicion_bola[0]) / 2
        x = (posicion_bola[0] + posicion_bola[2]) / 2
        y = (posicion_bola[1] + posicion_bola[3]) / 2
        # Predecir la posición de la pelota en el siguiente movimiento.
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Calcular los límites verticales de la pelota en la siguiente posición.
        arriba_bola = siguiente_y - radio
        abajo_bola = siguiente_y + radio
        # Obtener los límites de la paleta del jugador 1, situada a la derecha.
        izquierda_jugador = posicion_jugador[0]
        arriba_jugador = posicion_jugador[1]
        abajo_jugador = posicion_jugador[3]
        # Comprobar si la pelota se dirige hacia la paleta derecha.
        if dx > 0:
            # Comprobar si la pelota ya toca horizontalmente la paleta.
            if x + radio >= izquierda_jugador:
                if x - radio <= posicion_jugador[2]:
                    if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                        return 1
            # Comprobar si la pelota alcanzará la paleta en el siguiente movimiento.
            elif siguiente_x + radio >= izquierda_jugador:
                if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                    return 1
        # Obtener los límites de la paleta del jugador 2, situada a la izquierda.
        derecha_jugador_2 = posicion_jugador_2[2]
        arriba_jugador_2 = posicion_jugador_2[1]
        abajo_jugador_2 = posicion_jugador_2[3]
        # Comprobar si la pelota se dirige hacia la paleta izquierda.
        if dx < 0:
            # Comprobar si la pelota ya toca horizontalmente la paleta.
            if x - radio <= derecha_jugador_2:
                if x + radio >= posicion_jugador_2[0]:
                    if abajo_bola >= arriba_jugador_2 and arriba_bola <= abajo_jugador_2:
                        return -1
            # Comprobar si la pelota alcanzará la paleta en el siguiente movimiento.
            elif siguiente_x - radio <= derecha_jugador_2:
                if abajo_bola >= arriba_jugador_2 and arriba_bola <= abajo_jugador_2:
                    return -1
        # Si no se cumplen las condiciones anteriores, no hay colisión.
        return 0
#_______________________________________________________________________________________________________________________________________________________
# Movimiento de la bola y rebotes
    def mover_bola(dx, dy):
        # Detener los movimientos si el juego ya terminó.
        if not juego_activo[0]:
            return
        # Obtener las coordenadas actuales de la pelota.
        posicion = canvas.coords(esfera)
        # Calcular el radio y el centro de la pelota.
        radio = (posicion[2] - posicion[0]) / 2
        x = (posicion[0] + posicion[2]) / 2
        y = (posicion[1] + posicion[3]) / 2
        # Calcular la siguiente posición vertical de la pelota.
        siguiente_y = y + dy
        # Rebote en el borde inferior.
        if siguiente_y + radio >= 800 and dy > 0:
            dy = -abs(dy)
        # Rebote en el borde superior.
        elif siguiente_y - radio <= 0 and dy < 0:
            dy = abs(dy)
        # Detectar si la pelota choca con alguna de las dos paletas.
        colision = detectar_colision(
            esfera,
            paleta_jugador,
            paleta_jugador_2,
            dx,
            dy
        )
        # Colisión con la paleta derecha del jugador 1.
        if colision == 1:
            sonidos_2.reproducir_rebote()
            # Obtener la posición de la paleta derecha.
            posicion_jugador = canvas.coords(paleta_jugador)
            # Colocar la pelota justo fuera del borde izquierdo de la paleta.
            x = posicion_jugador[0] - radio -1
            canvas.coords(
                esfera,
                x - radio,
                y - radio,
                x + radio,
                y + radio
            )
            # Invertir la velocidad horizontal para devolver la pelota.
            dx = -abs(dx)
        # Colisión con la paleta izquierda del jugador 2.
        elif colision == -1:
            sonidos_2.reproducir_rebote()
            # Obtener la posición de la paleta izquierda.
            posicion_jugador_2 = canvas.coords(paleta_jugador_2)
            # Colocar la pelota justo fuera del borde derecho de la paleta.
            x = posicion_jugador_2[2] + radio +1
            canvas.coords(
                esfera,
                x - radio,
                y - radio,
                x + radio,
                y + radio
            )
            # Invertir la velocidad horizontal para devolver la pelota.
            dx = abs(dx)
        # Mover la pelota utilizando las velocidades actualizadas.
        canvas.move(esfera, dx, dy)
        # Obtener las coordenadas de la pelota después del movimiento.
        posicion = canvas.coords(esfera)
        # Si la pelota sale por la izquierda, anota el jugador 1.
        if posicion[2] <= 0:
            puntos_jugador_1[0] += 1
            # Actualizar la puntuación del jugador 1.
            label_puntos_1.config(
                text="Puntos: " + str(puntos_jugador_1[0])
            )
            # Reiniciar la pelota en el centro del campo.
            canvas.coords(esfera, 535, 385, 565, 415)
            # Establecer la velocidad inicial después del punto.
            dx, dy = 7, 5
        # Si la pelota sale por la derecha, anota el jugador 2.
        elif posicion[0] >= 1100:
            puntos_jugador_2[0] += 1
            # Actualizar la puntuación del jugador 2.
            label_puntos_2.config(
                text="Puntos: " + str(puntos_jugador_2[0])
            )
            # Reiniciar la pelota en el centro del campo.
            canvas.coords(esfera, 535, 385, 565, 415)
            # Establecer la velocidad inicial hacia el lado contrario.
            dx, dy = -7, 5
        # Programar el siguiente movimiento de la pelota.
        juego.after(30, mover_bola, dx, dy)
    # Iniciar el movimiento de las paletas.
    mover_paletas()
    # Iniciar el movimiento de la pelota.
    mover_bola(7, 5)
    # Iniciar el contador de tiempo.
    contar_tiempo()
#_______________________________________________________________________________________________________________________________________________________
def abrir_juego_medio(nombre_jugador_1, nombre_jugador_2):
    juego = tk.Toplevel()
    juego.title("Ping Pong modo medio")
    juego.geometry("1100x800")
    def cerrar_juego():
        musica.detener_musica()
        juego.destroy()
    juego.protocol("WM_DELETE_WINDOW", cerrar_juego)
    musica.cambiar_tema(
        personalizacion_datos.cancion_seleccionada
    )
    musica.reproducir_musica()
    # Fondo
    imagen = Image.open(personalizacion_datos.fondo_seleccionado)
    imagen = imagen.resize((1100, 800))
    fondo = ImageTk.PhotoImage(imagen, master=juego)
    canvas = tk.Canvas(
        juego,
        width=1100,
        height=800
    )
    canvas.pack()
    canvas.create_image(
        0,
        0,
        image=fondo,
        anchor="nw"
    )
    canvas.fondo = fondo # guardamos la imagen
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
#etiquetas del juego relevantes para mostrar el puntaje del jugador y de la IA, y el tiempo restante
    label_nombre_1 = tk.Label(
        juego,
        text=nombre_jugador_1,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_1.place(x=850, y=10)

    label_nombre_2 = tk.Label(
        juego,
        text=nombre_jugador_2,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_2.place(x=150, y=20)

    puntos_jugador_1 = [0]
    puntos_jugador_2 = [0]
    
    label_puntos_1 = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_1.place(x=850, y=60)

    label_puntos_2 = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_2.place(x=150, y=60)

    label_tiempo = tk.Label(
        juego,
        text="Tiempo: 60",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_tiempo.place(x=500, y=20)
    
    label_ganador = tk.Label(
        juego,
        text="",
        font=("Segoe UI Black", 24, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_ganador.place(x=400, y=700)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# sistema de conteo de tiempo, y guardado de puntaje version definitiva.
    tiempo = [120]
    juego_activo = [True] 
    def finalizar_partida():
        if not juego_activo[0]:
            return

        juego_activo[0] = False

        aviso = tk.Label(
            juego,
            text="Cierra esta ventana para volver al menú",
            font=("Arial", 14, "bold"),
            bg="#292A2B",
            fg="white"
        )
        aviso.place(x=350, y=750, width=400, height=35)

        if puntos_jugador_1[0] > puntos_jugador_2[0]:
            label_ganador.config(
                text=nombre_jugador_1 + " ¡Ganaste!"
            )
            mejores_puntajes.guardar_puntaje(
                nombre_jugador_1,
                puntos_jugador_1[0],
                "PVP Fácil"
            )
            sonidos_2.reproducir_victoria()
        elif puntos_jugador_2[0] > puntos_jugador_1[0]:
            label_ganador.config(
                text=nombre_jugador_2 + " ¡Ganaste!"
            )
            mejores_puntajes.guardar_puntaje(
                nombre_jugador_2,
                puntos_jugador_2[0],
                "PVP Medio"
            )
            sonidos_2.reproducir_victoria()
        else:
            label_ganador.config(text="¡Empate!")

    def contar_tiempo():
        if not juego_activo[0]:
            return

        tiempo[0] -= 1
        label_tiempo.config(
            text="Tiempo: " + str(tiempo[0])
        )

        if tiempo[0] <= 0:
            finalizar_partida()
        else:
            juego.after(1000, contar_tiempo)

#____________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Dibujamos las metas donde se anotan los puntos son lineas negras al final de la ventana
    canvas.create_line(
        5, 0, 5, 800,
        fill="black",
        width=4
    ) # marca la meta izquierda donde anota el jugador

    canvas.create_line(
        1095, 0, 1095, 800,
        fill="black",
        width=4
    ) # marca la meta derecha donde anota la IA    
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos la pelota como un círculo
    esfera = canvas.create_oval(
        535, 385, 565, 415,
        fill= colores.color_pelota
    )
# Dibujamos la pelota 2 como un círculo
    esfera2 = canvas.create_oval(
        535, 385, 565, 415,
        fill= colores.color_pelota
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos la paleta del jugador 1
    paleta_jugador = canvas.create_rectangle(
        940, 340, 960, 460,
        fill=colores.color_jugador_1
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# insertamos la paleta del player 2 
    paleta_jugador_2 = canvas.create_rectangle(
        140, 340, 160, 460,
        fill=colores.color_jugador_2
    )
#______________________________________________________________________________________________________________________________________________________________________________________________
    # Movimiento de ambos jugadores
    movimiento_1 = [0]
    movimiento_2 = [0]
    def mover_paletas():
        if not juego_activo[0]:
            return
        # Jugador 1: paleta derecha, W y S
        posicion_1 = canvas.coords(paleta_jugador)
        if movimiento_1[0] == -1 and posicion_1[1] >= 0:
            canvas.move(paleta_jugador, 0, -10)
        elif movimiento_1[0] == 1 and posicion_1[3] <= 800:
            canvas.move(paleta_jugador, 0, 10)
        # Jugador 2: paleta izquierda, flechas
        posicion_2 = canvas.coords(paleta_jugador_2)
        if movimiento_2[0] == -1 and posicion_2[1] >= 0:
            canvas.move(paleta_jugador_2, 0, -10)
        elif movimiento_2[0] == 1 and posicion_2[3] <= 800:
            canvas.move(paleta_jugador_2, 0, 10)
        juego.after(10, mover_paletas)
    def presionar_tecla(event):
        if event.keysym.lower() == "w":
            movimiento_1[0] = -1
        elif event.keysym.lower() == "s":
            movimiento_1[0] = 1
        elif event.keysym == "Up":
            movimiento_2[0] = -1
        elif event.keysym == "Down":
            movimiento_2[0] = 1
    def soltar_tecla(event):
        if event.keysym.lower() == "w":
            if movimiento_1[0] == -1:
                movimiento_1[0] = 0
        elif event.keysym.lower() == "s":
            if movimiento_1[0] == 1:
                movimiento_1[0] = 0
        elif event.keysym == "Up":
            if movimiento_2[0] == -1:
                movimiento_2[0] = 0
        elif event.keysym == "Down":
            if movimiento_2[0] == 1:
                movimiento_2[0] = 0
    juego.bind("<KeyPress>", presionar_tecla)
    juego.bind("<KeyRelease>", soltar_tecla)
    juego.focus_set()
    mover_paletas()
#______________________________________________________________________________________________________________________________________________________________________________________________________________________ 
    # Sistema de colisiones para las paletas y las bolas
    def detectar_colision(
        esfera,
        paleta_jugador,
        paleta_jugador_2,
        dx,
        dy
    ):
        # Obtener las coordenadas de la pelota y de las dos paletas.
        posicion_bola = canvas.coords(esfera)
        posicion_jugador = canvas.coords(paleta_jugador)
        posicion_jugador_2 = canvas.coords(paleta_jugador_2)
        # Calcular el radio y el centro de la pelota.
        radio = (posicion_bola[2] - posicion_bola[0]) / 2
        x = (posicion_bola[0] + posicion_bola[2]) / 2
        y = (posicion_bola[1] + posicion_bola[3]) / 2
        # Calcular la posición prevista de la pelota en el siguiente movimiento.
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Calcular los límites verticales previstos de la pelota.
        arriba_bola = siguiente_y - radio
        abajo_bola = siguiente_y + radio
        # Paleta del jugador 1, situada a la derecha.
        izquierda_jugador = posicion_jugador[0]
        arriba_jugador = posicion_jugador[1]
        abajo_jugador = posicion_jugador[3]
        # Comprobar que la pelota se mueve hacia la derecha.
        if dx > 0:
            # Comprobar si la pelota ya está tocando horizontalmente la paleta.
            if x + radio >= izquierda_jugador:
                if x - radio <= posicion_jugador[2]:
                    if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                        return 1
            # Comprobar si la pelota alcanzará la paleta en el siguiente movimiento.
            elif siguiente_x + radio >= izquierda_jugador:
                if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                    return 1
        # Paleta del jugador 2, situada a la izquierda.
        derecha_jugador_2 = posicion_jugador_2[2]
        arriba_jugador_2 = posicion_jugador_2[1]
        abajo_jugador_2 = posicion_jugador_2[3]
        # Comprobar que la pelota se mueve hacia la izquierda.
        if dx < 0:
            # Comprobar si la pelota ya está tocando horizontalmente la paleta.
            if x - radio <= derecha_jugador_2:
                if x + radio >= posicion_jugador_2[0]:
                    if abajo_bola >= arriba_jugador_2 and arriba_bola <= abajo_jugador_2:
                        return -1
            # Comprobar si la pelota alcanzará la paleta en el siguiente movimiento.
            elif siguiente_x - radio <= derecha_jugador_2:
                if abajo_bola >= arriba_jugador_2 and arriba_bola <= abajo_jugador_2:
                    return -1
        # Si no se cumplen las condiciones anteriores, no hay colisión.
        return 0
#_______________________________________________________________________________________________________________________________________________________
# Movimiento de la bola y rebotes
    def mover_bola(esfera, dx, dy, inicio_x, inicio_y):
        # No continuar moviendo las pelotas cuando el juego termina.
        if not juego_activo[0]:
            return
        # Obtener las coordenadas actuales de esta pelota.
        posicion = canvas.coords(esfera)
        # Calcular el radio y el centro de la pelota.
        radio = (posicion[2] - posicion[0]) / 2
        x = (posicion[0] + posicion[2]) / 2
        y = (posicion[1] + posicion[3]) / 2
        # Calcular la posición prevista para comprobar los bordes.
        siguiente_y = y + dy
        # Rebote en el borde inferior.
        if siguiente_y + radio >= 800 and dy > 0:
            dy = -abs(dy)
        # Rebote en el borde superior.
        elif siguiente_y - radio <= 0 and dy < 0:
            dy = abs(dy)
        # Revisar la colisión de esta pelota con cualquiera de las dos paletas.
        colision = detectar_colision(
            esfera,
            paleta_jugador,
            paleta_jugador_2,
            dx,
            dy
        )
        # Colisión con la paleta derecha del jugador 1.
        if colision == 1:
            sonidos_2.reproducir_rebote()
            # Obtener la posición de la paleta derecha.
            posicion_jugador = canvas.coords(paleta_jugador)
            # Colocar la pelota justo fuera del borde izquierdo de la paleta.
            x = posicion_jugador[0] - radio -1
            canvas.coords(
                esfera,
                x - radio, y - radio,
                x + radio, y + radio
            )
            # Cambiar la dirección horizontal para que rebote hacia la izquierda.
            dx = -abs(dx)
        # Colisión con la paleta izquierda del jugador 2.
        elif colision == -1:
            sonidos_2.reproducir_rebote()
            # Obtener la posición de la paleta izquierda.
            posicion_jugador_2 = canvas.coords(paleta_jugador_2)
            # Colocar la pelota justo fuera del borde derecho de la paleta.
            x = posicion_jugador_2[2] + radio +1
            canvas.coords(
                esfera,
                x - radio, y - radio,
                x + radio, y + radio
            )
            # Cambiar la dirección horizontal para que rebote hacia la derecha.
            dx = abs(dx)
        # Mover únicamente la pelota que recibe esta función.
        canvas.move(esfera, dx, dy)
        # Obtener sus coordenadas después del movimiento.
        posicion = canvas.coords(esfera)
        # Si la pelota sale por la izquierda, anota el jugador 1.
        if posicion[2] <= 0:
            puntos_jugador_1[0] += 1
            # Actualizar la puntuación del jugador 1.
            label_puntos_1.config(
                text="Puntos: " + str(puntos_jugador_1[0])
            )
            # Reiniciar esta pelota en sus propias coordenadas iniciales.
            canvas.coords(
                esfera,
                inicio_x - radio, inicio_y - radio,
                inicio_x + radio, inicio_y + radio
            )
            # Establecer la dirección inicial después del punto.
            dx, dy = 7, 5
        # Si la pelota sale por la derecha, anota el jugador 2.
        elif posicion[0] >= 1100:
            puntos_jugador_2[0] += 1
            # Actualizar la puntuación del jugador 2.
            label_puntos_2.config(
                text="Puntos: " + str(puntos_jugador_2[0])
            )
            # Reiniciar esta pelota en sus propias coordenadas iniciales.
            canvas.coords(
                esfera,
                inicio_x - radio, inicio_y - radio,
                inicio_x + radio, inicio_y + radio
            )
            # Establecer la dirección inicial hacia el lado contrario.
            dx, dy = -7, 5
        # Programar el siguiente movimiento de esta misma pelota,
        # conservando su identidad, velocidad y posición inicial.
        juego.after(
            30,
            mover_bola,
            esfera,
            dx,
            dy,
            inicio_x,
            inicio_y
        )
    # Iniciar el movimiento de las paletas.
    mover_paletas()
    # Iniciar la primera pelota en el centro del campo.
    mover_bola(esfera, 7, 5, 550, 400)
    # Iniciar la segunda pelota en una posición diferente.
    mover_bola(esfera2, -8, 6, 550, 300)
    # Iniciar el contador de tiempo.
    contar_tiempo()
#_______________________________________________________________________________________________________________________________________________________
def abrir_juego_dificil(nombre_jugador_1, nombre_jugador_2):
    juego = tk.Toplevel()
    juego.title("Ping Pong modo dificil")
    juego.geometry("1100x800")
    def cerrar_juego():
        musica.detener_musica()
        juego.destroy()
    juego.protocol("WM_DELETE_WINDOW", cerrar_juego)
    musica.cambiar_tema(
        personalizacion_datos.cancion_seleccionada
    )
    musica.reproducir_musica()
    # Fondo
    imagen = Image.open(personalizacion_datos.fondo_seleccionado)
    imagen = imagen.resize((1100, 800))
    fondo = ImageTk.PhotoImage(imagen, master=juego)
    canvas = tk.Canvas(
        juego,
        width=1100,
        height=800
    )
    canvas.pack()
    canvas.create_image(
        0,
        0,
        image=fondo,
        anchor="nw"
    )
    canvas.fondo = fondo # guardamos la imagen
#_____________________________________________________________________________________________________________________________________________#
# Obstáculo móvil del modo difícil
    obstaculo = canvas.create_rectangle(
        540, 330, 560, 470,
        fill="lightblue",
        outline="lightblue",
        width=2
    )
    def mover_obstaculo(dy):
        if not juego_activo[0]:
            return

        posicion = canvas.coords(obstaculo)

        if posicion[1] + dy <= 0:
            dy = abs(dy)
        elif posicion[3] + dy >= 800:
            dy = -abs(dy)

        canvas.move(obstaculo, 0, dy)

        juego.after(30, mover_obstaculo, dy)
        
    label_nombre_1 = tk.Label(
        juego,
        text=nombre_jugador_1,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_1.place(x=850, y=10)

    label_nombre_2 = tk.Label(
        juego,
        text=nombre_jugador_2,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre_2.place(x=150, y=20)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
#etiquetas del juego relevantes para mostrar el puntaje del jugador y de la IA, y el tiempo restante
    puntos_jugador_1 = [0]
    puntos_jugador_2 = [0]
    
    label_puntos_1 = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_1.place(x=850, y=60)

    label_puntos_2 = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_2.place(x=150, y=60)

    label_tiempo = tk.Label(
        juego,
        text="Tiempo: 60",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_tiempo.place(x=500, y=20)
    
    label_ganador = tk.Label(
        juego,
        text="",
        font=("Segoe UI Black", 24, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_ganador.place(x=400, y=700)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# sistema de conteo de tiempo, y guardado de puntaje version definitiva.
    tiempo = [120]
    juego_activo = [True] 
    def finalizar_partida():
        if not juego_activo[0]:
            return
        juego_activo[0] = False
        aviso = tk.Label(
            juego,
            text="Cierra esta ventana para volver al menú",
            font=("Arial", 14, "bold"),
            bg="#292A2B",
            fg="white"
        )
        aviso.place(x=350, y=750, width=400, height=35)
        if puntos_jugador_1[0] > puntos_jugador_2[0]:
            label_ganador.config(
                text=nombre_jugador_1 + " ¡Ganaste!"
            )
            mejores_puntajes.guardar_puntaje(
                nombre_jugador_1,
                puntos_jugador_1[0],
                "PVP Dificil"
            )
            sonidos_2.reproducir_victoria()
        elif puntos_jugador_2[0] > puntos_jugador_1[0]:
            label_ganador.config(
                text=nombre_jugador_2 + " ¡Ganaste!"
            )
            mejores_puntajes.guardar_puntaje(
                nombre_jugador_2,
                puntos_jugador_2[0],
                "PVP Dificil"
            )
            sonidos_2.reproducir_victoria()
        else:
            label_ganador.config(text="¡Empate!")
    def contar_tiempo():
        if not juego_activo[0]:
            return
        tiempo[0] -= 1
        label_tiempo.config(
            text="Tiempo: " + str(tiempo[0])
        )
        if tiempo[0] <= 0:
            finalizar_partida()
        else:
            juego.after(1000, contar_tiempo)
#____________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos las metas donde se anotan los puntos son lineas negras al final de la ventana
    canvas.create_line(
        5, 0, 5, 800,
        fill="black",
        width=4
    ) # marca la meta izquierda donde anota el jugador

    canvas.create_line(
        1095, 0, 1095, 800,
        fill="black",
        width=4
    ) # marca la meta derecha donde anota la IA    
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos la pelota como un círculo
    esfera = canvas.create_oval(
        535, 385, 565, 415,
        fill= colores.color_pelota
    )
# Dibujamos la pelota 2 como un círculo
    esfera2 = canvas.create_oval(
        535, 385, 565, 415,
        fill= colores.color_pelota
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Dibujamos la paleta del jugador 1
    paleta_jugador = canvas.create_rectangle(
        940, 340, 960, 460,
        fill=colores.color_jugador_1
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# insertamos la paleta del player 2 
    paleta_jugador_2 = canvas.create_rectangle(
        140, 340, 160, 460,
        fill = colores.color_jugador_2
    )
#______________________________________________________________________________________________________________________________________________________________________________________________
    # Movimiento de ambos jugadores
    movimiento_1 = [0]
    movimiento_2 = [0]
    def mover_paletas():
        if not juego_activo[0]:
            return
        # Jugador 1: paleta derecha, W y S
        posicion_1 = canvas.coords(paleta_jugador)
        if movimiento_1[0] == -1 and posicion_1[1] >= 0:
            canvas.move(paleta_jugador, 0, -10)
        elif movimiento_1[0] == 1 and posicion_1[3] <= 800:
            canvas.move(paleta_jugador, 0, 10)
        # Jugador 2: paleta izquierda, flechas
        posicion_2 = canvas.coords(paleta_jugador_2)
        if movimiento_2[0] == -1 and posicion_2[1] >= 0:
            canvas.move(paleta_jugador_2, 0, -10)
        elif movimiento_2[0] == 1 and posicion_2[3] <= 800:
            canvas.move(paleta_jugador_2, 0, 10)
        juego.after(10, mover_paletas)
    def presionar_tecla(event):
        if event.keysym.lower() == "w":
            movimiento_1[0] = -1
        elif event.keysym.lower() == "s":
            movimiento_1[0] = 1
        elif event.keysym == "Up":
            movimiento_2[0] = -1
        elif event.keysym == "Down":
            movimiento_2[0] = 1
    def soltar_tecla(event):
        if event.keysym.lower() == "w":
            if movimiento_1[0] == -1:
                movimiento_1[0] = 0
        elif event.keysym.lower() == "s":
            if movimiento_1[0] == 1:
                movimiento_1[0] = 0
        elif event.keysym == "Up":
            if movimiento_2[0] == -1:
                movimiento_2[0] = 0
        elif event.keysym == "Down":
            if movimiento_2[0] == 1:
                movimiento_2[0] = 0
    juego.bind("<KeyPress>", presionar_tecla)
    juego.bind("<KeyRelease>", soltar_tecla)
    juego.focus_set()
    mover_paletas()
#______________________________________________________________________________________________________________________________________________________________________________________________________________________ 
# Sistema de colisiones para las paletas y las bolas
    def detectar_colision(
        esfera,
        paleta_jugador,
        paleta_jugador_2,
        dx,
        dy
    ):
        posicion_bola = canvas.coords(esfera)
        posicion_jugador = canvas.coords(paleta_jugador)
        posicion_jugador_2 = canvas.coords(paleta_jugador_2)
        radio = (posicion_bola[2] - posicion_bola[0]) / 2
        # Calcular el centro actual de la pelota.
        x = (posicion_bola[0] + posicion_bola[2]) / 2
        y = (posicion_bola[1] + posicion_bola[3]) / 2
        # Predecir la posición de la pelota en el siguiente movimiento.
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Calcular los límites verticales de la pelota en la siguiente posición.
        arriba_bola = siguiente_y - radio
        abajo_bola = siguiente_y + radio
        # Paleta del jugador 1, situada a la derecha.
        izquierda_jugador = posicion_jugador[0]
        derecha_jugador = posicion_jugador[2]
        arriba_jugador = posicion_jugador[1]
        abajo_jugador = posicion_jugador[3]
        # Comprobar la colisión con la paleta derecha.
        if dx > 0:
            if x + radio >= izquierda_jugador:
                if x - radio <= derecha_jugador:
                    if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                        return 1
            elif siguiente_x + radio >= izquierda_jugador:
                if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                    return 1
        # Paleta del jugador 2, situada a la izquierda.
        izquierda_jugador_2 = posicion_jugador_2[0]
        derecha_jugador_2 = posicion_jugador_2[2]
        arriba_jugador_2 = posicion_jugador_2[1]
        abajo_jugador_2 = posicion_jugador_2[3]
        # Comprobar la colisión con la paleta izquierda.
        if dx < 0:
            if x - radio <= derecha_jugador_2:
                if x + radio >= izquierda_jugador_2:
                    if abajo_bola >= arriba_jugador_2 and arriba_bola <= abajo_jugador_2:
                        return -1
            elif siguiente_x - radio <= derecha_jugador_2:
                if abajo_bola >= arriba_jugador_2 and arriba_bola <= abajo_jugador_2:
                    return -1
        # Si no se detecta ninguna colisión, devolver 0.
        return 0
#_______________________________________________________________________________________________________________________________________________________
# Movimiento de la bola y rebotes
    def mover_bola(esfera, dx, dy, inicio_x, inicio_y):
        # Detener el movimiento cuando termina la partida.
        if not juego_activo[0]:
            return
        # Obtener las coordenadas actuales de esta pelota.
        posicion = canvas.coords(esfera)
        # Calcular el radio y el centro de la pelota.
        radio = (posicion[2] - posicion[0]) / 2
        x = (posicion[0] + posicion[2]) / 2
        y = (posicion[1] + posicion[3]) / 2
        # Calcular la posición prevista para el siguiente movimiento.
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Rebote contra el borde inferior.
        if siguiente_y + radio >= 800 and dy > 0:
            dy = -abs(dy)
        # Rebote contra el borde superior.
        elif siguiente_y - radio <= 0 and dy < 0:
            dy = abs(dy)
        # Obtener las coordenadas del obstáculo central.
        pared = canvas.coords(obstaculo)
        # Comprobar que el obstáculo tenga coordenadas válidas.
        if len(pared) == 4:
            # Comprobar si la pelota coincide verticalmente con el obstáculo.
            if siguiente_y + radio >= pared[1] and siguiente_y - radio <= pared[3]:
                # Colisión cuando la pelota viene desde la izquierda.
                if dx > 0 and x + radio <= pared[0] and siguiente_x + radio >= pared[0]:
                    dx = -abs(dx)
                    # Colocar la pelota fuera del lado izquierdo del obstáculo.
                    canvas.coords(
                        esfera,
                        pared[2],
                        y - radio,
                        pared[2] + 2 * radio,
                        y + radio
                    )
                # Colisión cuando la pelota viene desde la derecha.
                elif dx < 0 and x - radio >= pared[2] and siguiente_x - radio <= pared[2]:
                    dx = abs(dx)
                    # Colocar la pelota fuera del lado derecho del obstáculo.
                    canvas.coords(
                        esfera,
                        pared[2],
                        y - radio,
                        pared[2] + 2 * radio,
                        y + radio
                    )
        # Comprobar la colisión con las paletas.
        colision = detectar_colision(
            esfera,
            paleta_jugador,
            paleta_jugador_2,
            dx,
            dy
        )
        # Actualizar el centro después de cualquier posible reposicionamiento.
        posicion = canvas.coords(esfera)
        x = (posicion[0] + posicion[2]) / 2
        y = (posicion[1] + posicion[3]) / 2
        # Colisión con la paleta derecha.
        if colision == 1:
            sonidos_2.reproducir_rebote()
            # Obtener la posición de la paleta derecha.
            posicion_jugador = canvas.coords(paleta_jugador)
            # Colocar la pelota justo fuera de la paleta.
            x = posicion_jugador[0] - radio -1
            canvas.coords(
                esfera,
                x - radio, y - radio,
                x + radio, y + radio
            )
            # Cambiar la dirección horizontal hacia la izquierda.
            dx = -abs(dx)
        # Colisión con la paleta izquierda.
        elif colision == -1:
            sonidos_2.reproducir_rebote()
            # Obtener la posición de la paleta izquierda.
            posicion_jugador_2 = canvas.coords(paleta_jugador_2)
            # Colocar la pelota justo fuera de la paleta.
            x = posicion_jugador_2[2] + radio +1
            canvas.coords(
                esfera,
                x - radio, y - radio,
                x + radio, y + radio
            )
            # Cambiar la dirección horizontal hacia la derecha.
            dx = abs(dx)
        # Mover la pelota con las velocidades actualizadas.
        canvas.move(esfera, dx, dy)
        # Obtener las coordenadas después del movimiento.
        posicion = canvas.coords(esfera)
        # Punto para el jugador de la derecha si la pelota sale por la izquierda.
        if posicion[2] <= 0:
            puntos_jugador_1[0] += 1
            label_puntos_1.config(
                text="Puntos: " + str(puntos_jugador_1[0])
            )
            # Reiniciar esta pelota en su posición inicial.
            canvas.coords(
                esfera,
                inicio_x - radio, inicio_y - radio,
                inicio_x + radio, inicio_y + radio
            )
            # Preparar el siguiente lanzamiento hacia la derecha.
            dx = abs(dx)
            dy = abs(dy)
        # Punto para el jugador de la izquierda si la pelota sale por la derecha.
        elif posicion[0] >= 1100:
            puntos_jugador_2[0] += 1
            label_puntos_2.config(
                text="Puntos: " + str(puntos_jugador_2[0])
            )
            # Reiniciar esta pelota en su posición inicial.
            canvas.coords(
                esfera,
                inicio_x - radio, inicio_y - radio,
                inicio_x + radio, inicio_y + radio
            )
            # Preparar el siguiente lanzamiento hacia la izquierda.
            dx = -abs(dx)
            dy = abs(dy)
        # Programar el siguiente movimiento de esta pelota.
        juego.after(
            30,
            mover_bola,
            esfera,
            dx,
            dy,
            inicio_x,
            inicio_y
        )
    # Iniciar la primera pelota.
    mover_bola(esfera, 12, 12, 550, 400)
    # Iniciar la segunda pelota.
    mover_bola(esfera2, -10, 10, 550, 300)
    # Iniciar el movimiento del obstáculo.
    mover_obstaculo(5)
    # Iniciar el contador de tiempo.
    contar_tiempo()