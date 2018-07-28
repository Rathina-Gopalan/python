n=int(input())
b=[]
e=[]
for f in range(0,n):
    a=input()
    b.append(a)
   
for c in range(0,len(b)):
    for d in range(c+1,len(b)):
        if(b[c]==b[d]):
            e.append(b[c])
e.sort()
print(" ".join(e))
