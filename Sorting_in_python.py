List=[90,80,90,40,50,60]
temp=0
for i in range(0,len(List)):
    for j in range(0,len(List)):
        if List[i]<List[j]:
            temp=List[i]
            List[i]=List[j]
            List[j]=temp