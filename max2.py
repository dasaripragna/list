a=[1,2,3,4,5,6]
max=0
max_1=0
i=0
while i<len(a):
    if a[i]>max:
        max_1=max
    max=a[i]
    if max_1<a[i] and max>a[i]:
        max=a[i]
    i=i+1
print(max_1)     