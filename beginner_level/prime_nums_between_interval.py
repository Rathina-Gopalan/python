x = int(input())
y = int(input())
c=[]
for n in range(x,y + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           c.append(str(n));
b=" ".join(c);
print(b)
