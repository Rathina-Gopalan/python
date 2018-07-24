a=int(input())
b=int(input())
c=[]
for i in range(a+1,b):
    if(i%2!=0):
       c.append(str(i))
d=" ".join(c)
print(d)
