from elemento import Elemento
from nodeb import NodeABB
from arvorebb import ArvoreBB

arvore = ArvoreBB()

while True:
    i = int(input('Digite a chave para o nó : '))
    if i == -1:
        break
    else:
        e = Elemento(i)
        n = NodeABB(e)
        arvore.insertNode(n)

    e = None
    n = None

print('arvore em ordem crescente: ')
arvore.mostraArvore(arvore.getRaiz())

print('arvore em ordem decrescente: ')
arvore.mostraDecrescente(arvore.getRaiz())

print('maior elemento: ')
arvore.mostraMaior(arvore.getRaiz())

print('menor elemento: ')
arvore.mostraMenor(arvore.getRaiz())

valor = int( input('valor a ser buscado: '))
print('resultado da busca: ', arvore.encontraValor(arvore.getRaiz(), valor) )
print('resultado da busca: ', arvore.encontraValorRec(arvore.getRaiz(), valor) )