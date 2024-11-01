from elemento import Elemento
from nodeb import NodeABB
from arvorebb import ArvoreBB

arvore = ArvoreBB()

nodes = [8, 13 , 6, 7, 3, 1, 4, 5, 16, 17, 11, 10, 23, 21, 30, 19, 22]

for i in nodes:
    e = Elemento(i)
    n = NodeABB(e)
    arvore.insertNode(n)
    n = None
    e = None

aux = arvore.getInfoByKey(arvore.getRaiz(), arvore.getRaiz(), 16)

arvore.mostraArvore(arvore.getRaiz())

arvore.rmNode(arvore, arvore.getRaiz(), 17)
print('')

print(arvore.getRaiz().getNodeRight().getChave())
print(arvore.getRaiz().getNodeRight().getNodeRight().getChave())
arvore.mostraArvore(arvore.getRaiz())