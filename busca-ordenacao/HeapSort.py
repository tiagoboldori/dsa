def geraHeap(lista, n, i):

    maior = i #inicializa o maior como a raiz

    esquerda = 2*i + 1 #filhos da esquerda e da direita do nó/raíz em questao
    direita = 2*i + 2

    #verificando filho a esquerda da raiz
    if esquerda < n and lista[i] < lista[esquerda]:

        maior = esquerda

    #verificando filho a direita da raíz
    if direita < n and lista[i] < lista[direita]:
        maior = direita

    #modifica raiz caso necessario
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]

        #Gera o heap com a raiz
        geraHeap(lista ,n ,maior)

def heap(lista):

    n = len(lista)

    #constroi o heap maximo
    for i in range(n//2-1, -1, -1):
        geraHeap(lista, n ,i)

    #estraindo cada elemento e colocando na posição correta
    for i in range(n -1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        geraHeap( lista, i , 0)



vetor = [1,9,0,13,5,2,7]
heap(vetor)
print(vetor)
        
    
