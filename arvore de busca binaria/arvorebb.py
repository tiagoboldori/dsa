class ArvoreBB:

    def __init__(self):
        self.__raiz = None


    def getRaiz(self):
        return self.__raiz
    
    def setRaiz(self, node):
        self.__raiz = node


    def arvoreVazia(self):
        return self.getRaiz() == None
    

    def insert(self, pai, node):
        if node.getChave() < pai.getChave():
            if pai.getNodeLeft()==None:
                pai.setNodeLeft(node)
            else:
                self.insert(pai.getNodeLeft(), node)

        else:
            if pai.getNodeRight()==None:
                pai.setNodeRight(node)
            else:
                self.insert(pai.getNodeRight(), node)


    def insertNode(self, node):
        if self.arvoreVazia():
            self.setRaiz(node)
        else:
            self.insert(self.getRaiz(), node)
    


    def mostraArvore(self, n):
        if n != None:
            self.mostraArvore(n.getNodeLeft())
            print(n.getValores())
            self.mostraArvore(n.getNodeRight())
    
    
    


    #EXERCICIOS
    def mostraMaior(self, n):
        if n.getNodeRight() is None:
            print('maior numero: ',n.getChave())
            return n
        else:
            self.mostraMaior(n.getNodeRight())

    def mostraMenor(self, n):
        if n.getNodeLeft() is None:
            print('menor numero: ', n.getChave())
            return n
        else: self.mostraMenor(n.getNodeLeft())

    def getMaior(self, n):
        if n.getNodeRight() is None:
            return n
        else:
            self.mostraMaior(n.getNodeRight())

    def mostraDecrescente(self, n):
        if n is not None:
            self.mostraDecrescente(n.getNodeRight())
            print(n.getValores())
            self.mostraDecrescente(n.getNodeLeft())
            
    def encontraValor(self, n, v):
        while n is not None:
            if n.getChave() == v:
                return True
            
            if v > n.getChave():
                n = n.getNodeRight()
            if v < n.getChave():
                n = n.getNodeLeft()
        return False

    def encontraValorRec(self, n, v):
        if n is not None:
            if v == n.getChave():
                return True
            if v > n.getChave():
                return self.encontraValorRec(n.getNodeRight(), v)
            if v< n.getChave():
                return self.encontraValorRec(n.getNodeLeft(), v)
        return False