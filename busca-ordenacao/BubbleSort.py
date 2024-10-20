#BubbleSort
count = 0
vetor=[]

while True:
    a = int(input('digite um numero , -1 para sair'))

    if a ==-1:
        break
    else:
        vetor.append(a)
    count+=1

def bubble(v):
    cont=0
    for i in range(0, len(v)):
        for j in range(0, len(v)-1):
            cont+=1
            if v[j]>v[j+1]:
                v[j],v[j+1]=v[j+1],v[j]
    return v,cont

def betterBubble(v):
    cont=0
    for i in range(0,len(v)-1):
        for j in range(len(v)-1,i,-1):
            cont+=1
            if v[j]<v[j-1]:
                v[j],v[j-1]=v[j-1],v[j]
    return v,cont


print(bubble(vetor))
print(betterBubble(vetor))
