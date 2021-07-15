n=1
i=10
b=[]
while n<=i:
    j=1
    f=0
    while j<=n:
        if n%j==0:
            f=f+1
        j=j+1
    if f==2:
        b.append(n)
    n=n+1
print(b)   