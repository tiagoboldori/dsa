from node import Node
from elemento import Elemento


class ListaEncadeada:

    def __init__(self):
        elemento = Elemento()
        no = Node(elemento)
        self.__cabeca = no
    

    def getCabeca(self):
        return self.__cabeca
    
    def setCabeca(self,cabeca):
        self.__cabeca = cabeca

    
    def listaVazia(self):
        return self.getCabeca().getProx() == None
    

    def insereNoFim(self, n):
        aux = self.getCabeca()
        while aux.getProx() != None:
            aux = aux.getProx()
        aux.setProx(n)

    def mostraLista(self):
        if not self.listaVazia():
            aux = self.getCabeca().getProx()

            while aux != None:
                print(aux.getElemento())
                aux = aux.getProx()
