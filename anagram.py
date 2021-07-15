n="chin"
m="inch"
b=""
i=0
while i<len(n):
    if n[i] in m:
        b=b+n[i]
    i=i+1
if len(m)==len(b):
    print("anagram")
else:
    print("not")