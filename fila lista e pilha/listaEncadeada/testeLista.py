from node import Node
from listaEncadeada import ListaEncadeada
from elemento import Elemento


lista = ListaEncadeada()


i = input('Digite um nome para o no : ')
while i != '':
    c = int(input('Digite uma chave : '))
    e = Elemento(i, c)
    n = Node(e)
    lista.insereNoFim(n)
    c = None
    i = input('Digite um nome para o no : ')
    

lista.mostraLista()
