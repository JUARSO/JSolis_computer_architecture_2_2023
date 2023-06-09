import tkinter as tk
from tkinter import ttk
from TransferenciaDeDatos import Bus
from ProcesamientoDeDatos import Cpu, InterfaceData
from threading import Lock, Thread 
import threading
import time




# Creamos el lock
lock = Lock()
bus = Bus()
interfaceData = InterfaceData()

#Se crean los 4 procesaodres
procesor0 = Cpu(0, bus, lock, interfaceData)
procesor1 = Cpu(1, bus, lock, interfaceData)
procesor2 = Cpu(2, bus, lock, interfaceData)
procesor3 = Cpu(3, bus, lock, interfaceData)
processorlist = [procesor0, procesor1, procesor2, procesor3]

#Los procesadores se conectan el bus
bus.conections.append(procesor0)
bus.conections.append(procesor1)
bus.conections.append(procesor2)
bus.conections.append(procesor3)




def createProcessorsAux(processor):
    processor.getInstruction()


#Creacion de los hilos
def createProcessorsThreads():
    t1 = Thread(target=createProcessorsAux, args=(procesor0,), daemon=True).start()
    t2 = Thread(target=createProcessorsAux, args=(procesor1,), daemon=True).start()
    t3 = Thread(target=createProcessorsAux, args=(procesor2,), daemon=True).start()
    t4 = Thread(target=createProcessorsAux, args=(procesor3,), daemon=True).start()


# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("1200x520")
ventana.configure(bg="#F3E5AB")

'''
--------------------------------------------------- Proceador #0 -----------------------------------------------
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

tabla0Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla0Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla0Intruciones.heading("Instrucion generada", text="Instrucion generada")

tabla0Intruciones.column("Instrucion ejecutada", width=135)
tabla0Intruciones.column("Instrucion generada", width=135)
# Crear el título de la tabla para el procesador #1
titulo_tabla0 = ttk.Label(ventana, text="Procesador 1", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla0Cache.place(x=20, y=40, width=270, height=120)
tabla0Intruciones.place(x=20, y=180 , width= 270, height=50)
titulo_tabla0.place(x=20, y=10)


'''
--------------------------------------------------- Proceador #1 -----------------------------------------------
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

tabla1Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla1Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla1Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla1Intruciones.column("Instrucion ejecutada", width=135)
tabla1Intruciones.column("Instrucion generada", width=135)

# Crear el título de la tabla para el procesador #1
titulo_tabla1 = ttk.Label(ventana, text="Procesador 2", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla1Cache.place(x=310, y=40, width=270, height=120)
tabla1Intruciones.place(x=310, y=180 , width= 270, height=50)
titulo_tabla1.place(x=310, y=10)

'''
--------------------------------------------------- Proceador #2 -----------------------------------------------
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




tabla2Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla2Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla2Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla2Intruciones.column("Instrucion ejecutada", width=135)
tabla2Intruciones.column("Instrucion generada", width=135)





# Crear el título de la tabla para el procesador #1
titulo_tabla2 = ttk.Label(ventana, text="Procesador 3", font=("Arial", 12))

# Posicionar la tabla y el título en la ventana para el procesador #1
tabla2Cache.place(x=600, y=40, width=270, height=120)
tabla2Intruciones.place(x=600, y=180 , width= 270, height=50)
titulo_tabla2.place(x=600, y=10)

'''
--------------------------------------------------- Proceador #3 -----------------------------------------------
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



tabla3Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla3Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla3Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla3Intruciones.column("Instrucion ejecutada", width=135)
tabla3Intruciones.column("Instrucion generada", width=135)

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




# Crear el título de la tabla para el procesador #1
memoriaLabel = ttk.Label(ventana, text="Memoria", font=("Arial", 12))
# Posicionar la tabla y el título en la ventana para el procesador #1                   +++y 5-*/.7b53c e6
tablaMemoria.place(x=20, y=270, width=270, height=200)
memoriaLabel.place(x=20, y=240)

"""
------------------------------------- Botones --------------------------------------------------------------
"""


def pausa():
    for p in processorlist:
        p.continueProcess = False
    print("Pausa")

def Inicio():
    createProcessorsThreads()
    print('La aplicacion se ha iniciado')

def setTimeMode():
    for p in processorlist:
        p.continueProcess = True 
    print('Modo automatico')

def nextCycle():
    for p in processorlist:
        p.continueProcess = True 
    time.sleep(1)
    for p in processorlist:
        p.continueProcess = False
    print('Paso a Paso')

botonDeInicio = ttk.Button(ventana, text="Iniciar", command=Inicio)
botonDePausa =  ttk.Button(ventana, text="Pausa", command=pausa)
botonPasoAPaso = ttk.Button(ventana, text='Paso a paso', command=nextCycle)
botonAutomatico =  ttk.Button(ventana, text="Automatico", command=setTimeMode)
# Ejecutar el bucle principal de la ventana

botonDeInicio.place(x=400, y = 240)
botonDePausa.place(x= 500, y = 240)
botonPasoAPaso.place(x=600, y = 240)
botonAutomatico.place(x=700, y = 240)



def actualizacionDeDatos():
    #Procesador 0
    textAux = procesor0.controller.l1cache.getstring()
    tabla0Cache.delete(*tabla0Cache.get_children())
    for i in range (len(textAux)):
        tabla0Cache.insert("", "end", values=(textAux[i]))
    #Procesador 1
    textAux = procesor1.controller.l1cache.getstring()
    tabla1Cache.delete(*tabla1Cache.get_children())
    for i in range (len(textAux)):
        tabla1Cache.insert("", "end", values=(textAux[i]))
    #Procesador 2
    textAux = procesor2.controller.l1cache.getstring()
    tabla2Cache.delete(*tabla2Cache.get_children())
    for i in range (len(textAux)):
        tabla2Cache.insert("", "end", values=(textAux[i]))
    #Procesador 3
    textAux = procesor3.controller.l1cache.getstring()
    tabla3Cache.delete(*tabla3Cache.get_children())
    for i in range (len(textAux)):
        tabla3Cache.insert("", "end", values=(textAux[i]))
    ventana.after(1, actualizacionDeDatos)


def actualizacionDeInstruciones():
    #Procesador 0
    tabla0Intruciones.delete(*tabla0Intruciones.get_children())
    tabla0Intruciones.insert("", "end", values=(procesor0.lastInstruction, procesor0.currentInstruction))
    #Procesador 1
    tabla1Intruciones.delete(*tabla1Intruciones.get_children())
    tabla1Intruciones.insert("", "end", values=(procesor1.lastInstruction, procesor1.currentInstruction))
    #Procesador 2
    tabla2Intruciones.delete(*tabla2Intruciones.get_children())
    tabla2Intruciones.insert("", "end", values=(procesor2.lastInstruction, procesor2.currentInstruction))
    #Procesador 3
    tabla3Intruciones.delete(*tabla3Intruciones.get_children())
    tabla3Intruciones.insert("", "end", values=(procesor3.lastInstruction, procesor3.currentInstruction))
    ventana.after(1, actualizacionDeInstruciones)


def ActualizarMemoria():
    textAux = bus.memory.getstring()
    tablaMemoria.delete(*tablaMemoria.get_children())
    for i in range (len(textAux)):
        tablaMemoria.insert("", "end", values=(textAux[i]))
    ventana.after(1, ActualizarMemoria)

actualizacionDeInstruciones()
actualizacionDeDatos()
ActualizarMemoria()

ventana.mainloop()