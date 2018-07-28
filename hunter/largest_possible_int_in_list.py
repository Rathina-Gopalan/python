a=int(input())
b=[]
for i in range(a):
    b.append(input())
b.sort()
c=b[::-1]
d="".join(c)
print(d)
