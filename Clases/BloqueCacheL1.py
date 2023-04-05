from Clases.generadorDeInstruciones import *

class BloqueCacheL1():
    def __init__(self, numero, cohenrecia, dato , dirrecionMemoria):
        self.numero = numero
        self.coherencia = cohenrecia
        self.dato = dato
        self.dirrecionMemoria = dirrecionMemoria

    def getNumero(self):
        return self.numero
    
    def setNumero(self, numero):
        self.numero = numero
    
    def getCoherencia(self):
        return self.coherencia
    
    def setCoherencia(self, conherencia):
        self.coherencia = conherencia

    def getDato(self):
        return int(str(self.dato), 16)
    
    def setDato(self, dato):
        self.dato = decimalToHexadecimal(dato,16)

    def getDirrecionMemoria(self):
        return int(str(self.dato),2)

    def setDirrecionMemoria(self, direccionMemoria):
        self.dirrecionMemoria = decimalToBinario(direccionMemoria, 3)


    def getString(self):
        return "bloque: " + str(self.numero) + ", coherencia: " + self.coherencia + ", dato: " + str(
            self.dato) + ", dirección: " + str(self.dirrecionMemoria)      