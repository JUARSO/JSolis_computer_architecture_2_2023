import time
from Clases.Controlador import Controlador
from Clases.generadorDeInstruciones import *


class Cpu:
    def __init__(self, numero, bus, mutex, iterfaceData):
        self.numero = numero
        self.controlador = Controlador()
        self.bus = bus
        self.instruccionActual = ""
        self.mutex = mutex
        self.interfaceData = iterfaceData
        self.instrucionesManuales = []
        self.nextCycle = False
        self.ultimaInstruccion = ""
        self.continueProcess = True

    def setInstruccionManual(self, instrucion):
        self.instrucionesManuales = instrucion

    def getInstruction(self):
        name =  "file" + str(self.numero) + ".txt"
        file1 = open(name, 'w')
        file1.close()

        while 1:
            print(self.instrucionesManuales)
            if not self.instrucionesManuales:
                instrucion = generarInstucion()
            else:
                instrucion = self.instrucionesManuales
                self.instrucionesManuales = []
            print(self.numero, instrucion)
            actions = []
            if instrucion[0] == 'calc':
                self.instruccionActual = 'P' + str(self.numero) + ':CALC'
                actions = [['noAction']]
            elif instrucion[0] == 'wirete':
                self.instruccionActual = "P" + str(self.numero) + ": WRITE " + instrucion[1] + ";" + instrucion[2]
                actions = self.controlador.write(int(instrucion[1], 2), int(instrucion[2], 16))
            elif instrucion[0] == 'read':
                self.instruccionActual = "P" + str(self.number) + ": READ " + instrucion[1]
                actions = self.controlador.readPetition(int(instrucion[1], 2))
            self.log(self.instruccionActual + " cache: |" + self.controlador.l1Cache.getString())
            self.interfaceData.ultimaInstruccion = self.instruccionActual
            self.manageBus(actions)
            self.ultimaInstruccion = self.instruccionActual
            self.applyMode()

    def manageBus(self, actions):
        action = actions[0]
        if action[0] != 'noAction' and action[0] != 'hit':
            self.mutex.acquiere()
            if len(actions) == 2:
                self.bus.writeEnMemoria(action[1], action[2])
                self.applyMode()
                action = actions[1]
            if (action[0] == 'readMiss'):
                print(self.numero, 'readMiss')
                self.waitResponse(action[1])
            elif action[0] == "writeMiss":
                print(self.numero, "writemiss")
                self.Invalidate(action[1])
            self.mutex.release()

    def waitResponse(self, dirrecionMemoria):
        data = None
        for i in range(4):
            if i != self.numero:
                readed = self.bus.coneciones[i].controlador.readMiss(dirrecionMemoria)
                if readed is not None:
                    data = readed
        if data is None:
            data = self.bus.redEnMemoria(dirrecionMemoria)
            self.applyMode()
            action = self.controlador.read(dirrecionMemoria, data, 'memory')
        else:
            action = self.controlador.read(dirrecionMemoria, data, 'cache')
        if action[0] == 'WB':
            self.bus.writeEnMemoria(action[1], action[2])
            self.applyMode()
    
    def invalidate(self, dirrecionMemoria):
        for i in range(4):
            if i != self.numero:
                self.bus.coneciones[i].controlador.writeMiss(dirrecionMemoria)
    
    def apllyMode(self):
        if self.interfaceData.mode == 'manual':
            while 1:
                if self.nextCycle:
                    self.nextCycle = False
        else:
            while 1:
                if self.continueProcess:
                    break
            time.sleep(self.interfaceData.period)

    def log(self, string):
        name = 'file' + str(self.numero) + '.txt'
        file1 = open(name, "a")
        file1.write("\n")
        file1.write(string)
        file1.close()
