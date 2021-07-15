n=[10,10,10,10,20,20,20,20,40,40,50,50,70]
i=0
b=[]
while i<len(n):
    if n[i]not in b:
        b.append(n[i])
        j=0
        c=0
        while j<len(n):
            if n[i]==n[j]:
                c=c+1
            j=j+1
        print(n[i],":",c)
    i=i+1       
    # frequency