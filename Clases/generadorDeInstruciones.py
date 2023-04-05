import numpy as np 
import random
import math



'''
La funncion de generar instrucion utiliza una distribucion geometrica por lo cual solo necesita calcular un numero random entreo 
entre el 0 y el 2 para generar el tipo de instruciopn
'''
def generarInstucion():
    valorInstruccion = random.randint(0, 2) #Distribucion geometrica
    if valorInstruccion == 0:
        return generarRead()
    if valorInstruccion ==1:
        return generarWrite()
    elif valorInstruccion == 2:
        return ['CALC']
    
"""
En caso que el valor de la instrucion generado por la distribucion probabilistica se 0 
se vean a terminar de generar los valores necesario como el bloque de memoria en bianrio
"""
    
def generarRead():
    memoryBlock = round(np.random.randint(0, 799)) // 100
    memoryBlockBin = decimalToBinario(memoryBlock, 3)
    return ["read", memoryBlockBin]


"""
En caso que el valor de la instrucion generado por la distribucion probabilistica se 0 
se vean a terminar de generar los valores necesario como el bloque de memoria en binario
y el valor del dato en hexadecimal 
"""

def generarWrite():
    memoryBlock = round(np.random.randint(0, 799)) // 100
    memoryBlockBin = decimalToBinario(memoryBlock, 3)
    data = round(np.random.uniform(0, 65535))
    dataHexa = decimalToHexadecimal(data, 16)
    return ["write", memoryBlockBin, dataHexa]


'''
Cambia el valor decimal a bianrio
'''

def decimalToBinario(decimal, nbits):
    binary = bin(decimal).replace("0b", "")
    finalBinary = "0" * (nbits - len(binary)) + binary
    return finalBinary

'''
Cambia el valor de deciaml a hexadecimal 
'''

def decimalToHexadecimal(decimal, nbits):
    hexadecimal = hex(decimal).replace("0x", "")
    finalhexadecimal = "0" * (math.ceil(nbits / 4) - len(hexadecimal)) + hexadecimal
    return finalhexadecimal



