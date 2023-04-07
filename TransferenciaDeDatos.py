from AlmacenamientoDeDatos import Memory


"""
/*
La tranferencia de datos se utiliza una simulacion del bus en la cual vamos a trabajar el intercambio de datos entre la parte de almacenamiento en MEMORIA

*/
"""
class Bus:
    def __init__(self):
        self.conections = []
        self.memory = Memory()
    """
    /*
    Con esta funcion no encargamos de escribir en memoria, cuando nos dan una dirrecion y un dato
    */
    """
    def writeToMemory(self, address, data):
        block = self.memory.getBlockByNumber(address)
        block.setData(data)
    """
    /*
    En caso de querer leer un dato en la direcion de memoria
    */
    """
    def readFromMemory(self, address):
        return self.memory.getBlockByNumber(address).getData()
