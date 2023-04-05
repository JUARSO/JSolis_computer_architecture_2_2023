from Clases.generadorDeInstruciones import *

class bloqueMemoria:
    def __init__(self,numero, dato):
        self.numero = numero
        self.dato = dato

    def getNumero(self):
        return int(str(self.numero),2)
    
    def setNumero(self, numero):
        self.numero = decimalToBinario(numero, 3)

    def getDato(self):
        return int(str(self.dato),16)

    def setDato(self, dato):
        self.dato = decimalToHexadecimal(dato,16)


    def getString(self):
        return "bloque: "+str(decimalToBinario(self.numero,3))+", dato: "+str(self.dato)