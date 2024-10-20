

class Node:

    def __init__(self, elemento):
        self.__elemento = elemento
        self.__prox = None


    #get/set info
    def getElemento(self):
        return self.__elemento
    
    def setInfo(self, elemento):
        self.__elemento = elemento

    #get/set proximo
    def getProx(self):
        return self.__prox
    
    def setProx(self, prox):
        self.__prox = prox
