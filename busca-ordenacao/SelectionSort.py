vetor = [3,6,2,0]

def selectionSort(lista):

    #for iterando a lista de tras para frente
    for i in range(len(lista)-1, 0, -1):

        posMaior=0

        for local in range(1, i+1):

            if lista[local]>lista[posMaior]:
                posMaior = local

        lista[i], lista[posMaior] = lista[posMaior], lista[i]
        
    return lista

print(selectionSort(vetor))
