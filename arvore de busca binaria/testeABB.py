from elemento import Elemento
from nodeb import NodeABB
from arvorebb import ArvoreBB

arvore = ArvoreBB()

while True:
    print('Opções: \n 1-Criar/Adicionar nós a arvore. \n 2-Remover nó da arvore. \n 3- Procurar elemento na arvore. \n 4-Mostrar Arvore. \n 5-Mostrar maior e menor elemento da arvore. \n 6-Mostrar numero de elementos na arvore \n 7-Mostrar soma das chaves da arvore \n (-1 para sair)')
    info = int(input('Digite um numero correspondente as opções: '))
    if info ==-1:
        break

    if info ==1:
        print('Adicionando elementos a arvore!')

        while True:
            i = int(input('Digite a chave para o nó : '))
            if i == -1:
                break
            else:
                nome = input('Nome do nó: ')
                e = Elemento(i, nome)
                n = NodeABB(e)
                arvore.insertNode(n)

            e = None
            n = None
            
    if info == 2:
        
        i = int(input('Chave do nó a ser removido: '))
        if i != -1:
            arvore.rmNode(arvore, arvore.getRaiz(), i)

    if info==3:
        i = int(input('Digite o valor a ser buscado na arvore: '))
        print('resultado da busca: ', arvore.encontraValorRec(arvore.getRaiz(), i))
    
    if info == 4:
        print('arvore em ordem crescente: ')
        arvore.mostraArvore(arvore.getRaiz())

        print('arvore em ordem decrescente: ')
        arvore.mostraDecrescente(arvore.getRaiz())

    if info ==5:
        arvore.mostraMaior(arvore.getRaiz())
        arvore.mostraMenor(arvore.getRaiz())
    
    if info ==6:
        print('quantidade de nos: ', arvore.contaNos(arvore.getRaiz()))
    
    if info == 7:
        print('soma das chaves: ', arvore.contaChave(arvore.getRaiz()))
