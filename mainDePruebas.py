import time
from tkinter import *
from tkinter import ttk
from TransferenciaDeDatos import Bus
from ProcesamientoDeDatos import Cpu, InterfaceData
from threading import Lock, Thread



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
        text0="Procesador 0:\nInstrucción actual: " +procesor0.currentInstruction + "\n" + procesor0.controller.l1cache.getstring()            
        print(text0)        
        text1="Procesador 1:\nInstrucción actual: " +procesor1.currentInstruction + "\n" + procesor1.controller.l1cache.getstring()
        print(text1)
        text2="Procesador 2:\nInstrucción actual: " +procesor2.currentInstruction + "\n" + procesor2.controller.l1cache.getstring()
        print(text2)
        text3="Procesador 3:\nInstrucción actual: " +procesor3.currentInstruction + "\n" + procesor3.controller.l1cache.getstring()
        print(text3)
        text4="memoria:\n" + bus.memory.getstring()
        print(text4)
        time.sleep(5)

    # creating the tkinter window


Main_window = Tk()

# create a Label widget



def setManualMode():
    interfaceData.mode = "manual"



Thread(target=prueba4Procesadores, daemon=True).start()

Main_window.mainloop()