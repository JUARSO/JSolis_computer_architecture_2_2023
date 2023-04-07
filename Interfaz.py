import tkinter as tk
from tkinter import ttk
import time
from TransferenciaDeDatos import Bus
from ProcesamientoDeDatos import Cpu, InterfaceData
from threading import Lock, Thread

global text0

mutex = Lock()
bus = Bus()
interfaceData = InterfaceData()
procesor0 = Cpu(0, bus, mutex, interfaceData)
procesor1 = Cpu(1, bus, mutex, interfaceData)
procesor2 = Cpu(2, bus, mutex, interfaceData)
procesor3 = Cpu(3, bus, mutex, interfaceData)
processorlist = [procesor0, procesor1, procesor2, procesor3]
bus.conections.append(procesor0)
bus.conections.append(procesor1)
bus.conections.append(procesor2)
bus.conections.append(procesor3)


def createProcessorsAux(processor):
    processor.getInstruction()


def createProcessorsThreads():
    Thread(target=createProcessorsAux, args=(procesor0,), daemon=True).start()
    Thread(target=createProcessorsAux, args=(procesor1,), daemon=True).start()
    Thread(target=createProcessorsAux, args=(procesor2,), daemon=True).start()
    Thread(target=createProcessorsAux, args=(procesor3,), daemon=True).start()


if __name__ == '__main__':
    createProcessorsThreads()


def prueba4Procesadores():
    while 1:
        text0="Procesador 0:\nInstrucción actual: " +str(procesor0.currentInstructionList) #+ "\n" + str(procesor0.controller.l1cache.getstring())            
        #print(text0)        
        text1="Procesador 1:\nInstrucción actual: " +str(procesor1.currentInstructionList) #+ "\n" + str(procesor1.controller.l1cache.getstring())
        #print(text1)
        text2="Procesador 2:\nInstrucción actual: " +str(procesor2.currentInstructionList) #+ "\n" + str(procesor2.controller.l1cache.getstring())
        #print(text2)
        text3="Procesador 3:\nInstrucción actual: " +str(procesor3.currentInstructionList) #+ "\n" + str(procesor3.controller.l1cache.getstring())
        #print(text3)
        text4="Memoria:\n" +str(bus.memory.getstring())
        #print(text4)
        time.sleep(1*procesor0.interfaceData.period)



def pausar():
    procesor0.continueProcess = False


def reactivar():
    procesor0.continueProcess = True

def pasoApaso():
    procesor0.continueProcess = True
    time.sleep(1*2)
    procesor0.continueProcess = False






# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("1200x520")
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


def Procesor0Instructiones():
    return procesor0.controller.l1cache.getstring()

def ActualizarDatos0():
    textAux = Procesor0Instructiones()

    tabla0Cache.delete(*tabla0Cache.get_children())

    for i in range (len(textAux)):
        tabla0Cache.insert("", "end", values=(textAux[i]))
    
    ventana.after(5, ActualizarDatos0)

ActualizarDatos0()

tabla0Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla0Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla0Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla0Intruciones.insert("", "end", values=('B0 READ 0B0100', 'B1 CALC'))

def Procesor0Data():
    return procesor0.controller.l1cache.getstring()

def Procesor0Inst():
    textAux = Procesor0Data()

    tabla0Intruciones.delete(*tabla0Intruciones.get_children())


    tabla0Intruciones.insert("", "end", values=(procesor0.currentInstruction, procesor0.lastInstruction))
    
    ventana.after(5, Procesor0Inst)

Procesor0Inst()

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

def Procesor1Instructiones():
    return procesor1.controller.l1cache.getstring()

def ActualizarDatos1():
    textAux = Procesor1Instructiones()

    tabla1Cache.delete(*tabla1Cache.get_children())

    for i in range (len(textAux)):
        tabla1Cache.insert("", "end", values=(textAux[i]))
    
    ventana.after(5, ActualizarDatos1)

ActualizarDatos1()

tabla1Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla1Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla1Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla1Intruciones.column("Instrucion ejecutada", width=135)
tabla1Intruciones.column("Instrucion generada", width=135)
def Procesor1Data():
    return procesor1.controller.l1cache.getstring()

def Procesor1Inst():
    textAux = Procesor0Data()

    tabla1Intruciones.delete(*tabla1Intruciones.get_children())


    tabla1Intruciones.insert("", "end", values=(procesor1.currentInstruction, procesor1.lastInstruction))
    
    ventana.after(5, Procesor1Inst)

Procesor1Inst()

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

def Procesor2Instructiones():
    return procesor2.controller.l1cache.getstring()

def ActualizarDatos2():
    textAux = Procesor2Instructiones()

    tabla2Cache.delete(*tabla2Cache.get_children())

    for i in range (len(textAux)):
        tabla2Cache.insert("", "end", values=(textAux[i]))
    
    ventana.after(5, ActualizarDatos2)

ActualizarDatos2()

tabla2Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla2Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla2Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla2Intruciones.column("Instrucion ejecutada", width=135)
tabla2Intruciones.column("Instrucion generada", width=135)
def Procesor2Data():
    return procesor2.controller.l1cache.getstring()

def Procesor2Inst():
    textAux = Procesor2Data()

    tabla2Intruciones.delete(*tabla2Intruciones.get_children())


    tabla2Intruciones.insert("", "end", values=(procesor2.currentInstruction, procesor2.lastInstruction))
    
    ventana.after(5, Procesor2Inst)

Procesor2Inst()

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

def Procesor3Instructiones():
    return procesor3.controller.l1cache.getstring()

def ActualizarDatos3():
    textAux = Procesor3Instructiones()

    tabla3Cache.delete(*tabla3Cache.get_children())

    for i in range (len(textAux)):
        tabla3Cache.insert("", "end", values=(textAux[i]))
    
    ventana.after(5, ActualizarDatos3)

ActualizarDatos3()
tabla3Intruciones = ttk.Treeview(ventana, columns=('Instrucion ejecutada', 'Instrucion generada'), show='headings')
tabla3Intruciones.heading("Instrucion ejecutada", text="Instrucion ejecutada")
tabla3Intruciones.heading("Instrucion generada", text="Instrucion generada")
tabla3Intruciones.column("Instrucion ejecutada", width=135)
tabla3Intruciones.column("Instrucion generada", width=135)
def Procesor3Data():
    return procesor3.controller.l1cache.getstring()

def Procesor3Inst():
    textAux = Procesor3Data()

    tabla3Intruciones.delete(*tabla3Intruciones.get_children())


    tabla3Intruciones.insert("", "end", values=(procesor3.currentInstruction, procesor3.lastInstruction))
    
    ventana.after(5, Procesor3Inst)

Procesor3Inst()

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


def MemoriaData():
    return bus.memory.getstring()

def MemoriaDataPrint():
    textAux = MemoriaData()

    tablaMemoria.delete(*tablaMemoria.get_children())

    for i in range (len(textAux)):
        tablaMemoria.insert("", "end", values=(textAux[i]))
    
    ventana.after(5, MemoriaDataPrint)

MemoriaDataPrint()

# Crear el título de la tabla para el procesador #1
memoriaLabel = ttk.Label(ventana, text="Memoria", font=("Arial", 12))
ultimaEjecucionEjecutada = ttk.Label(ventana, text='Ultima instrucion ejecutada:', font=('Arial', 12))
# Posicionar la tabla y el título en la ventana para el procesador #1                   +++y 5-*/.7b53c e6
ultimaEjecucionEjecutada.place(x=20, y= 450)
tablaMemoria.place(x=20, y=270, width=270, height=160)
memoriaLabel.place(x=20, y=240)

"""
------------------------------------- Botones --------------------------------------------------------------
"""


botonPausa = ttk.Button(ventana, text="Pausa", command=pausar)
botonPasoAPaso =  ttk.Button(ventana, text="Paso a Paso", command=pasoApaso)
botonAutomatico =  ttk.Button(ventana, text="Automatico", command=reactivar)
botonEnviar =  ttk.Button(ventana, text="Enviar")
# Ejecutar el bucle principal de la ventana

botonPausa.place(x=500, y = 300)
botonPasoAPaso.place(x= 600, y = 300)
botonAutomatico.place(x=800, y = 300)

ColoqueLaInstruccion = tk.Label(ventana, text="Introduzca la Instruccion:", font=("Arial", 12))
entradaDeTexto = tk.Entry(ventana, width=40)
ColoqueLaInstruccion.place(x=400, y=340)
entradaDeTexto.place(x=400,y=370)
botonEnviar.place(x=700, y=370)

Thread(target=prueba4Procesadores, daemon=True).start()

ventana.mainloop()