import random

class Pilha:

    def __init__(self):

        self.__dados = []

    def pilhaVazia(self):

        return len(self.__dados)==0
    
    def empilha(self, x):
        self.__dados.append(x)

    def desempilha(self):
        if not self.pilhaVazia():
            self.__dados.pop()
    
    def __str__ (self):
        return str(self.__dados)

    
teste = Pilha()

for i in range(10):
    teste.empilha(random.randint(0,10))

print(teste)

teste.desempilha()

print(teste)