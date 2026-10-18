from py_compile import main
import tkinter as tk 
from PIL import Image, ImageTk 
import mejores_puntajes
import sonidos
import sonidos_2
import musica
import colores
import personalizacion_datos
#___________________________________________________________________________________________________________________________________________________________________________________________________________________
def abrir_jugador_vs_ia():  
    window = tk.Toplevel()
    window.title("Jugador VS IA")
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
    label_nombre = tk.Label(
        window,
        text="Añada su nombre player",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_nombre.place(x=150, y=60)
    nombre = tk.Entry(
        window,
        font=("Arial", 16)
    )
    nombre.place(x=180, y=105, width=240, height=40)
#____________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Dificultad botones
    label_dificultad = tk.Label(
        window,
        text="Seleccione la dificultad",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_dificultad.place(x=160, y=165)
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Con esto destruimos la ventana de selección y abrimos el juego para que se vea mas ordenado y no llenemos todo de ventanas abiertas
    def seleccionar_facil(window, nombre):
        nombre_jugador = nombre.get()
        window.destroy()
        abrir_juego_facil(nombre_jugador)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________    
    def seleccionar_medio(window, nombre):
        nombre_jugador = nombre.get()
        window.destroy()
        abrir_juego_medio(nombre_jugador)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
    def seleccionar_dificil(window, nombre):
        nombre_jugador = nombre.get()
        window.destroy()
        abrir_juego_dificil(nombre_jugador)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# botones de dificultad para seleccionar el nivel de dificultad del juego, y se pasa el nombre del jugador a la función que abre el juego
    boton_facil = tk.Button(
        window,
        text="Fácil",
        command=lambda: (sonidos.reproducir_sonido(), seleccionar_facil(window, nombre)),
        font=("Impact", 16, "bold"),
        bg="#4B7496",
        fg="white"
    )
    boton_facil.place(x=180, y=215, width=240, height=50)

    boton_medio = tk.Button(
        window,
        text="Medio",
        command=lambda: (sonidos.reproducir_sonido(), seleccionar_medio(window, nombre)),
        font=("Impact", 16, "bold"),
        bg="#4B7496",
        fg="white"
    )
    boton_medio.place(x=180, y=285, width=240, height=50)

    boton_dificil = tk.Button(
        window,
        text="Difícil",
        command=lambda: (sonidos.reproducir_sonido(), seleccionar_dificil(window, nombre)),
        font=("Impact", 16, "bold"),
        bg="#4B7496",
        fg="white"
    )
    boton_dificil.place(x=180, y=355, width=240, height=50)
#____________________________________________________________________________________________________________________________________________________________________________________________________________________ 
def abrir_juego_facil(nombre_jugador):
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
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# etiquetas del juego relevantes para mostrar el puntaje del jugador y de la IA, y el tiempo restante 
    label_puntos = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos.place(x=850, y=60)

    label_nombre = tk.Label(
        juego,
        text=nombre_jugador,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )

    label_nombre.place(x=850, y=20)
    puntos_jugador = [0]
    puntos_ia = [0]
    
    label_puntos_ia = tk.Label(
        juego,
        text="IA: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_ia.place(x=150, y=60)

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
    def contar_tiempo():
        if tiempo[0] > 0:
            tiempo[0] -= 1  # descontamos el tiempo en 1 segundo
            label_tiempo.config(
                text="Tiempo: " + str(tiempo[0]) # mala práctica diría Jeff pero se ve bonito en la ventana
            )
            juego.after(1000, contar_tiempo) # llamamos a la función contar_tiempo cada 1000 milisegundos (1 segundo) para que se actualice el tiempo restante
        else:
            juego_activo[0] = False # cuando el tiempo llegue a 0, se detiene el juego y se muestra el puntaje final del jugador y de la IA, y se guarda el puntaje del jugador en el archivo de mejores puntajes
            aviso = tk.Label(
                juego,
                text="Cierra esta ventana para volver al menú",
                font=("Arial", 14, "bold"),
                bg="#292A2B",
                fg="white"
            )
            aviso.place(x=350, y=750, width=400, height=35)

            mejores_puntajes.guardar_puntaje(
                nombre_jugador,
                puntos_jugador[0], # siempre que el jugador tenga mas puntos que la IA se guardaran los datos en el txt de mejores puntajes
                "Fácil"
            )
            if puntos_jugador[0] > puntos_ia[0]: 
                label_ganador.config(
                    text=nombre_jugador + " " + "¡Ganaste!"
                )
                sonidos_2.reproducir_victoria()
            elif puntos_ia[0] > puntos_jugador[0]:
                label_ganador.config(
                    text="¡La IA ganó!"
                )
                sonidos_2.reproducir_victoria()
            else:
                label_ganador.config(text="¡Empate!")
    contar_tiempo()
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
#________________________________________________________________________________________________________________________________________________________________________________________________
# movimiento de la paleta player 
    movimiento = [0] # con w sube y se va a -1 y con s baja y se va a 1, si no se presiona ninguna tecla se queda en 0
    def mover_paleta():
        if juego_activo[0] == False:
            return # si el juego ya terminó, se detiene el movimiento de la paleta
        posicion = canvas.coords(paleta_jugador) # obtiene las cuatro coordenadas de la paleta: izquierda, arriba, derecha y abajo
        if movimiento[0] == -1:
            if posicion[1] >= 0: # comprueba que el borde superior de la paleta no haya llegado al límite superior de la ventana
                canvas.move(paleta_jugador, 0, -10) # mueve la paleta 10 píxeles hacia arriba
        if movimiento[0] == 1:
            if posicion[3] <= 800: # comprueba que el borde inferior de la paleta no haya llegado al límite inferior de la ventana
                canvas.move(paleta_jugador, 0, 10) # mueve la paleta 10 píxeles hacia abajo
        juego.after(10, mover_paleta) # vuelve a ejecutar la función después de 10 milisegundos para mantener el movimiento continuo mientras se presiona una tecla
        
    def presionar_tecla(event):
        if event.keysym == "w": # detectores de teclas presionadas, si se presiona w se va a -1 y si se presiona s se va a 1, si no se presiona ninguna tecla se queda en 0
            movimiento[0] = -1
        if event.keysym == "s":
            movimiento[0] = 1
            
    def soltar_tecla(event):
        if event.keysym == "w" or event.keysym == "s": # si se suelta la tecla w o s, se queda en 0
            movimiento[0] = 0

    juego.bind("<KeyPress-w>", presionar_tecla)
    juego.bind("<KeyPress-s>", presionar_tecla) # reciclamos los bind de la version anterior para las teclas w y s

    juego.bind("<KeyRelease-w>", soltar_tecla)
    juego.bind("<KeyRelease-s>", soltar_tecla) # creamos nuevos bind para cuando soltamos las teclas y quede quieta de manera instantanea pues se movia como a 3 fps por seg

    juego.focus_set()

    mover_paleta()
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# insertamos la paleta del player 2 (IA) y le damos movimiento autonomo con un algoritmo simple de seguimiento de la bola, para que la paleta del jugador 2 siga la posición de la bola en el eje y
    paleta_inteligencia = canvas.create_rectangle(
        140, 340, 160, 460,
        fill=colores.color_jugador_2
    )
# movimiento de la paleta ia  
    def mover_ia():
        if juego_activo[0] == False:
            return
        posicion_bola = canvas.coords(esfera) # Obtiene la posición de la bola.
        posicion_ia = canvas.coords(paleta_inteligencia) #Obtiene la posición de la paleta de la IA.
        if posicion_bola[1] < posicion_ia[1] + 60:
            if posicion_ia[1] > 0:
                canvas.move(paleta_inteligencia, 0, -4)  #Si la bola está arriba de la IA, la IA sube y si esta abajo de la IA, la IA baja, con esto la paleta de la IA sigue la bola en el eje y 
        if posicion_bola[1] > posicion_ia[1] + 60:
            if posicion_ia[3] < 800:
                canvas.move(paleta_inteligencia, 0, 4)
        juego.after(30, mover_ia) # hace que vuelva a revisar la posición cada 30 milisegundos.
    mover_ia() # llamada recursiva para que la paleta de la IA siga la bola en el eje y
#______________________________________________________________________________________________________________________________________________________________________________________________________________________ 
    # Sistema de colisiones para las paletas y la bola
    def detectar_colision(esfera, paleta_jugador, paleta_inteligencia, dx, dy):
        posicion_bola = canvas.coords(esfera) # Obtiene las coordenadas actuales de la pelota
        posicion_jugador = canvas.coords(paleta_jugador) # Obtiene las coordenadas de la paleta del jugador
        posicion_ia = canvas.coords(paleta_inteligencia) # Obtiene las coordenadas de la paleta de la IA

        radio = 15 # La pelota tiene un diámetro de 30 píxeles, por eso su radio es de 15

        # Calculamos el centro de la pelota a partir de sus coordenadas
        x = (posicion_bola[0] + posicion_bola[2]) / 2
        y = (posicion_bola[1] + posicion_bola[3]) / 2

        # Predecir la posición de la pelota en el siguiente movimiento
        siguiente_x = x + dx # Calculamos dónde estará el centro de la pelota horizontalmente
        siguiente_y = y + dy # Calculamos dónde estará el centro de la pelota verticalmente

        arriba_bola = siguiente_y - radio # Calculamos el borde superior de la pelota en la siguiente posición
        abajo_bola = siguiente_y + radio # Calculamos el borde inferior de la pelota en la siguiente posición

        # Paleta del jugador: está a la derecha
        izquierda_jugador = posicion_jugador[0] # Obtenemos el borde izquierdo de la paleta del jugador
        arriba_jugador = posicion_jugador[1] # Obtenemos el borde superior de la paleta del jugador
        abajo_jugador = posicion_jugador[3] # Obtenemos el borde inferior de la paleta del jugador

        # Comprobamos si la pelota se mueve hacia la paleta del jugador
        if dx > 0:
            # Comprobamos si la pelota ya está tocando horizontalmente la paleta
            if x + radio >= izquierda_jugador:
                if x - radio <= posicion_jugador[2]: # Comprobamos que la pelota todavía no haya pasado por completo la paleta
                    # Comprobamos si la pelota coincide verticalmente con alguna parte de la paleta
                    if abajo_bola >= arriba_jugador:
                        if arriba_bola <= abajo_jugador:
                            return 1 # Si se cumplen las condiciones, se detecta una colisión con la paleta del jugador

            # Si todavía no hay contacto, comprobamos si la pelota llegará a la paleta en el siguiente movimiento
            elif siguiente_x + radio >= izquierda_jugador:
                # Comprobamos si la pelota alcanzará la paleta por su parte superior o inferior
                if abajo_bola >= arriba_jugador:
                    if arriba_bola <= abajo_jugador:
                        return 1 # Se detecta una colisión con la paleta del jugador

        # Paleta de la IA: está a la izquierda
        derecha_ia = posicion_ia[2] # Obtenemos el borde derecho de la paleta de la IA
        arriba_ia = posicion_ia[1] # Obtenemos el borde superior de la paleta de la IA
        abajo_ia = posicion_ia[3] # Obtenemos el borde inferior de la paleta de la IA

        # Comprobamos si la pelota se mueve hacia la paleta de la IA
        if dx < 0:
            # Comprobamos si la pelota ya está tocando horizontalmente la paleta
            if x - radio <= derecha_ia:
                if x + radio >= posicion_ia[0]: # Comprobamos que la pelota todavía no haya pasado por completo la paleta
                    # Comprobamos si la pelota coincide verticalmente con alguna parte de la paleta
                    if abajo_bola >= arriba_ia:
                        if arriba_bola <= abajo_ia:
                            return -1 # Si se cumplen las condiciones, se detecta una colisión con la paleta de la IA

            # Si todavía no hay contacto, comprobamos si la pelota llegará a la paleta en el siguiente movimiento
            elif siguiente_x - radio <= derecha_ia:
                # Comprobamos si la pelota alcanzará la paleta por su parte superior o inferior
                if abajo_bola >= arriba_ia:
                    if arriba_bola <= abajo_ia:
                        return -1 # Se detecta una colisión con la paleta de la IA

        return 0 # Si no se detecta contacto con ninguna paleta, no hay colisión
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Movimiento de la bola y rebotes
    def mover_bola(dx, dy):
        if juego_activo[0] == False:
            return # Si el juego ya terminó, se detiene el movimiento de la pelota

        posicion = canvas.coords(esfera) # Obtiene las coordenadas actuales de la pelota
        x = (posicion[0] + posicion[2]) / 2 # Calcula el centro horizontal de la pelota
        y = (posicion[1] + posicion[3]) / 2 # Calcula el centro vertical de la pelota

        # Rebote superior e inferior
        if y + 15 >= 800 and dy > 0:
            dy = -abs(dy) # Si la pelota llega al borde inferior mientras baja, invertimos su dirección vertical
        elif y - 15 <= 0 and dy < 0:
            dy = abs(dy) # Si la pelota llega al borde superior mientras sube, invertimos su dirección vertical

        # Detectar colisión con las paletas
        colision = detectar_colision(
            esfera,
            paleta_jugador,
            paleta_inteligencia,
            dx,
            dy
        ) # Enviamos las coordenadas y la dirección de movimiento para comprobar si habrá un choque

        if colision == 1:
            sonidos_2.reproducir_rebote() # Reproduce el efecto de sonido cuando la pelota golpea la paleta
            # La pelota golpeó la paleta derecha
            posicion_jugador = canvas.coords(paleta_jugador) # Obtenemos las coordenadas de la paleta del jugador
            x = posicion_jugador[0] - 15 - 15 # Colocamos el centro de la pelota justo fuera del lado izquierdo de la paleta
            canvas.coords(esfera, x - 15, y - 15, x + 15, y + 15) # Actualizamos las coordenadas de la pelota para evitar que quede dentro de la paleta
            dx = -abs(dx) # Invertimos la dirección horizontal para que la pelota rebote hacia la izquierda

        elif colision == -1:
            sonidos_2.reproducir_rebote() # Reproduce el efecto de sonido cuando la pelota golpea la paleta de la IA
            # La pelota golpeó la paleta izquierda
            posicion_ia = canvas.coords(paleta_inteligencia) # Obtenemos las coordenadas de la paleta de la IA
            x = posicion_ia[2] + 15 + 15 # Colocamos el centro de la pelota justo fuera del lado derecho de la paleta
            canvas.coords(esfera, x - 15, y - 15, x + 15, y + 15) # Actualizamos las coordenadas de la pelota para evitar que quede dentro de la paleta
            dx = abs(dx) # Invertimos la dirección horizontal para que la pelota rebote hacia la derecha

        # Movimiento de la pelota
        canvas.move(esfera, dx, dy) # Movemos la pelota según su dirección horizontal y vertical

        # Comprobar si la pelota salió por los extremos
        posicion = canvas.coords(esfera) # Obtenemos las coordenadas actualizadas después del movimiento

        if posicion[2] <= 0:
            puntos_jugador[0] += 1 # Sumamos un punto al jugador cuando la pelota sale por la izquierda
            label_puntos.config(
                text="Puntos: " + str(puntos_jugador[0]) # Actualizamos la etiqueta para mostrar el puntaje del jugador
            )
            canvas.coords(esfera, 535, 385, 565, 415) # Colocamos la pelota en el centro para reiniciar la jugada
            dx, dy = 7, 5 # Restablecemos la dirección inicial de la pelota

        elif posicion[0] >= 1100:
            puntos_ia[0] += 1 # Sumamos un punto a la IA cuando la pelota sale por la derecha
            label_puntos_ia.config(
                text="IA: " + str(puntos_ia[0]) # Actualizamos la etiqueta para mostrar el puntaje de la IA
            )
            canvas.coords(esfera, 535, 385, 565, 415) # Colocamos la pelota en el centro para reiniciar la jugada
            dx, dy = -7, 5 # Restablecemos la dirección inicial hacia la izquierda

        juego.after(30, mover_bola, dx, dy) # Volvemos a ejecutar la función después de 30 milisegundos para mantener el movimiento continuo

    mover_bola(7, 5) # Iniciamos el movimiento de la pelota con una velocidad horizontal de 7 y vertical de 5
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
def abrir_juego_medio(nombre_jugador):
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
#_________________________________________________________________________________________________________________________________________________________________________________________________
# etiquetas del juego relevantes para mostrar el puntaje del jugador y de la IA, y el tiempo restante
    label_puntos = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos.place(x=850, y=60)
    
    label_nombre = tk.Label(
        juego,
        text=nombre_jugador,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )

    label_nombre.place(x=850, y=20)
    puntos_jugador = [0]
    puntos_ia = [0]
    
    label_puntos_ia = tk.Label(
        juego,
        text="IA: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_ia.place(x=150, y=60)

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
    
    def contar_tiempo():
        if tiempo[0] > 0:
            tiempo[0] -= 1  # descontamos el tiempo en 1 segundo
            label_tiempo.config(
                text="Tiempo: " + str(tiempo[0]) # mala práctica diría Jeff pero se ve bonito
            )
            juego.after(1000, contar_tiempo) # llamamos a la función contar_tiempo cada 1000 milisegundos (1 segundo) para que se actualice el tiempo restante

        else:
            juego_activo[0] = False # cuando el tiempo llegue a 0, se detiene el juego y se muestra el puntaje final del jugador y de la IA, y se guarda el puntaje del jugador en el archivo de mejores puntajes
        
            aviso = tk.Label(
                juego,
                text="Cierra esta ventana para volver al menú",
                font=("Arial", 14, "bold"),
                bg="#292A2B",
                fg="white"
            )
            aviso.place(x=350, y=750, width=400, height=35)

            mejores_puntajes.guardar_puntaje(
                nombre_jugador,
                puntos_jugador[0],
                "Medio"
            )

            if puntos_jugador[0] > puntos_ia[0]:  # en estos solo se añade la etiqueta de ganador y se muestra en la ventana del juego, no se guarda en el archivo de mejores puntajes
                label_ganador.config(
                    text=nombre_jugador + " " + "Ganaste!"
                )
                sonidos_2.reproducir_victoria()
            elif puntos_ia[0] > puntos_jugador[0]:
                label_ganador.config(
                    text="¡La IA ganó!"
                )
                sonidos_2.reproducir_victoria()
            else:
                label_ganador.config(text="¡Empate!")
    contar_tiempo()
#_________________________________________________________________________________________________________________________________________________________________________________________
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
#_____________________________________________________________________________________________________________________________________________________________________________________________________
# movimiento de la paleta player 
    movimiento = [0] # con w sube y se va a -1 y con s baja y se va a 1, si no se presiona ninguna tecla se queda en 0
    def mover_paleta():
        if juego_activo[0] == False:
            return # si el juego ya terminó, se detiene el movimiento de la paleta
        posicion = canvas.coords(paleta_jugador) # obtiene las cuatro coordenadas de la paleta: izquierda, arriba, derecha y abajo
        if movimiento[0] == -1:
            if posicion[1] >= 0: # comprueba que el borde superior de la paleta no haya llegado al límite superior de la ventana
                canvas.move(paleta_jugador, 0, -10) # mueve la paleta 10 píxeles hacia arriba
        if movimiento[0] == 1:
            if posicion[3] <= 800: # comprueba que el borde inferior de la paleta no haya llegado al límite inferior de la ventana
                canvas.move(paleta_jugador, 0, 10) # mueve la paleta 10 píxeles hacia abajo
        juego.after(10, mover_paleta) # vuelve a ejecutar la función después de 10 milisegundos para mantener el movimiento continuo mientras se presiona una tecla
        
    def presionar_tecla(event):
        if event.keysym == "w": # detectores de teclas presionadas, si se presiona w se va a -1 y si se presiona s se va a 1, si no se presiona ninguna tecla se queda en 0
            movimiento[0] = -1
        if event.keysym == "s":
            movimiento[0] = 1
            
    def soltar_tecla(event):
        if event.keysym == "w" or event.keysym == "s": # si se suelta la tecla w o s, se queda en 0
            movimiento[0] = 0

    juego.bind("<KeyPress-w>", presionar_tecla)
    juego.bind("<KeyPress-s>", presionar_tecla) # reciclamos los bind de la version anterior para las teclas w y s

    juego.bind("<KeyRelease-w>", soltar_tecla)
    juego.bind("<KeyRelease-s>", soltar_tecla) # creamos nuevos bind para cuando soltamos las teclas y quede quieta de manera instantanea pues se movia como a 3 fps por seg

    juego.focus_set()

    mover_paleta()
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# insertamos la paleta del player 2 (IA) y le damos movimiento autonomo con un algoritmo simple de seguimiento de la bola, para que la paleta del jugador 2 siga la posición de la bola en el eje y
# Dibujamos la paleta de la IA
    paleta_inteligencia = canvas.create_rectangle(
        140, 340, 160, 460,
        fill= colores.color_jugador_2
    )
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________
# movimiento de la paleta ia  
    def mover_ia():
        if juego_activo[0] == False:
            return
        posicion_bola = canvas.coords(esfera) # Obtiene la posición de la bola.
        posicion_bola2 = canvas.coords(esfera2) # Obtiene la posición de la segunda bola.
        posicion_ia = canvas.coords(paleta_inteligencia) #Obtiene la posición de la paleta de la IA.
        # Calculamos el centro de las dos bolas
        x_bola = (posicion_bola[0] + posicion_bola[2]) / 2
        y_bola = (posicion_bola[1] + posicion_bola[3]) / 2
        x_bola2 = (posicion_bola2[0] + posicion_bola2[2]) / 2
        y_bola2 = (posicion_bola2[1] + posicion_bola2[3]) / 2
        # Calculamos el centro de la paleta de la IA
        x_ia = (posicion_ia[0] + posicion_ia[2]) / 2
        y_ia = (posicion_ia[1] + posicion_ia[3]) / 2
        # Calculamos la distancia de cada bola a la paleta de la IA
        distancia_bola = ((x_bola - x_ia) ** 2 + (y_bola - y_ia) ** 2) ** 0.5
        distancia_bola2 = ((x_bola2 - x_ia) ** 2 + (y_bola2 - y_ia) ** 2) ** 0.5
        # Elegimos la bola que está más cerca de la IA
        if distancia_bola <= distancia_bola2:
            objetivo_y = y_bola # La IA sigue la primera bola
        else:
            objetivo_y = y_bola2 # La IA sigue la segunda bola
        # Si la bola está arriba de la IA, la IA sube y si está abajo, la IA baja
        if objetivo_y < y_ia:
            if posicion_ia[1] > 0:
                canvas.move(paleta_inteligencia, 0, -7)
        if objetivo_y > y_ia:
            if posicion_ia[3] < 800:
                canvas.move(paleta_inteligencia, 0, 7)
        juego.after(30, mover_ia) # hace que vuelva a revisar la posición cada 30 milisegundos.
    mover_ia() # llamada recursiva para que la paleta de la IA siga la bola en el eje y
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Sistema de colisiones para las paletas y las bolas
    def detectar_colision(esfera, paleta_jugador, paleta_inteligencia, dx, dy):
        posicion_bola = canvas.coords(esfera)
        # Obtener las coordenadas actuales de la paleta del jugador.
        posicion_jugador = canvas.coords(paleta_jugador)
        # Obtener las coordenadas actuales de la paleta de la IA.
        posicion_ia = canvas.coords(paleta_inteligencia)
        # Calcular el radio de la pelota.
        radio = (posicion_bola[2] - posicion_bola[0]) / 2
        # Calcular el centro de la pelota.
        x = (posicion_bola[0] + posicion_bola[2]) / 2
        y = (posicion_bola[1] + posicion_bola[3]) / 2
        # Predecir la posición de la pelota en el siguiente movimiento.
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Calcular los límites verticales de la pelota en la siguiente posición.
        arriba_bola = siguiente_y - radio
        abajo_bola = siguiente_y + radio
        # Paleta del jugador: está a la derecha.
        izquierda_jugador = posicion_jugador[0]
        arriba_jugador = posicion_jugador[1]
        abajo_jugador = posicion_jugador[3]
        # Comprobar si la pelota se mueve hacia la paleta del jugador.
        if dx > 0:
            # Comprobar si la pelota ya está tocando horizontalmente la paleta.
            if x + radio >= izquierda_jugador:
                if x - radio <= posicion_jugador[2]:
                    if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                        return 1
            # Comprobar si la pelota llegará a la paleta en el siguiente movimiento.
            elif siguiente_x + radio >= izquierda_jugador:
                if abajo_bola >= arriba_jugador and arriba_bola <= abajo_jugador:
                    return 1
        # Paleta de la IA: está a la izquierda.
        derecha_ia = posicion_ia[2]
        arriba_ia = posicion_ia[1]
        abajo_ia = posicion_ia[3]
        # Comprobar si la pelota se mueve hacia la paleta de la IA.
        if dx < 0:
            # Comprobar si la pelota ya está tocando horizontalmente la paleta.
            if x - radio <= derecha_ia:
                if x + radio >= posicion_ia[0]:
                    if abajo_bola >= arriba_ia and arriba_bola <= abajo_ia:
                        return -1
            # Comprobar si la pelota llegará a la paleta en el siguiente movimiento.
            elif siguiente_x - radio <= derecha_ia:
                if abajo_bola >= arriba_ia and arriba_bola <= abajo_ia:
                    return -1
        return 0
#______________________________________________________________________________________________________________________________________________________
# Movimientos de la bola con físicas y colisiones
    def mover_bola(esfera, dx, dy):
        # Si el juego terminó, no se realizan más movimientos.
        if juego_activo[0] == False:
            return
        posicion = canvas.coords(esfera)
        # Calcular el radio y el centro de la pelota.
        radio = (posicion[2] - posicion[0]) / 2
        x = (posicion[0] + posicion[2]) / 2
        y = (posicion[1] + posicion[3]) / 2
        # Obtener el tamaño actual del área de juego.
        ancho_canvas = int(canvas["width"])
        alto_canvas = int(canvas["height"])

        # Rebote contra el borde inferior.
        # Si la pelota toca el límite inferior y se mueve hacia abajo,
        # invertir dy para que comience a subir.
        if y + radio >= alto_canvas and dy > 0:
            dy = -abs(dy)
        # Rebote contra el borde superior.
        # Si la pelota toca el límite superior y se mueve hacia arriba,
        # invertir dy para que comience a bajar.
        elif y - radio <= 0 and dy < 0:
            dy = abs(dy)
        # Detectar colisiones con las dos paletas.
        # La función devuelve 1 si choca con el jugador,
        # -1 si choca con la IA y 0 si no hay colisión.
        colision = detectar_colision(
            esfera,
            paleta_jugador,
            paleta_inteligencia,
            dx,
            dy
        )
        # Colisión con la paleta del jugador, ubicada a la derecha.
        if colision == 1:
            # Reproducir el efecto de sonido del rebote.
            sonidos_2.reproducir_rebote()
            # Obtener las coordenadas actuales de la paleta.
            posicion_jugador = canvas.coords(paleta_jugador)
            # Colocar el centro de la pelota justo fuera del borde izquierdo
            # de la paleta, evitando que quede dentro de ella.
            x = posicion_jugador[0] - radio -1
            # Actualizar las coordenadas de la pelota sin cambiar su altura.
            canvas.coords(
                esfera,
                x - radio,
                y - radio,
                x + radio,
                y + radio
            )
            # Invertir la velocidad horizontal para que la pelota rebote
            # hacia la izquierda, alejándose del jugador.
            dx = -abs(dx)
        elif colision == -1:
            # Reproducir el efecto de sonido del rebote.
            sonidos_2.reproducir_rebote()
            # Obtener las coordenadas actuales de la paleta de la IA.
            posicion_ia = canvas.coords(paleta_inteligencia)
            # Colocar el centro de la peloa justo fuera del borde derecho
            # de la paleta, evitando que quede dentro de ella.
            x = posicion_ia[2] + radio + 1
            # Actualizar las coordenadas de la pelota sin cambiar su altura.
            canvas.coords(
                esfera,
                x - radio,
                y - radio,
                x + radio,
                y + radio
            )
            # Invertir la velocidad horizontal para que la pelota rebote
            # hacia la derecha, alejándose de la IA.
            dx = abs(dx)
        # Mover la pelota según sus velocidades horizontal y vertical.
        # Esto se realiza después de corregir su posición si hubo un choque.
        canvas.move(esfera, dx, dy)
        # Obtener las coordenadas actualizadas después del movimiento.
        posicion = canvas.coords(esfera)
        # Si toda la pelota salió del área de juego, el jugador obtiene un punto.
        if posicion[2] <= 0:
            # Aumentar la puntuación del jugador.
            puntos_jugador[0] += 1
            # Actualizar la etiqueta que muestra los puntos del jugador.
            label_puntos.config(
                text="Puntos: " + str(puntos_jugador[0])
            )
            # Colocar la pelota nuevamente en el centro del campo.
            canvas.coords(esfera, 535, 385, 565, 415)
            # Darle una velocidad inicial para que vuelva al juego.
            dx, dy = 7, 5
        # Comprobar si la pelota salió por el extremo derecho.
        # En ese caso, la IA obtiene un punto.
        elif posicion[0] >= ancho_canvas:
            # Aumentar la puntuación de la IA.
            puntos_ia[0] += 1
            # Actualizar la etiqueta que muestra los puntos de la IA.
            label_puntos_ia.config(
                text="IA: " + str(puntos_ia[0])
            )
            # Colocar la pelota nuevamente en el centro del campo.
            canvas.coords(esfera, 535, 385, 565, 415)
            # Darle una velocidad inicial hacia la izquierda.
            dx, dy = -7, 5
        # Programar el siguiente movimiento de la misma pelota.
        # after(30) espera 30 milisegundos antes de ejecutar la función otra vez.
        # Se conservan las velocidades actualizadas después de cada rebote.
        juego.after(30, mover_bola, esfera, dx, dy) # ojo las metas de la pelota para anotaciones son los limites de la ventana, estos estan dibujados por una linea negra pero casi no se ven
    mover_bola(esfera, 10, 8)
    mover_bola(esfera2, -10, -8)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
def abrir_juego_dificil(nombre_jugador):
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
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
    # Obstáculo móvil del modo difícil
    obstaculo = canvas.create_rectangle(
        540, 330, 560, 470,
        fill="green",
        outline="green",
        width=2
    )
    def mover_obstaculo(dy):
        if juego_activo[0] == False:
            return
        posicion = canvas.coords(obstaculo)
        if posicion[1] <= 0:
            dy = abs(dy)
        elif posicion[3] >= 800:
            dy = -abs(dy)
        canvas.move(obstaculo, 0, dy)
        juego.after(30, mover_obstaculo, dy)
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# etiquetas del juego relevantes para mostrar el puntaje del jugador y de la IA, y el tiempo restante
    label_nombre = tk.Label(
        juego,
        text=nombre_jugador,
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos = tk.Label(
        juego,
        text="Puntos: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos.place(x=850, y=60)

    label_nombre.place(x=850, y=20)
    puntos_jugador = [0]
    puntos_ia = [0]
    
    label_puntos_ia = tk.Label(
        juego,
        text="IA: 0",
        font=("Segoe UI Black", 18, "bold"),
        bg="#292A2B",
        fg="white"
    )
    label_puntos_ia.place(x=150, y=60)
    
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
    def contar_tiempo():
        if tiempo[0] > 0:
            tiempo[0] -= 1  # descontamos el tiempo en 1 segundo
            label_tiempo.config(
                text="Tiempo: " + str(tiempo[0]) # mala práctica diría Jeff pero se ve bonito
            )
            juego.after(1000, contar_tiempo) # llamamos a la función contar_tiempo cada 1000 milisegundos (1 segundo) para que se actualice el tiempo restante
        else:
            juego_activo[0] = False # cuando el tiempo llegue a 0, se detiene el juego y se muestra el puntaje final del jugador y de la IA, y se guarda el puntaje del jugador en el archivo de mejores puntajes
            aviso = tk.Label(
                juego,
                text="Cierra esta ventana para volver al menú",
                font=("Arial", 14, "bold"),
                bg="#292A2B",
                fg="white"
            )
            aviso.place(x=350, y=750, width=400, height=35)
            mejores_puntajes.guardar_puntaje(
                nombre_jugador,
                puntos_jugador[0],
                "Dificil"
            )
            if puntos_jugador[0] > puntos_ia[0]:  # en estos solo se añade la etiqueta de ganador y se muestra en la ventana del juego, no se guarda en el archivo de mejores puntajes
                label_ganador.config(
                    text=nombre_jugador + " " + "Ganaste!"
                )
                sonidos_2.reproducir_victoria()
            elif puntos_ia[0] > puntos_jugador[0]:
                label_ganador.config(
                    text="¡La IA ganó!"
                )
                sonidos_2.reproducir_victoria()
            else:
                label_ganador.config(text="¡Empate!")
    contar_tiempo()
#_________________________________________________________________________________________________________________________________________________________________________________________
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
        fill= colores.color_jugador_1
    )
#_____________________________________________________________________________________________________________________________________________________________________________________________________
# movimiento de la paleta player 
    movimiento = [0] # con w sube y se va a -1 y con s baja y se va a 1, si no se presiona ninguna tecla se queda en 0
    def mover_paleta():
        if juego_activo[0] == False:
            return # si el juego ya terminó, se detiene el movimiento de la paleta
        posicion = canvas.coords(paleta_jugador) # obtiene las cuatro coordenadas de la paleta: izquierda, arriba, derecha y abajo
        if movimiento[0] == -1:
            if posicion[1] >= 0: # comprueba que el borde superior de la paleta no haya llegado al límite superior de la ventana
                canvas.move(paleta_jugador, 0, -10) # mueve la paleta 10 píxeles hacia arriba
        if movimiento[0] == 1:
            if posicion[3] <= 800: # comprueba que el borde inferior de la paleta no haya llegado al límite inferior de la ventana
                canvas.move(paleta_jugador, 0, 10) # mueve la paleta 10 píxeles hacia abajo
        juego.after(10, mover_paleta) # vuelve a ejecutar la función después de 10 milisegundos para mantener el movimiento continuo mientras se presiona una tecla
    def presionar_tecla(event):
        if event.keysym == "w": # detectores de teclas presionadas, si se presiona w se va a -1 y si se presiona s se va a 1, si no se presiona ninguna tecla se queda en 0
            movimiento[0] = -1
        if event.keysym == "s":
            movimiento[0] = 1     
    def soltar_tecla(event):
        if event.keysym == "w" or event.keysym == "s": # si se suelta la tecla w o s, se queda en 0
            movimiento[0] = 0
    juego.bind("<KeyPress-w>", presionar_tecla)
    juego.bind("<KeyPress-s>", presionar_tecla) # reciclamos los bind de la version anterior para las teclas w y s
    juego.bind("<KeyRelease-w>", soltar_tecla)
    juego.bind("<KeyRelease-s>", soltar_tecla) # creamos nuevos bind para cuando soltamos las teclas y quede quieta de manera instantanea pues se movia como a 3 fps por seg
    juego.focus_set()
    mover_paleta()
#______________________________________________________________________________________________________________________________________________________________________________________________________   
# insertamos la paleta del player 2 (IA) y le damos movimiento autonomo con un algoritmo simple de seguimiento de la bola, para que la paleta del jugador 2 siga la posición de la bola en el eje y
# Dibujamos la paleta de la IA
    paleta_inteligencia = canvas.create_rectangle(
        140, 340, 160, 460,
        fill= colores.color_jugador_2
    )    
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
# movimiento de la paleta ia  
    def mover_ia():
        if juego_activo[0] == False:
            return
        posicion_bola = canvas.coords(esfera) # Obtiene la posición de la bola.
        posicion_bola2 = canvas.coords(esfera2) # Obtiene la posición de la segunda bola.
        posicion_ia = canvas.coords(paleta_inteligencia) #Obtiene la posición de la paleta de la IA.
        # Calculamos el centro de las dos bolas
        x_bola = (posicion_bola[0] + posicion_bola[2]) / 2
        y_bola = (posicion_bola[1] + posicion_bola[3]) / 2
        x_bola2 = (posicion_bola2[0] + posicion_bola2[2]) / 2
        y_bola2 = (posicion_bola2[1] + posicion_bola2[3]) / 2
        # Calculamos el centro de la paleta de la IA
        x_ia = (posicion_ia[0] + posicion_ia[2]) / 2
        y_ia = (posicion_ia[1] + posicion_ia[3]) / 2
        # Calculamos la distancia de cada bola a la paleta de la IA
        distancia_bola = ((x_bola - x_ia) ** 2 + (y_bola - y_ia) ** 2) ** 0.5
        distancia_bola2 = ((x_bola2 - x_ia) ** 2 + (y_bola2 - y_ia) ** 2) ** 0.5
        # Elegimos la bola que está más cerca de la IA
        if distancia_bola <= distancia_bola2:
            objetivo_y = y_bola # La IA sigue la primera bola
        else:
            objetivo_y = y_bola2 # La IA sigue la segunda bola
        # Si la bola está arriba de la IA, la IA sube y si está abajo, la IA baja
        if objetivo_y < y_ia:
            if posicion_ia[1] > 0:
                canvas.move(paleta_inteligencia, 0, -10)
        if objetivo_y > y_ia:
            if posicion_ia[3] < 800:
                canvas.move(paleta_inteligencia, 0, 10)
        juego.after(30, mover_ia) # hace que vuelva a revisar la posición cada 30 milisegundos.
    mover_ia() # llamada recursiva para que la paleta de la IA siga la bola en el eje y
#______________________________________________________________________________________________________________________________________________________________________________________________________________________
    def detectar_colision(esfera, paleta_jugador, paleta_inteligencia, dx, dy):
        posicion_bola = canvas.coords(esfera)
        posicion_jugador = canvas.coords(paleta_jugador)
        posicion_ia = canvas.coords(paleta_inteligencia)
        radio = (posicion_bola[2] - posicion_bola[0]) / 2
        x = (posicion_bola[0] + posicion_bola[2]) / 2
        y = (posicion_bola[1] + posicion_bola[3]) / 2
        # Predecir la posición de la pelota en el siguiente movimiento.
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Calcular los límites verticales de la pelota.
        arriba_bola = siguiente_y - radio
        abajo_bola = siguiente_y + radio
        # Colisión con la paleta del jugador, situada a la derecha.
        if dx > 0:
            if x + radio >= posicion_jugador[0]:
                if x - radio <= posicion_jugador[2]:
                    if abajo_bola >= posicion_jugador[1] and arriba_bola <= posicion_jugador[3]:
                        return 1
            elif siguiente_x + radio >= posicion_jugador[0]:
                if abajo_bola >= posicion_jugador[1] and arriba_bola <= posicion_jugador[3]:
                    return 1
        # Colisión con la paleta de la IA, situada a la izquierda.
        if dx < 0:
            if x - radio <= posicion_ia[2]:
                if x + radio >= posicion_ia[0]:
                    if abajo_bola >= posicion_ia[1] and arriba_bola <= posicion_ia[3]:
                        return -1
            elif siguiente_x - radio <= posicion_ia[2]:
                if abajo_bola >= posicion_ia[1] and arriba_bola <= posicion_ia[3]:
                    return -1
        return 0
#______________________________________________________________________________________________________________________________________________________
# movimientos de la bola con fisicas y colisiones
    def mover_bola(esfera, dx, dy):
        if juego_activo[0] == False:
            return
        posicion = canvas.coords(esfera)
        radio = (posicion[2] - posicion[0]) / 2
        x = (posicion[0] + posicion[2]) / 2
        y = (posicion[1] + posicion[3]) / 2
        siguiente_x = x + dx
        siguiente_y = y + dy
        # Rebotes en los bordes superior e inferior.
        if siguiente_y + radio >= 800 and dy > 0:
            dy = -abs(dy)
        elif siguiente_y - radio <= 0 and dy < 0:
            dy = abs(dy)
        # Obtener las coordenadas del obstáculo.
        pared = canvas.coords(obstaculo)
        # Detectar la colisión horizontal con el obstáculo.
        # Se comprueba también que la pelota coincida con su altura.
        if pared:
            if siguiente_y + radio >= pared[1] and siguiente_y - radio <= pared[3]:
                # La pelota se mueve hacia la derecha.
                # La pelota se mueve hacia la derecha.
                if dx > 0 and x + radio <= pared[0] and siguiente_x + radio >= pared[0]:
                    if x + radio < pared[2]:
                        dx = -abs(dx)
                        canvas.coords(
                            esfera,
                            pared[0] - 2 * radio - 1,
                            y - radio,
                            pared[0] - 1,
                            y + radio
                        )
                # La pelota se mueve hacia la izquierda.
                elif dx < 0 and x - radio >= pared[2] and siguiente_x - radio <= pared[2]:
                    if x - radio > pared[0]:
                        dx = abs(dx)
                        canvas.coords(
                            esfera,
                            pared[2] + 1,
                            y - radio,
                            pared[2] + 2 * radio + 1,
                            y + radio
                        )
        # Detectar colisiones con las paletas.
        colision = detectar_colision(
            esfera,
            paleta_jugador,
            paleta_inteligencia,
            dx,
            dy
        )
        # Rebote contra la paleta del jugador.
        if colision == 1:
            sonidos_2.reproducir_rebote()
            posicion_jugador = canvas.coords(paleta_jugador)
            # Colocar la pelota justo a la izquierda de la paleta.
            canvas.coords(
                esfera,
                posicion_jugador[0] - 2 * radio - 1,
                y - radio,
                posicion_jugador[0] - 1,
                y + radio
            )
            dx = -abs(dx)
        # Rebote contra la paleta de la IA.
        elif colision == -1:
            sonidos_2.reproducir_rebote()
            posicion_ia = canvas.coords(paleta_inteligencia)
            # Colocar la pelota justo a la derecha de la paleta.
            canvas.coords(
                esfera,
                posicion_ia[2] + 1,
                y - radio,
                posicion_ia[2] + 2 * radio + 1,
                y + radio
            )
            dx = abs(dx)
        # Mover la pelota con las velocidades actualizadas.
        canvas.move(esfera, dx, dy)
        # Obtener las coordenadas después del movimiento.
        posicion = canvas.coords(esfera)
        # Punto para el jugador si la pelota sale por la izquierda.
        if posicion[2] <= 0:
            puntos_jugador[0] += 1
            label_puntos.config(
                text="Puntos: " + str(puntos_jugador[0])
            )
            canvas.coords(esfera, 535, 385, 565, 415)
            dx, dy = 12, 12
        # Punto para la IA si la pelota sale por la derecha.
        elif posicion[0] >= 1100:
            puntos_ia[0] += 1
            label_puntos_ia.config(
                text="Puntos de la IA: " + str(puntos_ia[0])
            )
            canvas.coords(esfera, 535, 385, 565, 415)
            dx, dy = -12, -12
        # Programar el siguiente movimiento de esta pelota.
        juego.after(30, mover_bola, esfera, dx, dy)
    # Iniciar el movimiento de las dos pelotas.
    mover_bola(esfera, 12, 10)
    mover_bola(esfera2, -12, -10)
    # Iniciar el movimiento del obstáculo.
    mover_obstaculo(5)