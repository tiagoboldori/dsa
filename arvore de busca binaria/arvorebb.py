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
        else:
            self.mostraMaior(n.getNodeRight())

    def mostraMenor(self, n):
        if n.getNodeLeft() is None:
            print('menor numero: ', n.getChave())
        else: 
            self.mostraMenor(n.getNodeLeft())

    def getMaior(self, n):
        if n.getNodeRight() is None:
            return n
        else:
            self.getMaior(n.getNodeRight())

    def getMenor(self, n):
        if n.getNodeLeft() is None:
            return n
        else:
            self.getMenor(n.getNodeLeft())

    def mostraDecrescente(self, n):
        if n is not None:
            self.mostraDecrescente(n.getNodeRight())
            print(n.getValores())
            self.mostraDecrescente(n.getNodeLeft())
    

    #ENCONTRAR VALOR V NA ARVORE
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
    
    #####################################################

    #REMOVE NO DA ARVORE

    def rmNode(self, arvore, n, v):

        temp = self.getInfoByKey(n, n, v)
        

        if not temp['root']:
            #CASO FOLHA
            if temp['node'].isFolha():

                if temp['pai'].getNodeRight() == temp['node']:

                    temp['pai'].setNodeRight(None)
                else:
                    temp['pai'].setNodeLeft(None)

            #CASO APENAS FILHO DE UM LADO
            elif temp['node'].onlyLeftNode():

                if temp['pai'].getNodeRight() == temp['node']:
                    temp['pai'].setNodeRight(temp['node'].getNodeLeft())
                else:
                    temp['pai'].setNodeLeft(temp['node'].getNodeLeft())

            elif temp['node'].onlyRightNode():

                if temp['pai'].getNodeRight() == temp['node']:
                    temp['pai'].setNodeRight(temp['node'].getNodeRight())
                else:
                    temp['pai'].setNodeLeft(temp['node'].getNodeRight())

            #CASO CONTRARIO:
            else:

                aux = self.getInfoByKey(temp['node'], temp['node'].getNodeRight(), self.getMenor(temp['node']))

                if temp['node'] == temp['pai'].getNodeRight():
                    temp['pai'].setNodeRight(aux['node'])
                else:
                    temp['pai'].setNodeLeft(aux['node'])

                if aux['pai'].getNodeLeft() == aux['node']:
                    aux['pai'].setNodeLeft(None)
                else:
                    aux['pai'].setNodeRight(None)

                aux['node'].setNodeRight(temp['nodeRight'])
                aux['node'].setNodeLeft(temp['nodeLeft'])
                temp['node'].setNodeRight(None)
                temp['node'].setNodeLeft(None)


    def getInfoByKey(self, pai, atual, v):
        if atual is not None:
            if pai.getChave() == atual.getChave():
                if v == atual.getChave():
                    return {
                    'root':True,
                    'nodeRight': atual.getNodeRight(),
                    'nodeLeft': atual.getNodeLeft(),
                    'pai':None,
                    'node': atual
                    }
                if v > atual.getChave():
                    return self.getInfoByKey(pai, atual.getNodeRight(), v)
                if v < atual.getChave():
                    return self.getInfoByKey(pai, atual.getNodeLeft(), v)
            else:
                if v == atual.getChave():
                    return{
                        'root':False,
                        'nodeRight': atual.getNodeRight(),
                        'nodeLeft': atual.getNodeLeft(),
                        'pai': pai,
                        'node': atual
                    }
                if v > atual.getChave():
                    return self.getInfoByKey(atual , atual.getNodeRight(), v)
                if v < atual.getChave():
                    return self.getInfoByKey(atual , atual.getNodeLeft(), v)
                
        print('Elemento fora da lista')

