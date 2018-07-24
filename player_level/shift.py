def shift(x,y,z):
	r=[]
	for i in range(x-y,x):
		r.append(z[i])
	for i in range(x-y):
		r.append(z[i])
	print(r)
def main():
		a=int(input())
		b=int(input())
		c=[]
		for i in range(n):
			c.append(input())
		shift(a,b,c)
main()
