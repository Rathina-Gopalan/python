x=input()
y=[]
z=[]
for i in range(0,x):
    x=input()
    y.append(x)
for i in range(0,len(y)):
    if(i==y[i]):
        z.append(i)
if(len(z)==0):
    print("-1")
else:
    print(z)
