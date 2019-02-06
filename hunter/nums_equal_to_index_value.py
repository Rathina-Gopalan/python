x=input()
y=[]
z=[]
for i in range(0,x):
    a=input()
    y.append(a)
for i in range(0,len(y)):
    if(i==y[i]):
        z.append(i)
if(len(z)==0):
    print("-1")
else:
    print(z)