from Clases.CacheL1 import *

class Controlador:
    def __init__(self):
        self.l1Cache = CachceL1()

    def readMiss(self, dirrecionMemoria):
        block = self.l1Cache.buscarDatos(dirrecionMemoria)
        if block is None:
            return None
        if block.getCoherence() == "M":
            block.setCoherence("O")
            return block.getData()
        elif block.getCoherence() == "O":
            return block.getData()
        elif block.getCoherence() == "E":
            block.setCoherence("S")
            return block.getData()
        elif block.getCoherence() == "S":
            return block.getData()
        elif block.getCoherence() == "I":
            return None
    
    def write(self, dirrecionMemoria, valor):
        bloqueMemoria = self.l1Cache.getBloqueWrite(dirrecionMemoria)
        if (bloqueMemoria.getCoherencia == 'M'):
            if(bloqueMemoria.getDirrecionMemoria() == dirrecionMemoria):
                bloqueMemoria.setDato(valor)
                return [["noAction"]]
            else:
                action=[["WB",bloqueMemoria.getDirrecionMemoria(),bloqueMemoria.getDato()],["writeMiss",dirrecionMemoria]]
                bloqueMemoria.setDirrecionMemoria(dirrecionMemoria)
                bloqueMemoria.setDato(dirrecionMemoria)
                return action
        elif (bloqueMemoria.getCoherencia == 'O'):
            if (bloqueMemoria.getDirrecionMemoria() == dirrecionMemoria):
                bloqueMemoria.setDato(valor)
                return [["writeMiss",dirrecionMemoria]]
            else:
                action=[["WB",bloqueMemoria.getDirrecionMemoria(),bloqueMemoria.getDato()],["writeMiss",dirrecionMemoria]]
                bloqueMemoria.setDirrecionMemoria(dirrecionMemoria)
                bloqueMemoria.setDato(valor)
                bloqueMemoria.setCoherencia("M")
                return action
        elif bloqueMemoria.getCoherencia() == "E":
            bloqueMemoria.setDirrecionMemoria(dirrecionMemoria)
            bloqueMemoria.setDato(valor)
            bloqueMemoria.setCoherencia("M")
            return [["noAction"]]
        elif bloqueMemoria.getCoherencia() == "S":
            bloqueMemoria.setDirrecionMemoria(dirrecionMemoria)
            bloqueMemoria.setDato(valor)
            bloqueMemoria.setCoherencia("M")
            return [["writeMiss",dirrecionMemoria]]
        elif bloqueMemoria.getCoherence() == "I":
            bloqueMemoria.setDirrecionMemoria(dirrecionMemoria)
            bloqueMemoria.setDato(valor)
            bloqueMemoria.setCoherencia("M")
            return [["writeMiss", dirrecionMemoria]]
        
    def writeMiss(self, dirrecionMemoria):
        bloqueMemoria = self.l1Cache.buscarDatos(dirrecionMemoria)
        if bloqueMemoria is None:
            return
        elif bloqueMemoria.getCoherencia() == "M":
            bloqueMemoria.setCoherencia("I")
        elif bloqueMemoria.getCoherencia() == "O":
            bloqueMemoria.setCoherencia("I")
        elif bloqueMemoria.getCoherencia() == "E":
            bloqueMemoria.setCoherencia("I")
        elif bloqueMemoria.getCoherencia() == "S":
            bloqueMemoria.setCoherencia("I")
    
    def readPetition(self,dirrecion):
        bloqueMemoria = self.l1Cache.buscarDatos(dirrecion)
        if bloqueMemoria is None:
            return [["readMiss",dirrecion]]
        elif bloqueMemoria.getCoherencia() == "I":
            return [["readMiss",dirrecion]]
        return [["hit",bloqueMemoria.getDirrecionMemoria(),bloqueMemoria.getDato()]]
    
    def read(self,direccion,valor,dataFrom):
        bloqueMemoria = self.l1Cache.getBloqueWrite(direccion)
        action = ["noAction"]
        if bloqueMemoria.getDirrecionMemoria() != direccion:
            if bloqueMemoria.getCoherencia() == "O" or bloqueMemoria.getCoherencia() == "M":
                action = ["WB", bloqueMemoria.getDirrecionMemoria(), bloqueMemoria.getDato()]
        bloqueMemoria.setDirrecionMemoria(direccion)
        bloqueMemoria.setDato(valor)
        if dataFrom == "memory":
            bloqueMemoria.setCoherencia("E")
        else:
            bloqueMemoria.setCoherencia("S")
        return action

        