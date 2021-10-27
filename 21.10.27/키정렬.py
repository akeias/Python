Li=[162,187,176,182,165,172,154]


for t in range(0,len(Li),1):
    k = len(Li)-t
    for i in range(0,k-1):
        if(Li[i]>=Li[i+1]):
            temp=Li[i]
            Li[i]=Li[i+1]
            Li[i+1]=temp

print(Li)
