import random

class Fila:
    def __init__(self):
        self.__dados = []
    
    def filaVazia(self):
        return len(self.__dados)==0
    
    def enfileirar(self,x):
        self.__dados.append(x)
    
    def desenfileirar(self):
        x = None
        if self.filaVazia() == False:
            x = self.__dados.pop(0)
        return x
    
    def __str__(self):
        return str(self.__dados)
    

teste = Fila()

for i in range (10):
    teste.enfileirar(random.randint(0,30))

print(teste)