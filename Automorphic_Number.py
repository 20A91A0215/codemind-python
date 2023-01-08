n=int(input())
m=n*n
m=str(m)
p1=str(n)
l=len(p1)
if(n==int(m[-l:])):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")