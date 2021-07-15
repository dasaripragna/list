n=[10,20,30,40,20,50,60,40,10,30,60,50,30,2,24]
i=0
b=[]
while i<=len(n):
    if n[i]not in b:
        b.append (n[i])
    i=i+1
print(b)  