

class Elemento:

    def __init__(self, nome = '',chave = None):
        self.__chave = chave
        self.__nome = nome
    

    def setChave(self, chave):
        self.__chave = chave
        
    def getChave(self):
        return self.__chave
    

    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    

    def __str__(self):
        return str(str(self.getChave()) + ' ' + self.getNome())