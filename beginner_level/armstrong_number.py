a = list(input())
c=0
d="".join(a)
b=len(a)
for i in a:
   c=c+(int(i)**b)
if int(d)==c:
  print("yes")
else:
  print("no")
