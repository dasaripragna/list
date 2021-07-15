n=5
i=1
b=[]
while i<=n:
    j=1
    c=[]
    while j<=10:
        x=(i*j)
        c.append(x)
        j=j+1
    b.append (c)
    i=i+1
print(b)