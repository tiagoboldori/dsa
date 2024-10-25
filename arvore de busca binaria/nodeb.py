from elemento import Elemento

class NodeABB:

    def __init__(self, elemento):

        self.__data = elemento
        self.__nodeLeft = None
        self.__nodeRight = None


    def getData(self):
        return self.__data
    
    def setData(self, d):
        self.__data = d
    

    def getChave(self):
        return self.getData().getChave()
    
    def getValores(self):
        return self.getData().getValores()


    def getNodeLeft(self):
        return self.__nodeLeft
    
    def setNodeLeft(self, n):
        self.__nodeLeft = n
    

    def getNodeRight(self):
        return self.__nodeRight
    
    def setNodeRight(self, n):
        self.__nodeRight = n


    def isFolha(self):
        return self.getNodeLeft()==None and self.getNodeRight() == None
    

    def onlyLeftNode(self):
        return self.getNodeLeft() != None and self.getNodeRight() == None
    
    def onlyRightNode(self):
        return self.getNodeRight() != None and self.getNodeLeft() == None
    