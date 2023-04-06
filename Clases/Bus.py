from Clases.memory import Memoria

class Bus:
    def __init__(self):
        self.coneciones = []
        self.memoria = Memoria()

    def writeEnMemoria(self, direccionMemoria, valor):
        bloqueMemoria = self.memoria.getBloqueMemoria(direccionMemoria)
        bloqueMemoria.setDato(valor)

    def redEnMemoria(self,dirrecionMemoria):
        return self.memoria.getBloqueMemoria(dirrecionMemoria).getDato()