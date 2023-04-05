from Clases.BloqueCacheL1 import BloqueCacheL1
import numpy as np

class CachceL1:
    def __init__(self):
        self.sets = [
            [BloqueCacheL1(0, "I", 0, 0), BloqueCacheL1(1, "I", 0, 0)],
            [BloqueCacheL1(2, "I", 0, 0), BloqueCacheL1(3, "I", 0, 0)]
        ]
    
    def getSets(self):
        return self.sets
    
    def getBlock(self,numero):
        return self.sets[numero // 2][numero % 2]
    

    def getSet(self, numero):
        return self.sets[numero]
    
    def getTodosLosBloques(self):
        return self.sets[0] + self.sets[1]
    
    def buscarDatos(self, dirrecionMemoria):
        set = self.getSet(dirrecionMemoria % 2)
        for block in set:
            if block.getDirrecionMemoria() == dirrecionMemoria:
                if block.getDirrecionMemoria() == 0 and block.getDato() == 0 and block.getCoherencia() == "I":
                    return None
                else:
                    return block
            return None

    def getBloqueDeRemplazo(self, dirrecionMemoria):
        selector = round(np.random.randint(0, 799)) // 100
        set = self.getSet(dirrecionMemoria % 2)
        block = set[selector]
        return block
    
    def getBloqueLibre(self, dirrecionMemoria):
        set = self.getSet(dirrecionMemoria)
        for block in set:
            if block.getCoherencia()  == 'I':
                return block
        return None
    
    def getBloqueWrite(self, dirrecionMemoria):
        bloque = self.buscarDatos(dirrecionMemoria)
        if bloque is None:
            bloque = self.getBloqueDeRemplazo(dirrecionMemoria)
            return bloque
        else:
            return bloque
        
    def getString(self):
        dato = ''
        for bloque in self.getTodosLosBloques():
            dato += bloque.getString()
            dato += '\n'
        return dato