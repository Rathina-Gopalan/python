a=int(input())
n=0
while(a!=0):
  b=a%10
  n=n+b**2
  a=a//10
print(n)
