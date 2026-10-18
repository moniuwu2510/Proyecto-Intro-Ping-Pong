import tkinter as tk 
from tkinter import colorchooser
from PIL import Image, ImageTk 
import sonidos
import musica
import colores
import personalizacion_datos
#____________________________________________________________________________________________________________________________________________________________#
def abrir_personalizaciones(window):
        window.destroy()
        personalizaciones = tk.Toplevel()
        personalizaciones.title("Personalizaciones")
        personalizaciones.geometry("600x500")
        personalizaciones.resizable(False, False)
# Fondo
        imagen_personalizaciones = Image.open("fondo_definitivo_2.gif")
        imagen_personalizaciones = imagen_personalizaciones.resize((600, 500))
        fondo_personalizaciones = ImageTk.PhotoImage(
            imagen_personalizaciones,
            master=personalizaciones
        )
        canvas_personalizaciones = tk.Canvas(
            personalizaciones,
            width=600,
            height=500,
            highlightthickness=0
        )
        canvas_personalizaciones.place(x=0, y=0)
        canvas_personalizaciones.create_image(
            0, 0,
            image=fondo_personalizaciones,
            anchor="nw"
        )
# Guardar la imagen
        canvas_personalizaciones.fondo = fondo_personalizaciones
        canvas_personalizaciones.create_text(
            300, 55,
            text="Personalizaciones",
            font=("Impact", 25, "bold"),
            fill="white"
        )
# Selección de fondos
        label_fondos = tk.Label(
            personalizaciones,
            text="Selecciona el fondo de tu partida:",
            font=("Impact", 15, "bold"),
            bg="#292A2B",
            fg="white"
        )
        label_fondos.place(x=120, y=110)

        fondos_disponibles = [
            "fondo_definitivo_2.gif",
            "fondo_dificil.png",
            "fondo_extra.jpe",
            "fondo_facil.jpg",
            "fondo_medio.jpg"
        ]
        fondo_elegido = tk.StringVar(value=fondos_disponibles[0])
        selector_fondos = tk.OptionMenu(
            personalizaciones,
            fondo_elegido,
            *fondos_disponibles
        )
        selector_fondos.config(
            font=("Impact", 12, "bold"),
            bg="#4B7496",
            fg="white",
            width=20
        )
        selector_fondos.place(x=170, y=150)
# Vista previa del fondo seleccionado
        vista_previa = tk.Label(personalizaciones, bg="#292A2B")
        vista_previa.place(x=175, y=200, width=250, height=140)

        imagen_previa = [None]

        def actualizar_vista_previa(nombre_fondo):
            imagen = Image.open(nombre_fondo)
            imagen = imagen.resize((250, 140))
            imagen_previa[0] = ImageTk.PhotoImage(
                imagen,
                master=personalizaciones
            )
            vista_previa.config(image=imagen_previa[0])

        def seleccionar_fondo(nombre_fondo):
            fondo_elegido.set(nombre_fondo)
            actualizar_vista_previa(nombre_fondo)

            personalizacion_datos.fondo_seleccionado = nombre_fondo

        selector_fondos = tk.OptionMenu(
            personalizaciones,
            fondo_elegido,
            *fondos_disponibles,
            command=seleccionar_fondo
        )

        selector_fondos.config(
            font=("Impact", 12, "bold"),
            bg="#4B7496",
            fg="white",
            width=20
        )
        selector_fondos.place(x=170, y=150)

        actualizar_vista_previa(fondo_elegido.get())
# Selección de música
        label_musica = tk.Label(
            personalizaciones,
            text="Selecciona la música:",
            font=("Impact", 15, "bold"),
            bg="#292A2B",
            fg="white"
        )
        label_musica.place(x=190, y=355)

        canciones_disponibles = [
            musica.tema_1,
            musica.tema_2
]

        cancion_elegida = tk.StringVar(
            master=personalizaciones,
            value=canciones_disponibles[0]
        )
        def seleccionar_cancion(nombre_cancion):
            cancion_elegida.set(nombre_cancion)
            personalizacion_datos.cancion_seleccionada = nombre_cancion

        selector_musica = tk.OptionMenu(
            personalizaciones,
            cancion_elegida,
            *canciones_disponibles,
            command=seleccionar_cancion
        )
        selector_musica.config(
            font=("Impact", 12, "bold"),
            bg="#4B7496",
            fg="white",
            width=20
        )
        selector_musica.place(x=170, y=390)

        # Ventana para cambiar los colores
        def abrir_colores():
            personalizaciones.destroy()

            ventana_colores = tk.Toplevel()
            ventana_colores.title("Colores de la partida")
            ventana_colores.geometry("600x500")
            ventana_colores.resizable(False, False)

            # Fondo
            imagen_colores = Image.open("fondo_definitivo_2.gif")
            imagen_colores = imagen_colores.resize((600, 500))
            fondo_colores = ImageTk.PhotoImage(
                imagen_colores,
                master=ventana_colores
            )

            canvas_colores = tk.Canvas(
                ventana_colores,
                width=600,
                height=500,
                highlightthickness=0
            )
            canvas_colores.place(x=0, y=0)
            canvas_colores.create_image(
                0, 0,
                image=fondo_colores,
                anchor="nw"
            )

            # Guardar la imagen
            canvas_colores.fondo = fondo_colores

            canvas_colores.create_text(
                300, 60,
                text="Colores de la partida",
                font=("Impact", 25, "bold"),
                fill="white"
            )

            # Cambiar el color seleccionado
            def cambiar_color(tipo):
                if tipo == "jugador_1":
                    color_actual = colores.color_jugador_1
                elif tipo == "jugador_2":
                    color_actual = colores.color_jugador_2
                else:
                    color_actual = colores.color_pelota

                resultado = colorchooser.askcolor(
                    title="Selecciona un color",
                    parent=ventana_colores
                )
                # Guardar el color si se seleccionó uno
                if resultado[1] is not None:
                    if tipo == "jugador_1":
                        colores.color_jugador_1 = resultado[1]
                        boton_jugador_1.config(bg=resultado[1])
                    elif tipo == "jugador_2":
                        colores.color_jugador_2 = resultado[1]
                        boton_jugador_2.config(bg=resultado[1])
                    else:
                        colores.color_pelota = resultado[1]
                        boton_pelota.config(bg=resultado[1])

            # Color del Jugador 1
            boton_jugador_1 = tk.Button(
                ventana_colores,
                text="Color del Jugador 1",
                command=lambda: cambiar_color("jugador_1"),
                font=("Impact", 15, "bold"),
                bg=colores.color_jugador_1,
                fg="white",
                width=22,
                height=2
            )
            boton_jugador_1.place(x=175, y=125)

            # Color del Jugador 2 o IA
            boton_jugador_2 = tk.Button(
                ventana_colores,
                text="Color del Jugador 2 / IA",
                command=lambda: cambiar_color("jugador_2"),
                font=("Impact", 15, "bold"),
                bg=colores.color_jugador_2,
                fg="white",
                width=22,
                height=2
            )
            boton_jugador_2.place(x=175, y=220)

            # Color de todas las pelotas
            boton_pelota = tk.Button(
                ventana_colores,
                text="Color de las pelotas",
                command=lambda: cambiar_color("pelota"),
                font=("Impact", 15, "bold"),
                bg=colores.color_pelota,
                fg="white",
                width=22,
                height=2
            )
            boton_pelota.place(x=175, y=315)
# Botón para abrir la ventana de colores
        boton_colores = tk.Button(
            personalizaciones,
            text="Colores de la partida",
            command=lambda: (
                sonidos.reproducir_sonido(),
                abrir_colores()
            ),
            font=("Impact", 13, "bold"),
            bg="#4B7496",
            fg="white",
            width=20,
            height=1
        )
        boton_colores.place(x=180, y=440)

