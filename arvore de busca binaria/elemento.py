
class Elemento:

    def __init__(self, chave = None , nome = ''):
        self.__chave = chave
        self.__nome = nome


    def getChave(self):
        return self.__chave

    def setChave(self, chave):
        self.__chave = chave


    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome


    def getValores(self):
        return self.getChave(), self.getNome()