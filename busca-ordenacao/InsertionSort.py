#InsertionSort

#dado o vetor
v=[3,1,0,7,2]

def insertionSort(v):
    for i in range(1,len(v)):
        aux=v[i]
        j=i-1
        while j>=0 and aux<v[j]:
            v[j+1]=v[j]
            j-=1
        v[j+1]=aux
    return v

print(insertionSort(v))