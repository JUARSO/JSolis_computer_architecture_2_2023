from AlmacenamientoDeDatos import L1Cache
from Instrucciones import *
import time

"""
/*
Con esta clase se van a menejar los tiempos y la ejecion del procesador
*/
"""

class InterfaceData:
    def __init__(self):
        self.mode="time"
        self.lastInstruction=""
        self.period = 2

"""
/*
Clase controlado se encarga del cumplimiento del protocolo de coherencia MOESI
*/
"""
class Controller:
    def __init__(self):
        self.l1cache = L1Cache()
    """
    /*
    En caso de un readMiss en la dirrecion de memoria
    */
    """
    def readMiss(self, address):
        block = self.l1cache.searchData(address) #Se le da el valor de bloque en la cache 
        if block is None:
            return None
        if block.getCoherence() == "M": #En caso de que el valor este modificado 
            block.setCoherence("O") # El nuevo valor sera O
            return block.getData() # Y devuelve el dato 
        elif block.getCoherence() == "O": #En caso que la coherencia de cache sea Owner
            return block.getData() #Se devuelve el valor del dato
        elif block.getCoherence() == "E": #En caso que que la conherencia sea Exclusivo
            block.setCoherence("S") #Ahora el nuevo estado sera compartido
            return block.getData() #Se debe de retunar el dato
        elif block.getCoherence() == "S": #En casp que de que la coheneria del bloque sea compartido 
            return block.getData() #Solo se retorna el dato 
        elif block.getCoherence() == "I": #En caso que la coherencia del dato sea Invalido 
            return None #No se retonar nada
    """
    /*
    En caso de tener que escribir en un bloque de cache
    */
    """
    def write(self,address,data):
        block = self.l1cache.getBlocktoWrite(address) #Se obtiene el valor del bloque de cache especifico
        if block.getCoherence() == "M": #En caso que la coheneria 
            if block.getAddress()==address:# Se revisa que al dirrecion de memoria sea la misma que la de la entras
                block.setData(data) #Se cambia el valor del dato
                return [["noAction"]] #Se retona no haga nada
            else: #En caso que la coherencia no sea modficaod
                action=[["WB",block.getAddress(),block.getData()],["writeMiss",address]] 
                block.setAddress(address) #Se cambia el valor de la dirrecion de memoria
                block.setData(data) #Se cambia el valor del dato
                return action
        elif block.getCoherence() == "O": #En caso que la cohereia del bloque sea Owner
            if block.getAddress()==address: #y la dirrecion de memeoria sea la misma
                block.setData(data) # Se cambia el valor del dato
                return [["writeMiss",address]] #Se retonar la accion a realizar
            else: #En caso la dirrecion de memoria sean distintas
                action=[["WB",block.getAddress(),block.getData()],["writeMiss",address]]#Se la accion
                block.setAddress(address) #Se cambia la direciond el bloque
                block.setData(data) #Se cambia el dato
                block.setCoherence("M") #Se cambia la cohenrencia a modificado
                return action #Se retorna la acion
        elif block.getCoherence() == "E": #En caso que el bloque de coheneria tenga un estado de Exclusivo
            block.setAddress(address) #Se cambia la direcion de memoria
            block.setData(data) #Se cambia el dato 
            block.setCoherence("M") #Se modifica el dato
            return [["noAction"]] #Y no se envia ninguna accion
        elif block.getCoherence() == "S": #En caso de que el dato sea compartido
            block.setAddress(address) #Se cambia la direcion de memoria
            block.setData(data) #Se cambia el el valor de la memoria
            block.setCoherence("M") #El estado pasa a ser modificado 
            return [["writeMiss",address]] #Envia la accion 
        elif block.getCoherence() == "I":
            block.setAddress(address) #Se cambia la direcion de memoria
            block.setData(data) #Se cambia el el valor de la memoria
            block.setCoherence("M") #El estado pasa a ser modificado 
            return [["writeMiss",address]] #Envia la accion 
    """
    /*
    En caso de WriteMiss
    */
    """
    def writeMiss(self,address): 
        block = self.l1cache.searchData(address) #Se guarda el bloque actual en la dirrecion de memoria
        if block is None: 
            return
        else:
            block.setCoherence("I") #Se cambia a estado invalido 

    """
    /*
    Peticion de lectura
    */
    """
    def readPetition(self,address):
        block = self.l1cache.searchData(address) #Se guarda el bloque de cache buscando una direcion especfica
        if block is None: #En caso de no haya nada
            return [["readMiss",address]] #Se envia la accion
        elif block.getCoherence() == "I": #En caso que el dato se invalido
            return [["readMiss",address]] #Se envia la ascion
        return [["hit",block.getAddress(),block.getData()]] #En caso que el daro
    """
    /*
    Hace una lectura en cache
    */
    """
    def read(self,address,data,dataFrom):
        block = self.l1cache.getBlocktoWrite(address)
        action = ["noAction"]
        if block.getAddress() != address:
            if block.getCoherence() == "O" or block.getCoherence() == "M":#En caso que el dato sea Owner o Modificiado
                action = ["WB", block.getAddress(), block.getData()] #Se encia la accion de WB
        block.setAddress(address)#Se cambia la dirrecio de memoria
        block.setData(data) #Se cambia el dato
        if dataFrom == "memory": #Si el dato viene de memoria
            block.setCoherence("E")
        else:#Si el dato viene de otra cache
            block.setCoherence("S")
        return action

"""
/*
Se crea una abstacion para la CPU
*/
"""
class Cpu:
    def __init__(self, number, bus, mutex, interfaceData):
        self.number = number #Numero de procesador
        self.controller = Controller() #Controlador del procesador
        self.bus = bus #Bus del procesador
        self.currentInstruction = "" #Instrucion Actual
        self.currentInstructionList = []
        self.mutex = mutex #Protecion de los recursos compartidos
        self.interfaceData = interfaceData #Interface de datos
        self.manualInstruction = [] #Lista de instruciones
        self.nextCycle = False #Siguiente ciclo
        self.lastInstruction = "" #Ultima instrucion
        self.lastInstructionList = []
        self.continueProcess = True #Continue con el proceso


    """
    /*
    Funcion que obtiene la isntrucion Actual
    */
    """
    def getInstruction(self):
        while True:
            instruction = generarInstucion() #Se genera una nueva instrucion al proceso
            actions = []
            if instruction[0] == "calc": #Si la instrucin es CALC
                self.currentInstruction = "P" + str(self.number) + " CALC: " #Instrucin Actua;
                self.currentInstructionList = ['P'+ str(self.number) , " CALC: "]
                actions = [["noAction"]] #No hace nada
            elif instruction[0] == "write": #En caso que la isntrcuin sea un WRITE
                self.currentInstruction = "P" + str(self.number) + " WRITE: " + instruction[1] + ' ' + instruction[2] #Se escribe en la instrucion
                actions = self.controller.write(int(instruction[1], 2), int(instruction[2], 16)) #Envia la accion
            elif instruction[0] == "read": #Si la instrucion es un reas
                self.currentInstruction = "P" + str(self.number) + " READ: " + instruction[1] #Instrucion de read
                actions = self.controller.readPetition(int(instruction[1], 2)) #Se agrega la accion
            #self.log(self.currentInstruction + " cache: |" + self.controller.l1cache.getstring())
            self.interfaceData.lastInstruction = self.currentInstruction #se agrega la isntruccion
            self.manageBus(actions)#Acciones del bus
            self.lastInstruction = self.currentInstruction #Nueva instrucon
            self.applyMode() #Se ejecuta
    """
    /*
    Funcion que se encarga del manejo del bus
    */
    """
    def manageBus(self, actions):
        action = actions[0] #Se agrega la reacion Actual
        if action[0] != "noAction" and action[0] != "hit": #En caso que no haya accion o sea un hit
            self.mutex.acquire() # Solicita el mutex
            if len(actions) == 2: #Si hay dos acciones
                self.bus.writeToMemory(action[1], action[2]) #Se ejecuta la accion en la posicion 1, 2
                self.applyMode() #Se ejecuta el ApplyMode
                action = actions[1] #Se agrga la acion atual
            if action[0] == "readMiss":#En caso que la acion actual sea igual a read mis
                self.waitResponse(action[1]) #Se ejecuta espera una respuesta
            elif action[0] == "writeMiss":#En caso que accion sea un WriteMiss
                self.Invalidate(action[1]) #Se ejecuta invalidar accion
            self.mutex.release() #Libera el mutex
    """
    /*
    Controla el WaitResponse , recive la direcion de memoria
    */
    """
    def waitResponse(self, address):
        data = None
        for i in range(4):
            if i != self.number:
                readed = self.bus.conections[i].controller.readMiss(address)
                if readed is not None:
                    data = readed
        if data is None:
            data = self.bus.readFromMemory(address) #Se hace un read en memoria
            self.applyMode()
            action = self.controller.read(address, data, "memory") #Hace un read en memoria
        else:
            action = self.controller.read(address, data, "cache") #Hace un read en cache
        if action[0] == "WB": #Revisa si la accion es un WB
            self.bus.writeToMemory(action[1], action[2]) #Se llama a escribir en memoria
            self.applyMode() #Se ejecuta applyMode
    """
    /*
    */
    """
    def Invalidate(self, address):
        for i in range(4):
            if i != self.number:
                self.bus.conections[i].controller.writeMiss(address)
    """
    /*
    Ejecucion del ApplyMode
    */
    """
    def applyMode(self):
        while True:
            if self.continueProcess:
                break
        time.sleep(self.interfaceData.period) #Espera el tiempo del periodo

