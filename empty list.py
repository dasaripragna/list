a=[]
b=[1,11,2,34,56,78,9,1,10,2,12,11,78,56]
i=0
while i<len(b):
    if b[i] not in a:
        a.append(b[i])
    i=i+1
print(a)