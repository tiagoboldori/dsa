import random


#HEAP SORT
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





#QUICK SORT
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


# MERGE SORT
def mergeSort(lista):

    print("Dividindo", lista)

    if len(lista)>1:

        meio = len(lista)//2

        metadeEsquerda = lista[:meio]

        metadeDireita = lista[meio:]


        mergeSort(metadeEsquerda)
        mergeSort(metadeDireita)

        i=0
        j=0
        k=0

        while i < len(metadeEsquerda) and j < len(metadeDireita):

            if metadeEsquerda[i] < metadeDireita[j]:

                lista[k] = metadeEsquerda[i]

                i+=1

            else:

                lista[k] = metadeDireita[j]

                j+=1
                
            k+=1

        while i < len(metadeEsquerda):

            lista[k] = metadeEsquerda[i]

            i+=1
            k+=1

        while j < len(metadeDireita):

            lista[k] = metadeDireita[j]

            j+=1
            k+=1
        
        print("Merging", lista)
        return lista




ordenado1 = [i for i in range(5000)]
ordenado2 = [i for i in range(10000)]

inverso1 = [i for i in range(5000,0,-1)]
inverso2 = [i for i in range(10000,0,-1)]


aleatorio1 = [random.randint(0,1000) for i in range(5000)]
aleatorio2 = [random.randint(0,1000) for i in range(10000)]
