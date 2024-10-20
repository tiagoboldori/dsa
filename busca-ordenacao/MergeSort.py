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

vetor = [1,10,8,6,3,15,4]
mergeSort(vetor)
print(vetor)
