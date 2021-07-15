n=int(input("enter position"))
i=1
c=0
b=[]
while n>=0:
    j=1
    f=0
    while j<=i:
        if i%j==0:
            f=f+1
        j=j+1
    if f==2:
        if c==n:
            #b.append(i) (or) print(i)
            break
        c=c+1
    i=i+1
print(b)