import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("1200x720")
ventana.configure(bg="#F3E5AB")

'''
--------------------------------------------------- Proceador #1 -----------------------------------------------
'''
# Crear la tabla para el procesador #1
tabla0Cache = ttk.Treeview(ventana, columns=("Bloque", "Coherencia", "Direccion", "Valor"), show="headings")
tabla0Cache.heading("Bloque", text="Bloque")
tabla0Cache.heading("Coherencia", text="Coherencia")
tabla0Cache.heading("Direccion", text="Direccion")
tabla0Cache.heading("Valor", text="Valor")

# Configurar el tamaño de la tabla procesador #1
tabla0Cache.column("Bloque", width=50)
tabla0Cache.column("Coherencia", width=75)
tabla0Cache.column("Direccion", width=75)
tabla0Cache.column("Valor", width=70)

# Insertar los datos iniciales en la tabala del procesador #1
tabla0Cache.insert("", "end", values=("B0", "I", "0B0000", "0xFFFF"))
tabla0Cache.insert("", "end", values=("B1", "I", "0B0000", "0XFFFF"))
tabla0Cache.insert("", "end", values=("B2", "I", "0B0000", "0xFFFF"))
tabla0Cache.insert("", "end", values=("B4", "I", "0B0000", "0xFFFF"))

tabla0Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla0Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla0Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla0Intruciones.insert("", "end", values=('B0 READ 0B0100', 'B1 CALC'))


tabla0Intruciones.column("Instrucion ejecutada", width=135)
tabla0Intruciones.column("Instrucion generada", width=135)
# Crear el título de la tabla para el procesador #1
titulo_tabla0 = ttk.Label(ventana, text="Procesador 1", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla0Cache.place(x=20, y=40, width=270, height=120)
tabla0Intruciones.place(x=20, y=180 , width= 270, height=50)
titulo_tabla0.place(x=20, y=10)


'''
--------------------------------------------------- Proceador #2 -----------------------------------------------
'''

# Crear la tabla para el procesador #1
tabla1Cache = ttk.Treeview(ventana, columns=("Bloque", "Coherencia", "Direccion", "Valor"), show="headings")
tabla1Cache.heading("Bloque", text="Bloque")
tabla1Cache.heading("Coherencia", text="Coherencia")
tabla1Cache.heading("Direccion", text="Direccion")
tabla1Cache.heading("Valor", text="Valor")

# Configurar el tamaño de la tabla procesador #1
tabla1Cache.column("Bloque", width=50)
tabla1Cache.column("Coherencia", width=75)
tabla1Cache.column("Direccion", width=75)
tabla1Cache.column("Valor", width=70)

# Insertar los datos iniciales en la tabala del procesador #1
tabla1Cache.insert("", "end", values=("B0", "I", "0B0000", "0xFFFF"))
tabla1Cache.insert("", "end", values=("B1", "I", "0B0000", "0XFFFF"))
tabla1Cache.insert("", "end", values=("B2", "I", "0B0000", "0xFFFF"))
tabla1Cache.insert("", "end", values=("B4", "I", "0B0000", "0xFFFF"))

tabla1Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla1Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla1Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla1Intruciones.column("Instrucion ejecutada", width=135)
tabla1Intruciones.column("Instrucion generada", width=135)
tabla1Intruciones.insert("", "end", values=('B0 READ 0B0100', 'B1 CALC'))

# Crear el título de la tabla para el procesador #1
titulo_tabla1 = ttk.Label(ventana, text="Procesador 2", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla1Cache.place(x=310, y=40, width=270, height=120)
tabla1Intruciones.place(x=310, y=180 , width= 270, height=50)
titulo_tabla1.place(x=310, y=10)

'''
--------------------------------------------------- Proceador #3 -----------------------------------------------
'''
# Crear la tabla para el procesador #1
tabla2Cache = ttk.Treeview(ventana, columns=("Bloque", "Coherencia", "Direccion", "Valor"), show="headings")
tabla2Cache.heading("Bloque", text="Bloque")
tabla2Cache.heading("Coherencia", text="Coherencia")
tabla2Cache.heading("Direccion", text="Direccion")
tabla2Cache.heading("Valor", text="Valor")

# Configurar el tamaño de la tabla procesador #1
tabla2Cache.column("Bloque", width=50)
tabla2Cache.column("Coherencia", width=75)
tabla2Cache.column("Direccion", width=75)
tabla2Cache.column("Valor", width=70)

# Insertar los datos iniciales en la tabala del procesador #1
tabla2Cache.insert("", "end", values=("B0", "I", "0B0000", "0xFFFF"))
tabla2Cache.insert("", "end", values=("B1", "I", "0B0000", "0XFFFF"))
tabla2Cache.insert("", "end", values=("B2", "I", "0B0000", "0xFFFF"))
tabla2Cache.insert("", "end", values=("B4", "I", "0B0000", "0xFFFF"))

tabla2Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla2Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla2Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla2Intruciones.column("Instrucion ejecutada", width=135)
tabla2Intruciones.column("Instrucion generada", width=135)
tabla2Intruciones.insert("", "end", values=('B0 READ 0B0100', 'B1 CALC'))

# Crear el título de la tabla para el procesador #1
titulo_tabla2 = ttk.Label(ventana, text="Procesador 3", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla2Cache.place(x=600, y=40, width=270, height=120)
tabla2Intruciones.place(x=600, y=180 , width= 270, height=50)
titulo_tabla2.place(x=600, y=10)

'''
--------------------------------------------------- Proceador #4 -----------------------------------------------
'''
# Crear la tabla para el procesador #1
tabla3Cache = ttk.Treeview(ventana, columns=("Bloque", "Coherencia", "Direccion", "Valor"), show="headings")
tabla3Cache.heading("Bloque", text="Bloque")
tabla3Cache.heading("Coherencia", text="Coherencia")
tabla3Cache.heading("Direccion", text="Direccion")
tabla3Cache.heading("Valor", text="Valor")

# Configurar el tamaño de la tabla procesador #1
tabla3Cache.column("Bloque", width=50)
tabla3Cache.column("Coherencia", width=75)
tabla3Cache.column("Direccion", width=75)
tabla3Cache.column("Valor", width=70)

# Insertar los datos iniciales en la tabala del procesador #1
tabla3Cache.insert("", "end", values=("B0", "I", "0B0000", "0xFFFF"))
tabla3Cache.insert("", "end", values=("B1", "I", "0B0000", "0XFFFF"))
tabla3Cache.insert("", "end", values=("B2", "I", "0B0000", "0xFFFF"))
tabla3Cache.insert("", "end", values=("B4", "I", "0B0000", "0xFFFF"))

tabla3Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla3Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla3Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla3Intruciones.column("Instrucion ejecutada", width=135)
tabla3Intruciones.column("Instrucion generada", width=135)
tabla3Intruciones.insert("", "end", values=('B0 READ 0B0100', 'B1 CALC'))

# Crear el título de la tabla para el procesador #1
titulo_tabla3 = ttk.Label(ventana, text="Procesador 4", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla3Cache.place(x=890, y=40, width=270, height=120)
tabla3Intruciones.place(x=890, y=180 , width= 270, height=50)
titulo_tabla3.place(x=890, y=10)
'''
--------------------------------------------------------- Memoria -----------------------------------------------------------
'''

tablaMemoria = ttk.Treeview(ventana, columns=('Direcion de memeoria', 'Valor'), show='headings')
tablaMemoria.heading("Direcion de memeoria", text="Direcion de memeoria")
tablaMemoria.heading("Valor", text="Valor")
tablaMemoria.column("Direcion de memeoria", width=135)
tablaMemoria.column("Valor", width=135)


tablaMemoria.insert("", "end", values=("0B0000", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0001", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0010", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0011", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0100", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0101", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0110", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B0111", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1000", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1001", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1010", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1011", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1100", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1101", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1110", "0xFFFF"))
tablaMemoria.insert("", "end", values=("0B1111", "0xFFFF"))

# Crear el título de la tabla para el procesador #1
memoriaLabel = ttk.Label(ventana, text="Memoria", font=("Arial", 12))
ultimaEjecucionEjecutada = ttk.Label(ventana, text='Ultima instrucion ejecutada:', font=('Arial', 12))
# Posicionar la tabla y el título en la ventana para el procesador #1
ultimaEjecucionEjecutada.place(x=20, y= 650)
tablaMemoria.place(x=20, y=270, width=270, height=360)
memoriaLabel.place(x=20, y=240)

"""
------------------------------------- Botones --------------------------------------------------------------
"""

botonDeInicio = ttk.Button(ventana, text="Inicio")
botonPausa = ttk.Button(ventana, text="Pausa")
botonPasoAPaso =  ttk.Button(ventana, text="Paso a Paso")
botonSiguiente = ttk.Button(ventana, text="Siguiente")
botonAutomatico =  ttk.Button(ventana, text="Automatico")
botonEnviar =  ttk.Button(ventana, text="Enviar")
# Ejecutar el bucle principal de la ventana

botonDeInicio.place(x=400, y=340)
botonPausa.place(x=500, y = 340)
botonPasoAPaso.place(x= 600, y = 340)
botonSiguiente.place(x=700, y= 340)
botonAutomatico.place(x=800, y = 340)

ColoqueLaInstruccion = tk.Label(ventana, text="Introduzca la Instruccion:", font=("Arial", 12))
entradaDeTexto = tk.Entry(ventana, width=40)
ColoqueLaInstruccion.place(x=400, y=400)
entradaDeTexto.place(x=400,y=430)
botonEnviar.place(x=700, y=425)
ventana.mainloop()