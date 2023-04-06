from Clases.BloqueDeMemoria import bloqueMemoria


class Memoria:
    def __init__(self):
        self.bloquesDeMemoria =[
            bloqueMemoria(0,0),
            bloqueMemoria(1,0),
            bloqueMemoria(2,0),
            bloqueMemoria(3,0),
            bloqueMemoria(4,0),
            bloqueMemoria(5,0),
            bloqueMemoria(6,0),
            bloqueMemoria(7,0),
        ]

    def getBloqueMemoria(self, numeroDeBloque):
        return self.bloquesDeMemoria[numeroDeBloque]
    
    def getString(self):
        dato =''
        for bloque  in self.bloquesDeMemoria:
            dato += bloque.getString()
            dato += '/'
            if bloque.numero%2 == 1:
                dato +="\n"
        return dato
