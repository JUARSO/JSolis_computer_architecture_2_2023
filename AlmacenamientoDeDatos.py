from Instrucciones import *


'''
/*
Se realiza una abstracion de un bloque de memoria el cual utiliza su numero de bloque y el valor que tiene asinado
*/
'''

class MemoryBlock:

    def __init__(self, number, data):
        self.number = number #Numero de bloque de memoria
        self.data = data #Numero de dato

    '''
    /*
    Esta funcion se encarga de obtener el numero de bloque de memoria del bloque actual
    */
    '''

    def getNumber(self):
        return int(str(self.number),2) #Obtiene el numero de bloque


    '''
    /*
    Se obtiene el valor almacenado en el numero de bloque de memoria actual
    */
    '''

    def getData(self):
        return int(str(self.data),16) #Obtiene valor de memoria

    '''
    /*
    Se cambia el valor almacenado en el numero de bloque de memoria actual
    */
    '''

    def setData(self, data):
        self.data = decimalToHexadecimal(data,16) #Se cambia el valor del dato

    '''
    /*
    Con esta funcion vamos a obtener un strin con el  Bloque: el valor en binario del numero del bloque
    y el valor en hexadecimal
    */
    '''

    def getstring(self):
        return [str(decimalToBinario(self.number, 3)), str(self.data)] #Se obtiene el numero de bloque y el valor del dato 

'''
/*
Con esta clase realizamos una abstracion de la memoria 
*/
'''    
class Memory:
    def __init__(self):
        self.blocks = [
            MemoryBlock(0, 0),
            MemoryBlock(1, 0),
            MemoryBlock(2, 0),
            MemoryBlock(3, 0),
            MemoryBlock(4, 0),
            MemoryBlock(5, 0),
            MemoryBlock(6, 0),
            MemoryBlock(7, 0)
        ]

    '''
    /*
    Se obtiene un bloque de memoria segun su numero
    */
    '''
    def getBlockByNumber(self, number):
        return self.blocks[number]

    '''
    /*
    Se obtiene los datos de manera de string de de bloque de memoria y el valor que este tiene
    */
    '''

    def getstring(self):
        data=[]
        for block in self.blocks: #De todos lo bloques de memoria
            data+=[block.getstring()] #Se agraga el dato a la memoria
        return data

'''
/*
En esta clase se realiza la abstracion un bloque unico de la cache L1
*/
'''        
class L1CacheBlock():
    def __init__(self, number, coherence, data, address):
        self.number = number #Numero de cache
        self.coherence = coherence #Valor de la coherencia de cache
        self.data = data #Valor del dato guardado en cache
        self.address = address #Valor de la dirrecion de memoria donde se encuentra la cache
    '''
    /*
    Se obtiene el numero del valor de cache actual
    */
    '''
    def getNumber(self):
        return self.number #Se otiene el valor del bloque de cache


    '''
    /*
    Se obtiene el estado actual de la cache
    */
    '''
    def getCoherence(self):
        return self.coherence #Se envia la cohenrecia de la cache
    '''
    /*
    Se cambia el estado actual de la cache
    */
    '''
    def setCoherence(self, coherence):
        self.coherence = coherence #Se cambia el valor de la coherencia
    '''
    /*
    Se obtiene el valor actual del dato almacenado en la cache
    */
    '''
    def getData(self):
        return int(str(self.data), 16) #Se obtiene el valor actual del dato del bloque de cache
    '''
    /*
    Se cambia el dato almacenado en la cahce
    */
    '''
    def setData(self, data):
        self.data = decimalToHexadecimal(data, 16) #Se obtiene el valor del dato en el bloque de cache
    '''
    /*
    Se obtiene la direcion de memoria de la cache actual
    */
    '''
    def getAddress(self):
        return int(str(self.address), 2) #Se obtiene la direcion actual del bloque de cache 
    '''
    /*
    Se cambia la direcion de memoria de la cache actual
    */
    '''
    def setAddress(self, address):
        self.address = decimalToBinario(address, 3) #Se cambia la dirrecion del bloque de cache
    '''
    /*
    Se obtiene con la informacion de un bloque de la cache L1
    */
    '''
    def getstring(self):
        return ['B'+ str(self.number) , str(self.coherence) ,  str(self.address), str(self.data)] #Se obtiene los valores detro de la cache

'''
/*
Se realiza una abstracion de la memoria cache
*/
'''    
class L1Cache:
    def __init__(self):
        self.sets = [[L1CacheBlock(0, "I", 0, 0), L1CacheBlock(1, "I", 0, 0)],[L1CacheBlock(2, "I", 0, 0), L1CacheBlock(3, "I", 0, 0)]]

    def getSets(self):
        return self.sets


    '''
    /*
    Se obtiene el set de memoria cahce l1 segun su numero
    */
    '''
    def getSet(self, setNumber):
        return self.sets[setNumber] 
    '''
    /*
    Se obtienen todos los bloques de memoria cache L1
    */
    '''
    def getAllBlocks(self):
        return self.sets[0] + self.sets[1]
    '''
    /*
    Se busca un dato de memoria, de la cache segun la dirrecion de memoria
    */
    '''
    def searchData(self, address): #Para buscar el dato
        set = self.getSet(address % 2) #Se calcual cual de los dos set se van a utitlizar %2 para obtener el set 
        for block in set: 
            if block.getAddress() == address:
                if block.getAddress() == 0 and block.getData() == 0 and block.getCoherence() == "I":
                    return None
                else:
                    return block #Devuelve el set
        return None
    '''
    /*

    */
    '''
    def getBlockByReplacePolicy(self, address):
        selector = round(np.random.uniform(0, 199)) // 100 
        set = self.getSet(address % 2) #Con esto seleciono el set a utilizar
        block = set[selector] #Seleciona el valor del selector
        return block
    '''
    /*
    Se busca un bloque de memoria cache el cual se encuente libre para escribir en el 
    */
    '''
    def getFreeBlock(self, address):
        set = self.getSet(address % 2) #Con esto seleciono el set a utilizar
        for block in set:
            if block.getCoherence() == "I": #En caso la coherencia del bloque este libre lo libera
                return block
        return None
    '''
    /*
    Se obtiene un bloque de memoria en el cual se pueda escribir
    */
    '''
    def getBlocktoWrite(self, address):
        block = self.searchData(address) 
        if block is None:
            block = self.getFreeBlock(address) 
            if block is None:
                block = self.getBlockByReplacePolicy(address)
            return block
        else:
            return block
    '''
    /*
    Se escribe la informacion de cada uno de los bloques de la Cache
    */
    '''
    def getstring(self):
        data=[]
        for block in self.getAllBlocks():
            data+=[block.getstring()]
        return data
